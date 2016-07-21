#from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from shopping.models import Goods, Shop, User
# Create your views here.

class ShopList(ListView):
	model = Shop
	queryset = Shop.objects.order_by("id")
	context_object_name = "index_shop_List"
	template_name = "shopping/index.html"

def shop_detail(request, shop_id):
	return HttpResponse(" list all goods of a shop ")

def shop_goods(request, shop_id, goods_id):
	return HttpResponse(" list the attr of a shop ")

def shop_buy(request, shop_id, goods_id):
	return HttpResponse(" click and buy ")