# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Shop(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
	name = models.CharField(max_length = 30, default="")
	description = models.CharField(max_length = 200, default="")
	category = models.CharField(max_length = 20, default="")
	
	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = '')
	name = models.CharField(max_length = 20, default="")
	address = models.CharField(max_length = 200, default="")
	sex = models.CharField(max_length = 10, default="")
	self_intro = models.CharField(max_length = 300, default="")
	tele = models.IntegerField(default = 0)
	
	def __str__(self):
		return self.name

class Goods(models.Model):
	shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
	#以下商品信息，店主无法直接修改
	name = models.CharField(max_length = 30)
	category = models.CharField(max_length = 20, default="")
	description = models.CharField(max_length = 200, default="")
	price = models.IntegerField(default = 0)
	number = models.IntegerField(default = 0)
	#以下信息，店主无法修改
	sold_number = models.IntegerField(default = 0)
	rating = models.IntegerField(default = 5, editable = 'false')
	rating_number = models.IntegerField(default = 0, editable = 'false')

	def __str__(self):
		return str(self.name)+'+'+str(self.id)

class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 200)

	date = models.DateTimeField(default = datetime.now) 

	def __str__(self):
		return self.content

class OrderForm(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	number = models.IntegerField(default = 0)
	message = models.CharField(max_length = 200, default="")
	address = models.CharField(max_length = 200, default="")
	tele = models.IntegerField(default = 0)
	#-1 表示是购物车
	#1	下单 
	#2	确认
	#3	发货
	#4	收货
	status = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.customer.name

class Search(models.Model):
	OBJECTNAME_CHOICE = (
		('商店','商店'),
		('商品','商品'),
	)
	FIELDNAME_CHOICE = (
		('名称','名称'),
		('类别','类别'),
	)

	content = models.CharField(max_length = 20, default="")
	object_name = models.CharField(max_length = 4, choices = OBJECTNAME_CHOICE, default = '商品')
	field_name = models.CharField(max_length = 4, choices = FIELDNAME_CHOICE, default = '名称')
