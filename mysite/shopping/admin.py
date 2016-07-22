from django.contrib import admin

# Register your models here.
from .models import User, Shop, Goods, Comment, ShoppingCart, OrderForm

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Goods)
admin.site.register(Comment)
admin.site.register(ShoppingCart)
admin.site.register(OrderForm)
