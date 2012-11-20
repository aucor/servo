from django.conf.urls import patterns, url

urlpatterns = patterns('products.views',
    url(r'^$', 'index'),
    url(r'^(\d+)/save/$', 'save'),
    url(r'^new/$', 'edit'),
    url(r'^incoming/$', 'index_incoming'),
    url(r'^invoices/$', 'invoices'),
    url(r'^product/remove/$', 'remove'),
    url(r'^group/(?P<group_id>\d+)/$', 'index'),
    url(r'^tag/(?P<tag_id>\d+)/$', 'index'),
    url(r'^spec/(?P<spec_id>\d+)/$', 'index'),
    url(r'^(\d+)/edit/$', 'edit'),
    url(r'^(?P<code>[\w\-/]+)/edit/$', 'edit'),
    url(r'^(\d+)/remove/$', 'remove'),
    url(r'^(?P<product_id>\d+)/order/$', 'create_po'),
    url(r'^index/(\d+)/save/$', 'index'),
    url(r'^(\d+)/view/$', 'view'),
    url(r'^(?P<code>[\w\-/]+)/view/$', 'view'),
    url(r'^po/$', 'index_po'),
    url(r'^po/new/$', 'create_po'),
    url(r'^po/new/$', 'create_po'),
    url(r'^po/(\d+)/$', 'edit_po'),
    url(r'^po/(\d+)/submit/$', 'submit_po'),
    url(r'^po/(\d+)/remove/$', 'remove_po'),
    url(r'^po/(\d+)/order_stock/$', 'order_stock'),
    url(r'^po/order/(?P<order_id>\d+)/$', 'create_po'),
    url(r'^po/(?P<id>\d+)/(?P<action>\w+)/(?P<item_id>\d+)/$', 'edit_po'),
)