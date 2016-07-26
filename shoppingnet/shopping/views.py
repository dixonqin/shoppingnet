from shopping.forms import GoodsForm, ManageGoodsForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from shopping.models import Goods, Shop, OrderForm, ShoppingCart, Comment
from django.contrib.auth import get_user_model
from django.db import models
# Create your views here.

def ShopList(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/register/')

	if request.user.is_shop == True:
		return HttpResponseRedirect('/shop/' + str(request.user.shop.id))

	queryset = Shop.objects.order_by("id")
	context = {
		'index_shop_List' : queryset,
	}
	return render(request, 'shopping/index.html', context)

def ShopDetail(request, shop_id):
	shop = Shop.objects.get(pk = shop_id)
	context = {
		'shop' : shop,
	}
	return render(request, 'shopping/user_goods_list.html', context)

def ManageShop(request, shop_id):
	shop = Shop.objects.get(pk = shop_id)
	context = {
		'shop' : shop,
	}
	return render(request, 'shopping/shop_goods_list.html', context)

def GoodsDetail(request, goods_id):
	goods = Goods.objects.get(pk = goods_id)
	if request.method == 'POST':
		form = GoodsForm(request.POST)
		if form.is_valid():
			number = form.cleaned_data['number']
			if 'buy' in request.POST:
				of = OrderForm()
				of.user = request.user
				of.goods = goods
				of.number = number
				of.save()
				return HttpResponseRedirect('/order')
			if 'collect' in request.POST:
				sc = ShoppingCart()
				sc.user = request.user
				sc.goods = goods
				sc.number = number
				sc.save()
				return HttpResponseRedirect('/cart')
	else:
		form = GoodsForm()

	context = {
        'goods': goods,
        'form' : form,
    }
	return render(request, 'shopping/goods.html', context)

############################################################################

def ManageGoods(request, goods_id):
	goods = Goods.objects.get(pk = goods_id)
	if request.method == 'POST':
		form = ManageGoodsForm(request.POST, instance = goods)
		if form.is_valid():
			if 'delete' in request.POST:
				shop_id = goods.shop.id
				goods.delete()
				return HttpResponseRedirect('/shop/'+str(shop_id)+'/')
			if 'save' in request.POST:
				form.save()
				form = ManageGoodsForm(instance= goods)
	else:
		form = ManageGoodsForm(instance = goods)

	context = {
        'goods': goods,
        'form' : form,
    }
	return render(request, 'shopping/shop_manage_goods.html', context)

def AddGoods(request):
	return HttpResponseRedirect('/shop/add_goods/')

def UserOrderForm(request):
	context = {
		"user_order" : request.user
	}
	return render(request, "shopping/user_order_list.html", context)

def UserShoppingCart(request):
	context = {
		"user_cart" : request.user
	}
	return render(request, "shopping/user_cart_list.html", context)

def UserShoppingCartDetail(request, cart_id):
	cart = ShoppingCart.objects.get(pk = cart_id)
	if request.method == "POST":
		if 'buy' in request.POST:
			of = OrderForm()
			of.user = request.user
			of.goods = cart.goods
			of.number = cart.number
			of.save()
			return HttpResponseRedirect('/order')
		if 'delete' in request.POST:
			cart.delete()
			return HttpResponseRedirect('/cart')
	context = {
		"cart" : cart
	}

	return render(request, 'shopping/cart.html', context)

def UserOrderFormDetail(request, order_id):
	order = OrderForm.objects.get(pk = order_id)
	if request.method == "POST":
		if 'comment' in request.POST:
			of = OrderForm()
			# of.user = request.user
			# of.goods = cart.goods
			# of.number = cart.number
			# of.save()
			# return HttpResponseRedirect('/order')
		if 'delete' in request.POST:
			order.delete()
			return HttpResponseRedirect('/order')
	context = {
		"order" : order
	}
	return render(request, 'shopping/order.html', context)

# added at 7.25 16:03 




# added at 7.25 16:03 