from django.conf.urls import url
from shopping.views import HomePage, ShopDetail, GoodsDetail, UserOrder, UserShoppingCart, ShopDetail, ManageShop, ManageGoods, AddGoods
from shopping.views import CompleteUserInfo, CompleteShopInfo, ShopOrder, ShopOrderFormDetail
from shopping.views import InfoView
from shopping import views

urlpatterns = [
	# 商店列表，购物网站的首页
	# ex: /shopping/
    url(r'^$', views.HomePage, name = "index"),
    # 某个商店，主要内容为购物进入某店时，商品列表
    # ex: /shopping/5/
    url(r'^(?P<shop_id>[0-9]+)/$', views.ShopDetail),
    #
    #完善商店信息
    url(r'^shop_info/$', views.CompleteShopInfo),
    #
    #完善商品信息
    url(r'^user_info/$', views.CompleteUserInfo),
    #
    # 某个商店，主要为店主直接修改某些商品信息
    url(r'^shop/(?P<shop_id>[0-9]+)/$', views.ManageShop),
    # 某个商品的详细信息
    # ex: shopping/goods/2
    url(r'^goods/(?P<goods_id>[0-9]+)/$', views.GoodsDetail),
    #
    #
    url(r'^shop/goods/(?P<goods_id>[0-9]+)/$', views.ManageGoods),
    # 
    # 
    url(r'^shop/add_goods/$', views.AddGoods),
    # 显示用户历史记录的页面, 里面可以评分...
    # ex: /user/5/order
    url(r'^user_order/$', views.UserOrder),

    url(r'^user_order/(?P<order_id>[0-9]+)/$', views.UserOrderFormDetail),
    # 显示用户购物车的页面
    # ex: /user/5/cart
    url(r'^cart/$', views.UserShoppingCart),

    url(r'^cart/(?P<order_id>[0-9]+)/$', views.UserShoppingCartDetail),

    url(r'^shop_order/$', views.ShopOrder),

    url(r'^shop_order/(?P<order_id>[0-9]+)/$', views.ShopOrderFormDetail),

    url(r'^info_view/$', views.InfoView, name = "info_view"),
]

