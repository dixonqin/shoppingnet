from django.contrib import admin

# Register your models here.
from .models import Shop, Goods, Comment, OrderForm, Customer

# admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Goods)
admin.site.register(Comment)
admin.site.register(OrderForm)
admin.site.register(Customer)
