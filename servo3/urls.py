from django.conf.urls import patterns, include, url
from django.utils.translation import ugettext as _

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('servo',
    url(r'^$', 'views.orders.index'),
    url(r'^document/save$', 'views.documents.save'),
    url(r'^document/edit/(\w+)$', 'views.documents.edit'),
    url(r'^document/view/(\w+)$', 'views.documents.view'),
    url(r'^document/remove/(\w+)$', 'views.documents.remove'),
    url(r'^document/remove$', 'views.documents.remove'),
    url(r'^document/(\w+)/print/([a-z]+)/(\w+)$', 'views.documents.output'),
    url(r'^document/barcode/(\w+)$', 'views.documents.barcode'),

    url(r'^files/create$', 'views.documents.create'),
    url(r'^user/save$', 'views.admin.save_user'),
    url(r'^user/edit/(\w+)$', 'views.admin.edit_user'),
    
    url(r'^search/lookup\-(.+)$', 'views.search.lookup'),
    
    url(r'^device/search$', 'views.devices.search'),
    url(r'^device/(\w+)/$', 'views.devices.edit'),
    url(r'^device/index$', 'views.devices.index'),
    url(r'^device/create$', 'views.devices.create'),
    url(r'^device/remove$', 'views.devices.remove'),
    url(r'^device/remove/(\w+)$', 'views.devices.remove'),
    url(r'^device/save$', 'views.devices.save'),
    url(r'^device/create/order/(\w+)$', 'views.devices.create'),
    
    url(r'^customer/index$', 'views.customers.index'),
    url(r'^customer/edit/(\w+)$', 'views.customers.edit'),
    url(r'^customer/create$', 'views.customers.create'),
    url(r'^customer/create/(\w+)$', 'views.customers.create'),
    url(r'^customer/search$', 'views.customers.search'),
    url(r'^customer/remove$', 'views.customers.remove'),
    url(r'^customer/remove/(\w+)$', 'views.customers.remove'),
    url(r'^customer/save$', 'views.customers.save'),
    url(r'^customer/view/(\w+)$', 'views.customers.view'),
    url(r'^customer/move$', 'views.customers.move'),
    url(r'^customer/move/(\w+)$', 'views.customers.move'),
    url(r'^customer/create/order/(?P<order>\w+)$', 'views.customers.create'),
      
    url(r'^orders/$', 'views.orders.index'),
    url(r'^orders/index/(?P<param>\w+)/(?P<value>[\w\-]+)/$', 'views.orders.index'),
    
    url(r'^orders/(\d+)/$', 'views.orders.edit'),
    url(r'^orders/search$', 'views.orders.search'),
    url(r'^orders/remove/(\w+)$', 'views.orders.remove'),
    url(r'^orders/statuses$', 'views.orders.statuses'),
    url(r'^orders/remove$', 'views.orders.remove'),
    url(r'^orders/create$', 'views.orders.create'),
    url(r'^orders/follow/(\w+)$', 'views.orders.follow'),
    url(r'^orders/(\d+)/messages/$', 'views.orders.messages'),
    url(r'^orders/(\d+)/events/$', 'views.orders.events'),
    url(r'^orders/(\d+)/issues/$', 'views.orders.issues'),
    url(r'^orders/(\d+)/devices$', 'views.orders.devices'),
    url(r'^orders/(\d+)/products/$', 'views.orders.products'),
    url(r'^orders/customer/(\w+)$', 'views.orders.customer'),
    url(r'^orders/tags/(\w+)$', 'views.orders.tags'),
    url(r'^orders/update/(\w+)$', 'views.orders.update'),
    url(r'^orders/gsx_repair/(\w+)$', 'views.orders.create_gsx_repair'),
    url(r'^orders/submit_gsx_repair$', 'views.orders.submit_gsx_repair'),
    url(r'^orders/(?P<order_id>\d+)/print/?(?P<kind>\w+)?/(?P<template_id>\d+)$',
        'views.orders.put_on_paper'),
    
    url(r'^message/$', 'views.messages.index'),
    url(r'^message/save$', 'views.messages.save'),
    url(r'^message/view/(\w+)$', 'views.messages.view'),
    url(r'^message/remove$', 'views.messages.remove'),
    url(r'^message/remove/(\w+)$', 'views.messages.remove'),
    url(r'^message/create$', 'views.messages.form'),
    url(r'^message/edit/(\w+)$', 'views.messages.edit'),
    url(r'^message/(?P<replyto>\d+)/reply/$', 'views.messages.form'),
    url(r'^message/smsto/(?P<smsto>\w+)$', 'views.messages.form'),
    url(r'^message/mailto/(?P<mailto>.+)$', 'views.messages.form'),

    url(r'^admin/files$', 'views.documents.index'),
    url(r'^admin/status/$', 'views.admin.status'),
    url(r'^status/save$', 'views.admin.save_status'),
    url(r'^status/edit/(\w+)$', 'views.admin.status_form'),
    url(r'^admin/queues/$', 'views.queues.index'),
    url(r'^admin/status/create$', 'views.admin.status_form'),
    url(r'^admin/fields/$', 'views.admin.fields'),
    url(r'^admin/fields/edit/$', 'views.admin.edit_field'),
    url(r'^admin/settings$', 'views.admin.settings'),
    url(r'^admin/users$', 'views.admin.users'),
    url(r'^admin/user/create$', 'views.admin.edit_user'),
    url(r'^admin/locations$', 'views.admin.locations'),
    url(r'^admin/location/create$', 'views.admin.edit_location'),
    url(r'^location/edit/(\w+)$', 'views.admin.edit_location'),
    url(r'^admin/tags/$', 'views.admin.tags'),
      
    url(r'^fields/edit/(\w+)$', 'views.admin.edit_field'),
    url(r'^fields/remove/$', 'views.admin.remove_field'),
    url(r'^fields/remove/(\w+)$', 'views.admin.remove_field'),
    url(r'^admin/fields/save/$', 'views.admin.save_field'),
    url(r'^admin/templates/$', 'views.admin.templates'),
    url(r'^template/create$', 'views.admin.create_template'),
    url(r'^template/save$', 'views.admin.save_template'),
    url(r'^template/view/(\w+)$', 'views.admin.view_template'),
      
    url(r'^gsx/accounts$', 'views.admin.gsx_accounts'),
    url(r'^gsx/create_account$', 'views.admin.gsx_form'),
    url(r'^gsx/edit/(\w+)$', 'views.admin.gsx_form'),
    url(r'^gsx/remove_account$', 'views.admin.gsx_remove'),
    url(r'^gsx/save_account$', 'views.admin.gsx_save'),
      
    url(r'^queue/create$', 'views.queues.edit'),
    url(r'^queue/save$', 'views.queues.save'),
    url(r'^queue/edit/(\w+)$', 'views.queues.edit'),
    url(r'^queue/remove$', 'views.queues.remove'),
    url(r'^queue/remove/(\w+)$', 'views.queues.remove'),
    
    url(r'^products/([\w\-]+)/$', 'views.products.edit'),
    url(r'^products/([\w\-]+)/save/$', 'views.products.save'),
    url(r'^products/create/order/(\d+)/$', 'views.products.create'),
    url(r'^products/create$', 'views.products.create'),
    url(r'^products/index$', 'views.products.index'),
    url(r'^products/search$', 'views.products.search'),
    url(r'^products/remove$', 'views.products.remove'),
    url(r'^products/(\d+)/remove/$', 'views.products.remove'),
    url(r'^products/remove/order/(?P<order_item_id>\d+)$', 'views.products.remove'),
    url(r'^products/reserve/([\w\-]+)$', 'views.products.reserve'),
    url(r'^products/reserve', 'views.products.reserve'),
    
    url(r'^issue/create/order/(?P<order_id>\d+)/$', 'views.issues.edit'),
    url(r'^issue/(?P<id>\d+)?/edit/$', 'views.issues.edit'),
    url(r'^issue/(?P<id>\d+)/remove/$', 'views.issues.remove'),
    url(r'^issue/(?P<id>\d+)/(?P<kind>\w+)/$', 'views.issues.edit'),

    url(r'^tag/create/(\w+)$', 'views.tags.create'),
    url(r'^tag/save/(\w+)$', 'views.tags.save'),
    url(r'^tag/index/(\w+)$', 'views.tags.index'),
    
    url(r'^location/save$', 'views.admin.save_location'),
    
    url(r'^user/login$', 'views.users.login'),
    url(r'^user/logout$', 'views.users.logout'),
    url(r'^user/settings$', 'views.users.settings'),
    
    url(r'^store/order_products/([\d;]+)$', 'views.store.order_products'),
    url(r'^store/sell_products/(?P<numbers>[\d;]+)$', 'views.store.dispatch'),
    url(r'^store/save_po$', 'views.store.save_po'),
    url(r'^store/po/index$', 'views.store.index_po'),
    url(r'^store/po/incoming$', 'views.store.index_incoming'),
    url(r'^store/dispatch/order/(?P<order_id>\w+)$', 'views.store.dispatch'),
    url(r'^store/dispatch$', 'views.store.dispatch'),
    url(r'^store/invoices$', 'views.store.invoices'),
    url(r'^calendars/$', 'views.calendars.index'),
    url(r'^calendars/save$', 'views.calendars.save'),
    url(r'^calendar/save_event$', 'views.calendars.save_event'),
    url(r'^calendar/create$', 'views.calendars.create'),
    url(r'^calendar/edit/(\w+)$', 'views.calendars.edit'),
    url(r'^calendar/remove$', 'views.calendars.remove'),
    url(r'^calendar/remove/(\w+)$', 'views.calendars.remove'),
    url(r'^calendar/events/(\w+)$', 'views.calendars.events'),
    url(r'^calendar/(\w+)/create_event$', 'views.calendars.event'),

    url(r'^article/$', 'views.articles.index'),
    url(r'^article/index$', 'views.articles.index'),
    url(r'^article/view/(\w+)$', 'views.articles.view'),
    url(r'^article/edit/(\w+)$', 'views.articles.edit'),
    url(r'^article/save$', 'views.articles.save'),
    url(r'^article/remove/(\w+)$', 'views.articles.remove'),
    url(r'^article/remove$', 'views.articles.remove'),

    url(r'^search/save$', 'views.search.save'),
    url(r'^specs/index$', 'views.specs.index'),
    # url(r'^servo3/', include('servo3.foo.urls')),
)
