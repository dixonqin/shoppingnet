# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Shop(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
	name = models.CharField(max_length = 30, default="")
	description = models.TextField(max_length = 300)
	sold_number = models.IntegerField(default = 0)
	category = models.CharField(max_length = 20, default="")
	tele = models.CharField(max_length = 20, default="")
	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = '')
	head_img = models.ImageField(upload_to = 'img', null=True, blank=True, default="img/no_image.png")
	name = models.CharField(max_length = 20, default="")
	address = models.CharField(max_length = 200, default="")
	sex = models.CharField(max_length = 10, default="")
	self_intro = models.TextField(max_length = 300)
	tele = models.CharField(max_length = 20, default="")
	def __str__(self):
		return self.name

class Goods(models.Model):
	image = models.ImageField(upload_to = 'img', null=True, blank=True, default="img/no_img.jpg")
	shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
	#以下商品信息，店主无法直接修改
	name = models.CharField(max_length = 30)
	category = models.CharField(max_length = 20, default="")
	description = models.TextField(max_length = 300)
	price = models.IntegerField(default = 0)
	number = models.IntegerField(default = 0)
	#以下信息，店主无法修改
	sold_number = models.IntegerField(default = 0)
	rating = models.IntegerField(default = 0)
	rating_number = models.IntegerField(default = 0)
	#
	rating_total = models.IntegerField(default = 0)

	def __str__(self):
		return str(self.name)+'+'+str(self.id)

class OrderForm(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)
	total_price = models.IntegerField(default = 0)
	number = models.IntegerField(default = 0)
	message = models.CharField(max_length = 200, default="")
	address = models.TextField(max_length = 300)
	tele = models.CharField(max_length = 20, default="")
	#-1 表示是购物车
	#1	下单 
	#2	确认
	#3	发货
	#4	收货
	#5  完成
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

class Comment(models.Model):
	order =  models.OneToOneField(OrderForm, on_delete = models.CASCADE, default='')
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default='')
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE, default='')
	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 300)
	date = models.DateTimeField(default = datetime.now)
	isReplied = models.BooleanField(default = 'False')

	def __str__(self):
		return self.content

class Reply(models.Model):
	comment = models.ForeignKey(Comment, on_delete = models.CASCADE, default='')
	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 300)
	date = models.DateTimeField(default = datetime.now)

	def __str__(self):
		return self.content
