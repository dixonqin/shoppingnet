from django.contrib import admin

# Register your models here.
from .models import User, Shop, Goods

admin.site.register(User)
admin.site.register(Shop)
admin.site.register(Goods)
