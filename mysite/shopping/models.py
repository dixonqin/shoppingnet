from django.db import models


# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length = 30)
	category = models.CharField(max_length = 30)

	class Meta:
		ordering = ["-name"]

	def __str__(self):
		return self.name

class User(models.Model):
	name = models.CharField(max_length = 30)
	email = models.EmailField()

	def __str__(self):
		return self.name

class Goods(models.Model):
	name = models.CharField(max_length = 30)
	shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
	price = models.IntegerField(default = 0)

	def __str__(self):
		return self.name

class Comment(models.Model):
	rating = models.IntegerField(default = 0)
	content = models.TextField(max_length = 200)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	def __str__(self):
		return self.content

class ShoppingCart(models.Model):
	number = models.IntegerField(default = 0)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

class OrderForm(models.Model):
	number = models.IntegerField(default = 0)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	goods = models.ForeignKey(Goods, on_delete = models.CASCADE)

	def __str__(self):
		return self.user.name