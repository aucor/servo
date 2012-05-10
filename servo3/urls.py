from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext as _

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  
  url(r'^$', 'orders.views.index'),
  url(r'^document/save$', 'documents.views.save'),
  url(r'^document/view/(\w+)$', 'documents.views.view'),
  url(r'^document/remove/(\w+)$', 'documents.views.remove'),
  url(r'^document/remove$', 'documents.views.remove'),
  url(r'^files/create$', 'documents.views.create'),
  url(r'^user/save$', 'admin.views.save_user'),
  url(r'^user/edit/(\w+)$', 'admin.views.edit_user'),
   
  url(r'^customer/index$', 'customers.views.index'),
  url(r'^customer/edit/(\w+)$', 'customers.views.edit'),
  
  url(r'^search/lookup\-(.+)$', 'search.views.lookup'),
  
  url(r'^device/search$', 'devices.views.search'),
  url(r'^device/index$', 'devices.views.index'),
  url(r'^device/create$', 'devices.views.create'),
  url(r'^device/edit/(\w+)$', 'devices.views.edit'),
  url(r'^device/remove$', 'devices.views.remove'),
  url(r'^device/remove/(\w+)$', 'devices.views.remove'),
  url(r'^device/save$', 'devices.views.save'),
  url(r'^device/create/order/(\w+)$', 'devices.views.create'),
  
  url(r'^customer/create$', 'customers.views.create'),
  url(r'^customer/create/(\w+)$', 'customers.views.create'),
  url(r'^customer/create/order/(?P<order>\w+)$', 'customers.views.create'),
    
  url(r'^customer/search$', 'customers.views.search'),
  url(r'^customer/remove$', 'customers.views.remove'),
  url(r'^customer/remove/(\w+)$', 'customers.views.remove'),
  url(r'^customer/save$', 'customers.views.save'),
  url(r'^customer/view/(\w+)$', 'customers.views.view'),
  url(r'^customer/move$', 'customers.views.move'),
  url(r'^customer/move/(\w+)$', 'customers.views.move'),
    
  url(r'^orders/$', 'orders.views.index'),
  url(r'^orders/index/(\w+)/(\w+)/$', 'orders.views.index'),
  
  url(r'^orders/edit/(\w+)$', 'orders.views.edit'),
  url(r'^orders/remove/(\w+)$', 'orders.views.remove'),
  url(r'^orders/remove$', 'orders.views.remove'),
  url(r'^orders/create$', 'orders.views.create'),
  url(r'^orders/follow/(\w+)$', 'orders.views.follow'),
  url(r'^orders/tags/(\w+)$', 'orders.views.tags'),
  url(r'^orders/update/(\w+)$', 'orders.views.update'),
  
  url(r'^message/$', 'messages.views.index'),
  url(r'^message/save$', 'messages.views.save'),
  url(r'^message/view/(\w+)$', 'messages.views.view'),
  url(r'^message/remove$', 'messages.views.remove'),
  url(r'^message/remove/(\w+)$', 'messages.views.remove'),
  url(r'^message/create/order/(\w+)$', 'messages.views.form'),
  url(r'^message/edit/(\w+)$', 'messages.views.edit'),
  
  url(r'^admin/files$', 'documents.views.index'),
  url(r'^admin/status/$', 'admin.views.status'),
  url(r'^status/save$', 'admin.views.save_status'),
  url(r'^status/edit/(\w+)$', 'admin.views.status_form'),
  url(r'^admin/queues/$', 'queues.views.index'),
  url(r'^admin/status/create$', 'admin.views.status_form'),
  url(r'^admin/fields/$', 'admin.views.fields'),
  url(r'^admin/fields/edit/$', 'admin.views.edit_field'),
  url(r'^admin/settings$', 'admin.views.settings'),
  url(r'^admin/users$', 'admin.views.users'),
  url(r'^admin/user/create$', 'admin.views.edit_user'),
  url(r'^admin/locations$', 'admin.views.locations'),
  url(r'^admin/location/create$', 'admin.views.edit_location'),
    
  url(r'^fields/edit/(\w+)$', 'admin.views.edit_field'),
  url(r'^fields/remove/$', 'admin.views.remove_field'),
  url(r'^fields/remove/(\w+)$', 'admin.views.remove_field'),
  url(r'^admin/fields/save/$', 'admin.views.save_field'),
  url(r'^admin/templates/$', 'admin.views.templates'),
  url(r'^template/create$', 'admin.views.create_template'),
  url(r'^template/save$', 'admin.views.save_template'),
  url(r'^template/view/(\w+)$', 'admin.views.view_template'),
    
  url(r'^gsx/accounts$', 'admin.views.gsx_accounts'),
  url(r'^gsx/create_account$', 'admin.views.gsx_form'),
  url(r'^gsx/edit/(\w+)$', 'admin.views.gsx_form'),
  url(r'^gsx/remove_account$', 'admin.views.gsx_remove'),
  url(r'^gsx/save_account$', 'admin.views.gsx_save'),
    
  url(r'^queue/create$', 'queues.views.edit'),
  url(r'^queue/save$', 'queues.views.save'),
  url(r'^queue/edit/(\w+)$', 'queues.views.edit'),
  url(r'^queue/remove$', 'queues.views.remove'),
  url(r'^queue/remove/(\w+)$', 'queues.views.remove'),
    
  url(r'^products/create/order/(\w+)$', 'products.views.create'),
  url(r'^products/create$', 'products.views.create'),
  url(r'^products/index$', 'products.views.index'),
  url(r'^products/save$', 'products.views.save'),
  url(r'^products/search$', 'products.views.search'),
  url(r'^products/remove$', 'products.views.remove'),
  url(r'^products/remove/(\w+)$', 'products.views.remove'),
  url(r'^products/edit/([\w\-]+)$', 'products.views.edit'),
  
  url(r'^issue/create/order/(\w+)$', 'issues.views.create'),
  url(r'^issue/edit/(\w+)$', 'issues.views.edit'),
  url(r'^issue/save$', 'issues.views.save'),
  url(r'^issue/remove$', 'issues.views.remove'),
  url(r'^issue/remove/(\w+)$', 'issues.views.remove'),
    
  url(r'^tag/create/(\w+)$', 'tags.views.create'),
  url(r'^tag/index$', 'tags.views.index'),
  url(r'^tag/index/type/(\w+)$', 'tags.views.index'),
  
  url(r'^location/save$', 'admin.views.save_location'),
  
  url(r'^user/login$', 'users.views.login'),
  url(r'^user/logout$', 'users.views.logout'),
  url(r'^user/settings$', 'users.views.settings'),
  # url(r'^servo3/', include('servo3.foo.urls')),
)
