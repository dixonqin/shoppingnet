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
	# just for test
	sell = models.ForeignKey(Shop, on_delete = models.CASCADE)
	buy = models.ForeignKey(User, on_delete = models.CASCADE)

	price = models.IntegerField(default = 0)

	def __str__(self):
		return self.name