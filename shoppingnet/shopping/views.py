from shopping.forms import GoodsForm, ManageGoodsForm, ShopInfoForm, CustomerForm, UserOrderForm, SearchForm, ReplyForm, CommentForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from shopping.models import Goods, Shop, OrderForm, Comment, Customer, Reply


def HomePage(request):
	if request.user.is_authenticated() and request.user.is_complete == False and request.user.is_shop == True:
		return HttpResponseRedirect('/shop_info/')

	if request.user.is_authenticated() and request.user.is_complete == False and request.user.is_shop == False:
		return HttpResponseRedirect('/user_info/')

	if request.user.is_authenticated() and request.user.is_shop == True:
		return HttpResponseRedirect('/shop/' + str(request.user.shop.id))

	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			temp = form.save(commit=False)
			if temp.object_name == '商品' and temp.field_name == '名称':
				goods_list = Goods.objects.filter(name__contains=temp.content)
				return GoodsSearchResult(request, goods_list)
			if temp.object_name == '商品' and temp.field_name == '类别':
				goods_list = Goods.objects.filter(category__contains=temp.content)
				return GoodsSearchResult(request, goods_list)
			if temp.object_name == '商店' and temp.field_name == '名称':
				shop_list = Shop.objects.filter(name__contains=temp.content)
				return ShopSearchResult(request, shop_list)
			if temp.object_name == '商店' and temp.field_name == '类别':
				shop_list = Shop.objects.filter(category__contains=temp.content)
				return ShopSearchResult(request, shop_list)
	else:
		form = SearchForm()
	
	index_shop_List = Shop.objects.order_by("id")
	context = {
		'index_shop_List' : index_shop_List,
		'form': form,
		'user': request.user,
	}
	return render(request, 'shopping/index.html', context)

def GoodsSearchResult(request, goods_list):
	if len(goods_list) == 0:
		return render(request, 'shopping/search_not_found.html')
	context = {
		'goods_list' : goods_list,
		'user' : request.user,
	}
	return render(request, 'shopping/search_goods.html', context)

def ShopSearchResult(request, shop_list):
	if len(shop_list) == 0:
		return render(request, 'shopping/search_not_found.html')
	context = {
		'shop_list' : shop_list,
	}
	return render(request, 'shopping/search_shop.html', context)

def CompleteUserInfo(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		if request.user.is_complete == True:
			form = CustomerForm(request.POST, request.FILES, instance=request.user.customer)
		else:
			form = CustomerForm(request.POST, request.FILES)
		if form.is_valid():
			if 'submit' in request.POST:
				temp = Customer()
				temp = form.save(commit=False)
				request.user.is_complete = True
				temp.user = request.user
				temp.save()
				request.user.save()
				return HttpResponseRedirect('/')
	else:
		if request.user.is_complete == True:
			form = CustomerForm(instance=request.user.customer)
		else:
			form = CustomerForm()
	context = {
		'form': form,
		'user': request.user,
	}
	return render(request, 'shopping/user_info.html', context)

def CompleteShopInfo(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		if request.user.is_complete:
			form = ShopInfoForm(request.POST, instance=request.user.shop)
		else:
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
		if request.user.is_complete:
			form = ShopInfoForm(instance=request.user.shop)
		else:
			form = ShopInfoForm()
	context = {
		'form': form,
	}
	return render(request, 'shopping/shop_info.html', context)


def ShopDetail(request, shop_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	shop = Shop.objects.get(pk = shop_id)
	context = {
		'shop' : shop,
	}
	return render(request, 'shopping/user_goods_list.html', context)

def ManageShop(request, shop_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	shop = Shop.objects.get(pk = shop_id)
	context = {
		'shop' : shop,
	}
	return render(request, 'shopping/shop_goods_list.html', context)

def GoodsDetail(request, goods_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	goods = Goods.objects.get(pk = goods_id)
	if request.method == 'POST':
		form = UserOrderForm(request.POST)
		if form.is_valid():
			if 'buy' in request.POST:
				of = OrderForm()
				of = form.save(commit=False)
				if of.number > goods.number:
					return HttpResponseRedirect('/')
				of.goods = goods
				goods.sold_number += of.number
				goods.number -= of.number
				goods.save()
				of.user = request.user
				of.total_price = of.number * goods.price
				of.status = 1
				of.save()
				return HttpResponseRedirect('/user_order/')
			if 'collect' in request.POST:
				of = OrderForm()
				of = form.save(commit=False)
				if of.number > goods.number:
					return HttpResponseRedirect('/')
				of.goods = goods
				of.user = request.user
				of.status = -1
				of.save()
				return HttpResponseRedirect('/cart/')
			if 'viewComment' in request.POST:
				context = {
					'goods': goods,
				}
				return render(request, 'shopping/comment.html', context)
	else:
		form = UserOrderForm()

	context = {
        'goods': goods,
        'form' : form,
    }
	return render(request, 'shopping/goods.html', context)

def ManageGoods(request, goods_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	goods = Goods.objects.get(pk = goods_id)
	message = '请在表单中修改'

	if request.method == 'POST':
		form = ManageGoodsForm(request.POST, request.FILES, instance = goods)
		if form.is_valid():
			if 'delete' in request.POST:
				shop_id = goods.shop.id
				goods.delete()
				return HttpResponseRedirect('/shop/'+str(shop_id)+'/')
			if 'save' in request.POST:
				form.save()
				form = ManageGoodsForm(instance= goods)
				message = '成功修改！'
	else:
		form = ManageGoodsForm(instance = goods)

	context = {
        'goods': goods,
        'form' : form,
        'message' : message, 
    }
	return render(request, 'shopping/shop_goods.html', context)

def AddGoods(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == "POST":
		form = ManageGoodsForm(request.POST, request.FILES)
		if form.is_valid():
			if 'submit' in request.POST:
				temp = Goods()
				temp = form.save(commit=False)
				temp.shop = request.user.shop
				temp.save()
				return HttpResponseRedirect('/')
	else:
		form = ManageGoodsForm()
	context = {
		'form': form,
	}
	return render(request, "shopping/shop_add_goods.html", context)

def UserShoppingCart(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	user_cart = request.user.orderform_set.all().filter(status = -1)
	if request.method == "POST":
		if 'buy' in request.POST:
			for order in user_cart:
				order.goods.sold_number += order.number
				order.goods.number -= order.number
				order.total_price = order.number * order.goods.price
				order.status = 1
				order.save()
				order.goods.save()
	user_cart = request.user.orderform_set.all().filter(status = -1)
	context = {
		"user_cart" : user_cart,
	}
	return render(request, "shopping/user_cart_list.html", context)

def UserShoppingCartDetail(request, order_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	order = OrderForm.objects.get(pk = order_id)
	if request.method == "POST":
		if 'buy' in request.POST:
			order.status = 1
			order.goods.sold_number += order.number
			order.goods.number -= order.number
			order.total_price = order.number * order.goods.price
			order.goods.save()
			order.save()
			return HttpResponseRedirect('/order')
		if 'delete' in request.POST:
			order.delete()
			return HttpResponseRedirect('/cart')
	context = {
		"order" : order
	}

	return render(request, 'shopping/cart.html', context)

def UserOrder(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	user_order = request.user.orderform_set.all().exclude(status = -1)
	context = {
		"user_order" : user_order,
	}
	return render(request, "shopping/user_order_list.html", context)

def UserOrderFormDetail(request, order_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	order = OrderForm.objects.get(pk = order_id)
	com = CommentForm(request.POST)
	message = "请进行操作"
	if request.method == "POST":
		if 'delete' in request.POST:
			order.delete()
			return HttpResponseRedirect('/user_order')
		if 'cancle' in request.POST:
			order.status = 0
			return HttpResponseRedirect('/user_order')
		if 'confirm' in request.POST:
			order.status = 4
			order.save()
			message = '确认收货成功'
		if 'comment' in request.POST:
			comm = Comment()
			comm = com.save(commit=False)
			comm.user = request.user
			comm.order = order
			if comm.rating > 5:#分数大于5时，取5
				comm.rating = 5
			if comm.rating < 0:#分数小于0时，取0
				comm.rating = 0
			order.goods.rating_total += comm.rating
			order.goods.rating_number += 1
			order.goods.rating = order.goods.rating_total / order.goods.rating_number
			#comm.save()
			order.status = 5
			order.save()
			context={
				'goods': order.goods,
			}
			return render(request, 'shopping/comment.html', context)
	context = {
		"order" : order,
		'message' : message,
		'comment': com, 
	}
	return render(request, 'shopping/user_order.html', context)

def CommentView(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return HttpResponseRedirect('/')

def ShopOrder(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	shop = request.user.shop
	context = {
		'shop' : shop,
	}
	return render(request, "shopping/shop_order_list.html", context)

def ShopOrderFormDetail(request, order_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	order = OrderForm.objects.get(pk = order_id)
	message = '请进行操作'
	form = CommentForm(request.POST)
	if request.method == 'POST':
		if 'confirm' in request.POST and order.status == 1:
			order.status = 2
			order.save()
			message = '成功确认订单'
		if 'delivery' in request.POST and order.status == 2:
			order.status = 3
			order.save()
			message = '成功发货'
		if 'reply' in request.POST and order.status == 5:
			repForm = ReplyForm(request.POST)
			rep = Reply()
			rep = repForm.save(commit=false)
			if rep.rating > 5:#分数大于5时，取5
				rep.rating = 5
			if rep.rating < 0:#分数小于0时，取0
				rep.rating = 0
			rep.save()
			order.comment.reply = rep
			order.comment.isReplied = True
			order.comment.save()

	context = {
        'order': order,
        'message' : message,
	}
	return render(request, 'shopping/shop_order.html', context)

def InfoView(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.user.is_shop == True:
		return HttpResponseRedirect('/shop_info/')
	else:
		return HttpResponseRedirect('/user_info/')

