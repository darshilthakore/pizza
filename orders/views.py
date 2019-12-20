from django.shortcuts import render

# Create your views here.
from .models import Category, Item

def index(request):
	regularpizza = Category.objects.get(pk="Regular Pizza")
	sicilianpizza = Category.objects.get(pk="Sicilian Pizza")
	topping = Category.objects.get(pk="Toppings")
	context = {
		"regularpizzas": regularpizza.itemname.all(),
		"sicilianpizzas": sicilianpizza.itemname.all(),
		"toppings": topping.itemname.all(),
	}

	return render(request, "orders/menu.html", context)