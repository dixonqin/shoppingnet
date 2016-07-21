from django.conf.urls import url

from . import views
from shopping.views import ShopList

urlpatterns = [
	# ex: /shopping/
    url(r'^$', ShopList.as_view()),
    # ex: /shopping/5/
    url(r'^(?P<shop_id>[0-9]+)/$', views.shop_detail, name='shop_detail'),
    # ex: /shopping/5/goods/
    url(r'^(?P<shop_id>[0-9]+)/goods/(?P<goods_id>[0-9]+)/$', views.shop_goods, name='shop_goods'),
    # ex: /shopping/5/buy/
    url(r'^(?P<shop_id>[0-9]+)/buy/(?P<goods_id>[0-9]+)/$', views.shop_buy, name='shop_buy'),
]

