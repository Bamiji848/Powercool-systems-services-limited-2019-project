from django.conf.urls import url
from . import views

app_name = 'powercool_app'

urlpatterns = [
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^shop/(?P<category_slug>[-\w]+)/$', views.shop, name='product_list_by_category'),
    url(r'^shop_single(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.shop_single, name='shop_single'),
]


