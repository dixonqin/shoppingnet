from django.db import models
from django.conf import settings

# Create your models here.
class Shop(models.Model):

	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
	name = models.CharField(max_length = 30)
	category = models.CharField(max_length = 30)

	class Meta:
		ordering = ["-name"]

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
	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	def __str__(self):
		return self.content

class ShoppingCart(models.Model):
	number = models.IntegerField(default = 0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

class OrderForm(models.Model):
	number = models.IntegerField(default = 0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.username