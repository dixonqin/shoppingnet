from shopping.forms import GoodsForm, ManageGoodsForm, ShopInfoForm, CustomerForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from shopping.models import Goods, Shop, OrderForm, ShoppingCart, Comment, Customer


def HomePage(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/register/')

	if request.user.is_complete == False and request.user.is_shop == True:
		return HttpResponseRedirect('/shop_info/')

	if request.user.is_complete == False and request.user.is_shop == False:
		return HttpResponseRedirect('/user_info/')

	if request.user.is_shop == True:
		return HttpResponseRedirect('/shop/' + str(request.user.shop.id))

	index_shop_List = Shop.objects.order_by("id")
	context = {
		'index_shop_List' : index_shop_List,
	}
	return render(request, 'shopping/index.html', context)

def CompleteUserInfo(request):
	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES)
		if form.is_valid():
			if 'submit' in request.POST:
				t = Customer()
				t = form.save(commit=False)
				request.user.is_complete = True
				t.user = request.user
				t.save()
				request.user.save()
				return HttpResponseRedirect('/')
	else:
		form = CustomerForm()
	context = {
		'form': form,
	}
	return render(request, 'shopping/user_info.html', context)

def CompleteShopInfo(request):
	if request.method == "POST":
		form = ShopInfoForm(request.POST)
		if form.is_valid():
			if 'submit' in request.POST:
				temp = Shop()
				temp = form.save(commit=False)
				request.user.is_complete = True
				temp.user = request.user
				temp.save()
				request.user.save()
				return HttpResponseRedirect('/')
	else:
		form = ShopInfoForm()
	context = {
		'form': form,
	}
	return render(request, 'shopping/shop_info.html', context)


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
				of.customer = request.user
				of.goods = goods
				of.number = number
				of.status = 1
				of.save()
				return HttpResponseRedirect('/user_order')
			if 'collect' in request.POST:
				sc = ShoppingCart()
				sc.customer = request.user
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

###########################################################################

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

#customer's order form list
#7/26 edit:
	#html add status 
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
			of.customer = request.user
			of.goods = cart.goods
			of.number = cart.number
			of.status = 1
			of.save()
			return HttpResponseRedirect('/user_order')
		if 'delete' in request.POST:
			cart.delete()
			return HttpResponseRedirect('/cart')
	context = {
		"cart" : cart
	}

	return render(request, 'shopping/cart.html', context)

#7/36 edit: 
	#add comfirm button
	#html add detail's such as address, shop.name, message etc.
def UserOrderFormDetail(request, order_id):
	order = OrderForm.objects.get(pk = order_id)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if 'comment' in request.POST:
			if form.is_valid():
				rating = form.cleaned_data['rating']
				content = form.cleaned_data['content']
				tel = form.cleaned_data['tel']
				cm = Comment()
				cm.rating = rating
				cm.content = content
				cm.tel = tel
				cm.customer = order.customer
				cm.goods = order.goods
				cm.save()
				context = {
					"goods_comment_list": order.goods,
				}
				return render(request,'shopping/comment.html', context)
			return HttpResponseRedirect('/user_order')
		if 'delete' in request.POST:
			order.delete()
			return HttpResponseRedirect('/user_order')
		if 'comfirm' in request.POST:
			order.status = 4
			return HttpResponseRedirect('/user_order')
	context = {
		"order" : order
	}
	return render(request, 'shopping/user_order.html', context)

#7/26 added. test by Dixon 
def UserInfoView(request):
	form = CustomerForm(request.POST, request.FILES)
	if 'changeInfo' in request.POST:
		if request.user.is_shop:
			return HttpResponseRedirect('/shop_info')
		else:
			return HttpResponseRedirect('/user_info')
	context = {
		"user" : request.user
	}
	return render(request, 'shopping/info_view.html', context)

