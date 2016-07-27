from django.db import models
from django.conf import settings

# Create your models here.
class Shop(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
	name = models.CharField(max_length = 30, default="")
	description = models.CharField(max_length = 200, default="")
	category = models.CharField(max_length = 20, default="")
	#location = models.CharField(max_length = 100, default="")
	address = models.CharField(max_length = 200, default="")

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class Customer(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = '')
	name = models.CharField(max_length = 20, default="")
	address = models.CharField(max_length = 200, default="")
	sex = models.CharField(max_length = 10, default="")
	tel = models.CharField(max_length = 20, default = "")
	#head_img = models.ImageField(upload_to = 'img', null=True, blank=True)
	self_intro = models.CharField(max_length = 300, default="")

	def __str__(self):
		return self.name


class Goods(models.Model):
	shop = models.ForeignKey(Shop, on_delete = models.CASCADE, default = '')
	#以下商品信息，店主无法直接修改
	name = models.CharField(max_length = 30, default = "")
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
	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 200, default = "")
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = '')
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE, default = '')

	def __str__(self):
		return self.content

class ShoppingCart(models.Model):
	number = models.IntegerField(default = 0)
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default = "")
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE, default = "")

class OrderForm(models.Model):
	status = models.IntegerField(default = 0)#1是下单，2是确认，3是发货，4是收货
	number = models.IntegerField(default = 0)
	customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, default="")
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE, default = "")
	message = models.CharField(max_length = 200, default = "")
	tel = models.CharField(max_length = 20, default = "")
	address = models.CharField(max_length = 100, default = "")

	def __str__(self):
		return self.customer.name

