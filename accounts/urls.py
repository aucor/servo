from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
	url(r'^login/$', 'login'),
	url(r'^logout/$', 'logout'),
	url(r'^messages/$', 'messages'),
    url(r'^messages/(\d+)/$', 'messages'),
    url(r'^messages/unread/$', 'messages', {'flags': '01'}),
    url(r'^messages/sent/$', 'messages', {'flags': '01'}),
    url(r'^settings/$', 'settings'),
)
