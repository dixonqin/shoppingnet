from django import forms
from django.forms import ModelForm
from registration.forms import RegistrationForm
from customauth.models import MyUser
from shopping.models import Goods, Shop, Customer, OrderForm, Comment, Search, Reply
from django.utils.translation import ugettext_lazy as _

class MyCustomUserForm(RegistrationForm):
    class Meta:
        model = MyUser
        fields = ['email', 'is_shop']

class GoodsForm(forms.Form):
	number = forms.IntegerField()

class ManageGoodsForm(forms.ModelForm):
	class Meta:
		model = Goods
		exclude = ['shop', 'rating','rating_number', 'rating_total', 'sold_number']
		labels = {
			'name':_("名称"),
			'category':_("类别"),
			'description':_("描述"),
			'price':_("价格"),
			'number':_("数量"),
		}

class ShopInfoForm(forms.ModelForm):
	class Meta:
		model = Shop
		exclude = ['user','sold']
		labels = {
			'name':_("名称"),
			'category':_("类别"),
			'tele':_("联系方式"),
			'description':_("描述"),
		}

class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		exclude = ['user',]
		labels = {
			'head_img':_("头像"),
			'name':_("姓名"),
			'sex':_("性别"),
			'tele':_("联系方式"),
			'address':_("地址"),
			'self_intro':_("个人简介"),	
		}

class UserOrderForm(forms.ModelForm):
	class Meta:
		model = OrderForm
		fields = ['number', 'message', 'tele', 'address']
		labels = {
			'number':_("数量"),
			'message':_("附加信息"),
			'tele':_("联系方式"),
			'address':_("收货地址"),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['rating', 'content']
		labels = {
			'rating':_("评分"),
			'content':_("评论"),
		}

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ['rating', 'content']
		labels = {
			'rating':_("评分"),
			'content':_("回复内容"),
		}

class SearchForm(forms.ModelForm):
	class Meta:
		model = Search
		fields = ['content', 'field_name', 'object_name']