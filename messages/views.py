from bson.objectid import ObjectId
from django.shortcuts import render
from django.http import HttpResponse

from servo3.models import Message, Template, Order

def index(req):
  messages = Message.objects
  return render(req, 'messages/index.html', {'messages' : messages })
  
def form(req, order_id=None):
  m = Message()
  m.order_id = order_id
  return render(req, 'messages/form.html', {'message' : m, 'templates': Template.objects})
  
def save(req):
  m = Message(created_by = 'filipp')
  m.subject = req.POST['body']
  m.body = req.POST['body']
  m.smsto = req.POST['smsto']
  m.mailto = req.POST['mailto']
  
  if 'order' in req.POST:
    order = Order.objects(id=ObjectId(req.POST['order']))[0]
    m.order = order
  
  m.send_mail()
  m.send_sms()
  
  m.save()
  
  return HttpResponse('Viesti tallennettu')

def remove(req, id=None):
  """docstring for remove_message"""
  if 'id' in req.POST:
    msg = Message.objects(id = ObjectId(req.POST['id']))
    msg.delete()
    return HttpResponse('Viesti poistettu')
  else:
    msg = Message.objects(id = ObjectId(id))[0]
    return render(req, 'messages/remove.html', msg)
    
def view(req, id):
  m = Message.objects(id = ObjectId(id))[0]
  return render(req, 'messages/view.html', m)