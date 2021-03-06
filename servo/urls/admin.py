from django.conf.urls import patterns, url

urlpatterns = patterns('servo.views.admin',
    url(r'^$', 'settings'),
    url(r'^queues/$', 'queues'),
    url(r'^files/$', 'documents'),

    url(r'^statuses/$', 'statuses'),
    url(r'^statuses/(\w+)/$', 'edit_status'),
    url(r'^settings/$', 'settings'),

    url(r'^users/$', 'users'),
    url(r'^users/new/$', 'edit_user'),
    url(r'^users/(\d+)/edit/$', 'edit_user'),
    url(r'^users/(\d+)/save/$', 'save_user'),
    url(r'^users/(\d+)/delete/$', 'remove_user'),

    url(r'^groups/$', 'groups'),
    url(r'^groups/new/$', 'edit_group'),
    url(r'^groups/(\d+)/edit/$', 'edit_group'),

    url(r'^tags/$', 'tags'),
    url(r'^tags/new/$', 'edit_tag'),
    url(r'^tags/(\w+)/save/$', 'edit_tag'),

    url(r'^fields/$', 'fields'),
    url(r'^fields/(?P<field_id>\w+)/save/$', 'edit_field'),
    url(r'^fields/(?P<field_id>\w+)/$', 'edit_field'),
    url(r'^fields/(\d+)/remove/$', 'remove_field'),
    
    url(r'^templates/$', 'templates'),
    url(r'^templates/new/$', 'edit_template'),
    url(r'^template/save/$', 'edit_template'),
    url(r'^templates/(\d+)/edit/$', 'edit_template'),
    url(r'^templates/(\d+)/delete/$', 'remove_template'),

    url(r'^queues/new/$', 'edit_queue'),
    url(r'^queues/(\d+)/edit/$', 'edit_queue'),
    url(r'^queues/(\d+)/remove/$', 'remove_queue'),

    url(r'^gsx/accounts/$', 'gsx_accounts'),
    url(r'^gsx/accounts/(\w+)/$', 'gsx_form'),
    url(r'^gsx/accounts/(\d+)?/delete/$', 'gsx_remove'),
    url(r'^gsx/accounts/(\d+)/save/$', 'gsx_save'),

    url(r'^locations/$', 'locations'),
    url(r'^locations/new/$', 'edit_location'),
    url(r'^locations/(\d+)?/edit/$', 'edit_location'),

    url(r'^notifications/$', 'notifications'),
    url(r'^notifications/(\w+)/$', 'edit_notification'),

)
