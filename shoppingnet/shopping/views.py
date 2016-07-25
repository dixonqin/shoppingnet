from shopping.forms import GoodsForm
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from shopping.models import Goods, Shop, OrderForm, ShoppingCart, Comment
from django.contrib.auth import get_user_model
# Create your views here.

def ShopList(request):
	queryset = Shop.objects.order_by("id")
	if request.method == "POST":
		if request.POST.get("submit") == "cart":
			return render(request, 'user'+request.user.id+'/cart/')
		if request.POST.get("submit") == "order":
			return render(request, 'user'+request.user.id+'/order/')

	context = {
		'index_shop_List' : queryset,
	}
	return render(request, 'shopping/index.html', context)

def toUserOrder(request):
	model = get_user_model()
	context_object_name = "user_order"
	template_name = "shopping/user_order.html"

	def get_context_data(self, **kwargs):
		context = super(UserOrderForm, self).get_context_data(**kwargs)
		return context

class ShopDetail(DetailView):
	model = Shop
	context_object_name = "shop_goods_list"
	template_name = "shopping/shop.html"

	def get_context_data(self, **kwargs):
		context = super(ShopDetail, self).get_context_data(**kwargs)
		return context

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

def UserOrderForm(request):
	context = {
		"user_order" : request.user
	}

	return render(request, "shopping/user_order.html", context)

def UserShoppingCart(request):
	context = {
		"user_cart" : request.user
	}

	return render(request, "shopping/user_cart.html", context)

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
