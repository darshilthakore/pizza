from django.contrib import admin

# Register your models here.
from .models import Category, Item, Cart, Topping

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(Topping)