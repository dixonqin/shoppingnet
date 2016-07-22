from shopping.forms import GoodsForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from shopping.models import Goods, Shop, User, OrderForm, ShoppingCart, Comment
# Create your views here.

class ShopList(ListView):
	model = Shop
	queryset = Shop.objects.order_by("id")
	context_object_name = "index_shop_List"
	template_name = "shopping/index.html"

class ShopDetail(DetailView):
	model = Shop
	context_object_name = "shop_goods_list"
	template_name = "shopping/shop.html"

	def get_context_data(self, **kwargs):
		context = super(ShopDetail, self).get_context_data(**kwargs)
		return context

def GoodsDetail(request, goods_id):
	goods = Goods.objects.get(pk = goods_id)
	params = request.POST if request.method == 'POST' else None
	form = GoodsForm(params)
	if form.is_valid():
		post = form.save(commit=False)
		post.user = request.user
		post.goods = goods
		post.save()
		form = PostForm()
	context = {
        'goods': goods,
        'form' : form,
    }
	return render(request, 'shopping/goods.html', context)

class UserOrderForm(DetailView):
	model = User
	context_object_name = "user_order"
	template_name = "shopping/user_order.html"

	def get_context_data(self, **kwargs):
		context = super(UserOrderForm, self).get_context_data(**kwargs)
		return context

class UserShoppingCart(DetailView):
	model = User
	context_object_name = "user_cart"
	template_name = "shopping/user_cart.html"

	def get_context_data(self, **kwargs):
		context = super(UserShoppingCart, self).get_context_data(**kwargs)
		return context

def UserShoppingCartDetail(request, cart_id):
	cart = ShoppingCart.objects.get(pk = cart_id)
	if request.method == "POST":
		if(request.POST.has_key("delete")):
			user_id = cart.user.id
			cart.delete()
			return render(request, 'shopping/user'+user_id+'/cart/')####
		if(request.POST.has_key("buy")):
			order = OrderForm()
			order.number = cart.number
			order.user = cart.user
			order.goods = cart.user
			order.save()
			return render(request, 'shopping/user'+order.user.id+'/order/')####
	context = {
		"cart" : cart
	}

	return render(request, 'shopping/cart.html', context)


# def OrderFormDetail(request, order_id):
# 	order = OrderForm.objects.get(pk = order_id)
# 	params = request.POST if request.method == 'POST' else None
# 	if params.has_key("delete"):

# 	if params.has_key("comment"):

# 	context = {
#         'goods': goods,
#         'form' : form,
#     }
# 	return render(request, 'shopping/goods.html', context)