# coding=utf-8
import logging, json, re
from datetime import datetime
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.datastructures import DotExpandedDict
from django.shortcuts import render, render_to_response, redirect

from django.views.decorators.csrf import csrf_exempt
from servo.models import *
from django import forms

class SidebarForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'queue', 'status', 'priority']

def index(req, param = None, value = None):
    data = Order.objects.all()

    if param == "status":
        status = Status.objects.get(id = value)
        data = status.order_set.all()

    if param == "user":
        try:
            user = User.objects.get(username = value)
            data = user.order_set.all()
        except Exception, e:
            data = Order.objects.all()

    if param == "customer":
        customer = Customer.objects.get(id = value)
        data = customer.order_set.all()

    return render(req, 'orders/index.html', {'data' : data})

def create(req):
    user = req.session.get('user')
    o = Order.objects.create(created_by=user, created_at=datetime.now())

    desc = 'Tilaus %d luotu' % o.id
    Event.objects.create(description=desc, order=o,
        type='create_order', user=user)

    return redirect('/orders/edit/%d' % o.id)

def tags(req, id):
    if 'title' in req.POST:
        order = Order.objects.get(pk = id)
        title = req.POST['title']
    
    if title not in order.tags:
        order.tags.append(title)
        order.save()
    
    if len(Tag.objects(title=title, type='order')) < 1:
        tag = Tag.objects.create(title=title, type='order')
    
    return HttpResponse(json.dumps({order.tags}), content_type='application/json')
  
def edit(req, id):
    o = Order.objects.get(pk = id)

    req.session['order'] = o
    
    form = SidebarForm(instance=o)
    users = User.objects.all()
    queues = Queue.objects.all()
    statuses = Status.objects.all()
    priorities = ['Matala', 'Normaali', 'Korkea']

    return render(req, 'orders/edit.html', {
        'order': o,
        'queues': queues,
        'users': users,
        'statuses': statuses,
        'priorities': priorities,
        'form': form
        })

def remove(req, id = None):
    if 'id' in req.POST:
        order = Order.objects.get(id = req.POST['id'])
        #Inventory.objects(slot = order).delete()
        order.delete()
        return HttpResponse('Tilaus poistettu')
    else :
        order = Order.objects.get(pk = id)
        return render(req, 'orders/remove.html', {'order': order})

def follow(req, id):
    order = Order.objects.get(pk = id)
    order.followed_by.add(req.session.get('user'))
    return HttpResponse('%d seuraa' % order.followed_by.count())

@csrf_exempt
def update(req, id):
    order = Order.objects.get(pk = id)

    if 'queue' in req.POST:
        queue = Queue.objects.get(pk = req.POST['queue'])
        order.queue = queue
        order.save()
        event = Event.objects.create(description = queue.title,
            order = order,
            type = 'set_queue',
            user = req.session.get('user')
        )
    
    if 'status' in req.POST:
        from time import time
        status_id = req.POST.get('status')
        status = Status.objects.get(pk = status_id)
        # calculate when this status will timeout
        green = (status.limit_green*status.limit_factor)+time()
        yellow = (status.limit_yellow*status.limit_factor)+time()
        req.session['order'].status_limit_green = green
        req.session['order'].status_limit_yellow = yellow
        req.session['order'].status = status
        req.session['order'].save()

        event = Event.objects.create(description = status.title,
            order = req.session['order'],
            type = 'set_status',
            user = req.session.get('user'))
    
    if 'user' in req.POST:
        user = req.POST['user']
        user = User.objects.get(id = user)
        req.session['order'].user = user
        req.session['order'].save()
        event = Event.objects.create(description=user.fullname,
            order=req.session['order'], 
            type='set_user',
            user=req.session.get('user'))
    
    if 'priority' in req.POST:
        req.session['order'].priority = req.POST['priority']
        req.session['order'].save()

    return render(req, "orders/events.html", {"order": order})
  
def create_gsx_repair(req, order_id):
    order = Order.objects(id = ObjectId(order_id)).first()
    customer = {}
    templates = Message.objects.filter(is_template = True)
    comptia = json.load(open("/Users/filipp/Projects/servo3/gsx/symptoms.json"))
  
    if order.customer:
        for k, v in order.customer.properties.items():
            if re.search('@', v):
                customer['emailAddress'] = v
            if re.search('^\d{5}$', v):
                customer['zip'] = v
            if re.search('^\d{6,}$', v):
                customer['primaryPhone'] = v
            if re.search('^\w+\s\d+', v):
                customer['adressLine1'] = v
            if re.search('^[A-Za-z]+$', v):
                customer['city'] = v
  
        (customer['firstName'], customer['lastName']) = order.customer.name.split(" ", 1)
  
    if not "primaryPhone" in customer:
        customer['primaryPhone'] = req.session['user'].location.phone
  
    if not "city" in customer:
        customer['city'] = req.session['user'].location.city
  
    if not "addressLine1" in customer:
        customer['adressLine1'] = req.session['user'].location.address
  
    if not "zip" in customer:
        customer['zip'] = req.session['user'].location.zip
  
    if not "primaryPhone" in customer:
        customer['primaryPhone'] = req.session['user'].location.phone

    if not "emailAddress" in customer:
        customer['emailAddress'] = req.session['user'].location.email

    parts = []
  
    for p in order.products:
        # find the corresponding compnent code from coptia
        try:
            comp = p.product.gsx_data['componentCode']
        except Exception, e:
            # skip products with no GSX data
            continue

    symptoms = comptia['symptoms'][comp]
    parts.append({"number": p.product.number,
        "title": p.product.title, "code": p.product.code, "symptoms": symptoms})
  
    return render(req, "orders/gsx_repair_form.html", {
        "templates": templates,
        "parts": parts,
        "modifiers": comptia['modifiers'],
        "customer": customer,
        "order": order
    })
    
def submit_gsx_repair(req):
    data = DotExpandedDict(req.POST)
    parts = []
  
    order_number = data.get("order_number");
    order = Order.objects(number = int(order_number)).first()

    # create Purchase Order
    po = PurchaseOrder(supplier = "Apple", reference = order_number)
    po.save()
  
    for k, v in data.get("items").items():
        # add to "ordered" inventory
        p = Product.objects(code = v['partNumber']).first()
        Inventory(kind = "po", product = p, slot = po).save()
        Inventory(kind = "order", product = p, slot = order).save()
        parts.append(v)
    
    po.products = parts
    po.carrier = "UPS"
    po.save()
  
    repair = {
        "billTo": "677592",
        "shipTo": "677592",
        "diagnosis": data.get("diagnosis"),
        "notes": data.get("diagnosis"),
        "poNumber": "FL" + order_number,
        "referenceNumber": po.number,
        "requestReviewByApple": data.get("request_review"),
        "serialNumber": data.get("sn"),
        "symptom": data.get("symptom"),
        "unitReceivedDate": data.get("unitReceivedDate"),
        "unitReceivedTime": data.get("unitReceivedTime")
    }
  
    customer = data.get("customerAddress")

    try:
        gsx_repair = submit_repair(repair, customer, parts)
    except Exception, e:
        return HttpResponse(e)

    po.confirmation = gsx_repair['confirmationNumber']
    po.save()
    
    order = Order.objects(number = int(order_number)).first()
    order.gsx_repairs.append(gsx_repair)
    
    return HttpResponse("GSX korjaus luotu")
  
def messages(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/messages.html", {"order": order})
  
def issues(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/issues.html", {"order": order})
  
def devices(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/devices.html", {"order": order})
  
def events(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/events.html", {"order": order})
  
def customer(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/customer.html", {"order": order})

def statuses(req):
    statuses = req.session.get('order').queue.statuses.all()
    return render(req, "orders/statuses.html", {"statuses": statuses})

def products(req, order_id):
    order = Order.objects.get(pk = order_id)
    return render(req, "orders/products.html", {"order": order})