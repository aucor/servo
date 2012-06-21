from django.shortcuts import render
from django.http import HttpResponse
from servo.models import Message, Order, Attachment

from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']

def index(req):
    messages = Message.objects.filter(recipient = req.session['user'])
    return render(req, 'messages/index.html', {'messages': messages})

def form(req, replyto = None, smsto = None, mailto = None):
    form = MessageForm()
    print form

    m = Message()

    if replyto:
        parent = Message.objects.get(pk = replyto)
        m = Message(path = parent.path)
    if smsto:
        m.smsto = smsto
    if mailto:
        m.mailto = mailto

    templates = Message.objects.filter(is_template = True)

    return render(req, 'messages/form.html', {'message': m, 'templates': templates})

def edit(req, id = None):
    m = Message.objects.get(pk = id)
    templates = Message.objects.filter(is_template = True)
    return render(req, 'messages/form.html', {'message': m, 'templates': templates})

def save(req):
    m = Message(sender = req.session.get('user'))

    m.body = req.POST.get("body")
    m.smsto = req.POST.get("smsto")
    m.subject = req.POST.get("body")
    m.mailto = req.POST.get("mailto")
    
    for a in req.POST.getlist('attachments'):
        doc = Attachment.objects.get(pk = id)
        m.attachments.append(doc)
    
    if "order" in req.session:
        m.order = req.session['order']
        m.recipient = req.session['order'].user
    
    if m.mailto:
        m.send_mail()
    
    if m.smsto:
        m.send_sms()
    
    m.save()
    m.path = req.POST.get('path', str(m.id))
    m.save()

    return HttpResponse('Viesti tallennettu')

def remove(req, id = None):
    if 'id' in req.POST:
        msg = Message.objects.get(pk = req.POST['id'])
        msg.delete()
        return HttpResponse('Viesti poistettu')
    else:
        msg = Message.objects.get(pk = id)
    
    return render(req, 'messages/remove.html', {'message': msg})
    
def view(req, id):
    msg = Message.objects.get(pk = id)
    return render(req, 'messages/view.html', {'message': msg})