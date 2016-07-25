from django.conf.urls import url
from shopping.views import ShopList, ShopDetail, GoodsDetail, UserOrderForm, UserShoppingCart
from shopping import views

urlpatterns = [
	# 商店列表，购物网站的首页
	# ex: /shopping/
    url(r'^$', views.ShopList, name = "index"),
    # 某个商店，主要内容为商品列表
    # ex: /shopping/5/
    url(r'^(?P<pk>[0-9]+)/$', ShopDetail.as_view()),
    # 某个商品的详细信息
    # ex: shopping/goods/2
    url(r'^goods/(?P<goods_id>[0-9]+)/$', views.GoodsDetail),
    # 显示用户历史记录的页面, 里面可以评分...
    # ex: /user/5/order
    url(r'^order/$', views.UserOrderForm),
    # 显示用户购物车的页面
    # ex: /user/5/cart
    url(r'^cart/$', views.UserShoppingCart),

    url(r'^order/(?P<order_id>[0-9]+)/$', views.UserOrderFormDetail),

    url(r'^cart/(?P<cart_id>[0-9]+)/$', views.UserShoppingCartDetail),

    
]

