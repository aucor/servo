from mongoengine import *
from datetime import datetime
from bson.objectid import ObjectId

connect('servo')

class Tag(Document):
  title = StringField(required=True, default='Uusi tagi')
  type = StringField(required=True)
  
class Config(Document):
  mail_from = EmailField(default = 'servo@example.com')
  imap_host = StringField()
  imap_user = StringField()
  imap_password = StringField()
  imap_ssl = BooleanField(default=True)
  smtp_host = StringField()
  
  sms_url = StringField()
  sms_user = StringField()
  sms_password = StringField()
  
class Field(Document):
  title = StringField(required=True)
  type = StringField(required=True)
  format = StringField()
  
class Location(Document):
  title = StringField(required=True)
  description = StringField()
  phone = StringField()
  email = EmailField()
  address = StringField()
  
class GsxAccount(Document):
  title = StringField(default="Uusi tili")
  sold_to = StringField()
  ship_to = StringField()
  username = StringField()
  password = StringField()
  environment = StringField()
  is_default = BooleanField(default=True)

class Queue(Document):
  title = StringField(default = "Uusi jono")
  description = StringField()
  gsx_account = ReferenceField(GsxAccount)
  
class Customer(Document):
  meta = { 'ordering': ['path', '-id'] }
  number = SequenceField()
  name = StringField(required=True, default="Uusi asiakas")
  """
  path is a comma-separated list of Customer ids with the last one always being the
  current customer
  """
  path = StringField()
  properties = DictField()

  def get_indent(self):
    """docstring for get_indent"""
    return self.path.count(',')+1

  def fullname(self):
    """
    Get the entire info tree for this customer, upwards
    """
    title = []

    for c in self.path.split(','):
      customer = Customer.objects(id = ObjectId(c))[0]
      title.append(customer.name)

    title.reverse()

    return str(', ').join(title)

  def fullprops(self):
    """
    Get the combined view of all the properties for this customer
    """
    props = {}
    for c in self.path.split(','):
      parent = Customer.objects(id = ObjectId(c))[0]
      for key, value in parent.properties.items():
        props[key] = value

    return props
  
class Order(Document):
  number = SequenceField()
  priority = IntField()
  created_at = DateTimeField(default=datetime.now())
  closed_at = DateTimeField()
  followers = ListField()
  customer = ReferenceField(Customer)
  tags = ListField()
  
  def issues(self):
    return Issue.objects(order = self)
    
  def messages(self):
    return Message.objects(order = self)
    
  def status(self):
    return "Ei statusta"
  
  def status_img(self):
    return 'undefined'
  
  def device(self):
    return "Ei laitetta"
  
  def customer_name(self):
    return 'Filipp Lepalaan'
  
  def customer_id(self):
    return 1
  
  def device_name(self):
    return 'Mac mini (Early 2009)'
  
  def device_spec(self):
    return 1
  
  def events(self):
    """docstring for events"""
    return Event.objects(ref_order = self)

class User(Document):
  email = StringField(max_length=128, required=True)
  username = StringField(max_length=64, required=True)
  fullname = StringField(max_length=128, required=True)
  password = StringField(max_length=64, required=True)
  role = StringField(max_length=64, required=True)
  location = ReferenceField(Location)

class Issue(Document):
  symptom = StringField(required=True)
  diagnosis = StringField()
  solution = StringField()
  
  diagnosed_at = DateTimeField()
  diagnosed_by = ReferenceField(User)
  
  solved_at = DateTimeField()
  solved_by = ReferenceField(User)
  
  created_at = DateTimeField(default=datetime.now())
  created_by = StringField(default='filipp')
  
  order = ReferenceField(Order)
  
class Message(Document):
  subject = StringField()
  body = StringField()
  sender = StringField(default='filipp')
  created_at = DateTimeField(default=datetime.now())
  mailto = StringField()
  smsto = StringField()
  order = ReferenceField(Order)
  path = StringField()
  
  def attachments(self):
    pass
    
  def indent(self):
    return 1
    
  def send_mail(self):
    conf = Config.objects[0]
    import smtplib
    server = smtplib.SMTP(conf.smtp_host)
    server.sendmail(conf.mail_from, self.mailto, self.body)
    server.quit()
    
  def send_sms(self):
    conf = Config.objects[0]
    import urllib
    params = urllib.urlencode({'username' : conf.sms_user, 'password' : conf.sms_password, 'text' : self.body, 'to' : self.smsto})
    f = urllib.urlopen("%s?%s" %(conf.sms_url, params))
    print f.read()
    
class Status(Document):
  title = StringField(default="Uusi status")
  description = StringField()

class Product(Document):
  number = SequenceField()
  code = StringField()
  title = StringField(required=True)
  brand = StringField()
  tags = ListField(StringField(max_length=30))
  
  price_purchase = DecimalField()
  price_sales = DecimalField()
  price_exchange = DecimalField()
  
  amount_stocked = IntField(default=0)
  amount_ordered = IntField(default=0)
  amount_reserved = IntField(default=0)

class Template(Document):
  title = StringField(required=True)
  body = StringField(required=True)
  
class Calendar(Document):
  title = StringField(required=True)
  username = StringField()
  events = DictField()

class Invoice(Document):
  number = SequenceField()
  created_at = DateTimeField(default=datetime.now())
  paid_at = DateTimeField()
  items = DictField()
  total = DecimalField()
  
class Event(Document):
  description = StringField()
  created_by = StringField(default='filipp')
  created_at = DateTimeField(default=datetime.now())
  handled_at = DateTimeField()
  ref_order = ReferenceField(Order)
  type = StringField()
  