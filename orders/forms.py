#coding=utf-8

from lib.gsxlib import gsxlib
from django import forms
from orders.models import *
from servo.models import QueueStatus
from products.forms import LocalizedModelForm
from django.utils.translation import ugettext as _
from countries.models import Country

class InvoiceForm(LocalizedModelForm):
    class Meta:
        model = Invoice
        exclude = ('created_at', 'paid_at', 'created_by',
        'customer', 'order', 'total_margin',)

class SidebarForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('user', 'queue', 'status', 'priority',)

class FieldsForm(forms.Form):
    pass

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = ServiceOrderItem
        fields = ('title', 'sn', 'amount', 'price_category',
            'price', 'should_report', 'should_return', )
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'input-mini'}),
            'price': forms.TextInput(attrs={'class': 'input-mini'})
        }

class GsxPartForm(forms.Form):
    partNumber = forms.CharField(max_length=18, widget=forms.TextInput(
        attrs={'class': 'input-small'}))
    comptiaCode = forms.CharField(max_length=3)
    abused = forms.CharField(max_length=1)
    comptiaModifier = forms.CharField(max_length=1)

class GsxCustomerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        customer = kwargs['customer']
        profile = kwargs['profile']

        del(kwargs['customer'], kwargs['profile'])

        super(GsxCustomerForm, self).__init__(*args, **kwargs)

        if customer['primaryPhone'] == '':
            customer['primaryPhone'] = profile.location.phone
        if customer['city'] == '':
            customer['city'] = profile.location.city
        if customer['addressLine1'] == '':
            customer['addressLine1'] = profile.location.address
        if customer['zipCode'] == '':
            customer['zipCode'] = profile.location.zip_code
        if customer['emailAddress'] == '':
            customer['emailAddress'] = profile.location.email

        self.fields['firstName'] = forms.CharField(max_length=100, 
            label=_(u'Etunimi'),
            initial=customer['firstName'])
        self.fields['lastName'] = forms.CharField(max_length=100, 
            label=_(u'Sukunimi'),
            initial=customer['lastName'])
        self.fields['emailAddress'] = forms.CharField(max_length=100, 
            label=_(u'Sähköposti'),
            initial=customer['emailAddress'])
        self.fields['primaryPhone'] = forms.CharField(max_length=100, 
            label=_(u'Puhelin'),
            initial=customer['primaryPhone'])
        self.fields['addressLine1'] = forms.CharField(max_length=100, 
            label=_(u'Osoite'),
            initial=customer['addressLine1'])
        self.fields['zipCode'] = forms.CharField(max_length=8, 
            label=_(u'Postinumero'),
            initial=customer['zipCode'])
        self.fields['city'] = forms.CharField(max_length=32, 
            label=_(u'Toimipaikka'),
            initial=customer['city'])
        self.fields['country'] = forms.ModelChoiceField(
            label=_(u'Maa'),
            queryset=Country.objects.all())

class GsxRepairForm(forms.Form):
    def __init__(self, *args, **kwargs):
        order = kwargs['order']
        del(kwargs['order'])
        super(GsxRepairForm, self).__init__(*args, **kwargs)
        
        langs = gsxlib.langs('en_XXX')
        symptom_text = order.issues()[0].body

        try:
            diagnosis_text = order.issues()[0].replies.all()[0].body
        except IndexError:
            diagnosis_text = ''
        
        self.fields['device'] = forms.ModelChoiceField(queryset=order.devices.all(), 
            label=_(u'Laite'))

        self.fields['symptom'] = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'input-xxlarge copy-source template', 'rows': 6}),
            initial=symptom_text,
            label=_(u'Vikakuvaus'))

        self.fields['diagnosis'] = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'input-xxlarge copy-target template', 'rows': 6}), 
            initial=diagnosis_text,
            label=_(u'Diagnoosi'))

        self.fields['notes'] = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'input-xxlarge', 'rows': 6}), label=_(u'Merkinnät'),
            required=False)

        self.fields['unitReceivedDate'] = forms.DateField(
            initial=order.created_at,
            widget=forms.DateInput(format=langs['df'],
                attrs={'class': 'input-small'}),
            input_formats=[langs['df']],
            label=_(u'Päivämäärä'))

        self.fields['unitReceivedTime'] = forms.TimeField(initial=order.created_at,
            widget=forms.TimeInput(format=langs["tf"], 
                attrs={'class': 'input-small'}),
            input_formats=[langs["tf"]],
            label=_(u'Aika'))

        self.fields['fileData'] = forms.FileField(required=False, 
            label=_(u'Liite'))
