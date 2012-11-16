# coding=utf-8

from django import forms
from django.contrib import auth
from django.contrib import messages as msgs
from django.shortcuts import redirect, render
from django.utils.translation import ugettext as _

from accounts.models import UserProfile

from notes.models import Note
from orders.models import Order
from servo.models import Location

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile

def logout(request):
    auth.logout(request)
    msgs.add_message(request, msgs.INFO, _(u'Kirjauduit ulos'))
    return redirect('/accounts/login/')
  
def login(request):
    if 'username' in request.POST:
        user = auth.authenticate(username=request.POST['username'],
            password=request.POST['password'])
        
        if user is not None and user.is_active:
            auth.login(request, user)
            msgs.add_message(request, msgs.INFO, _('Moi, %s!' % user.username))
            return redirect('/orders/index/user/%s/' % user.username)
        else:
            msgs.add_message(request, msgs.INFO,
            	_(u'Väärä käyttäjätunnus tai salasana'))
      
    return render(request, 'accounts/login.html')

def settings(request):
    if request.method == 'POST':
        (profile, created) = UserProfile.objects.get_or_create(user=request.user)
        location_id = request.POST.get('location')
        if location_id:
            loc = Location.objects.get(pk=location_id)
            profile.location = loc

        profile.phone = request.POST.get('phone')
        profile.tech_id = request.POST.get('tech_id')
        profile.locale = request.POST.get('locale')
        profile.save()
        
        if request.POST.get('password'):
            request.user.set_password(request.POST['password'])

        profile.save()
        request.session['user_profile'] = profile

        msgs.add_message(request, msgs.INFO, _(u'Asetukset tallennettu'))
        return redirect('accounts.views.settings')
    else:
        form = ProfileForm(instance=request.session.get('user_profile'))
        return render(request, 'accounts/settings.html', {'form': form})

def home(request):
    data = dict()
    data['orders'] = Order.objects.filter(user=request.user)
    return render(request, 'accounts/home.html', data)

def messages(request, message_id=None, flags='01'):
    messages = Note.objects.filter(recipient=request.user)

    if message_id:
        message = Note.objects.get(pk=message_id)
        return render(request, 'accounts/view_message.html', {
            'msgs': messages, 'msg': message
            })

    return render(request, 'accounts/messages.html', {'msgs': messages})
