from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from .models import Category, Item, Cart

def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})
	regularpizza = Category.objects.get(pk="Regular Pizza")
	#sicilianpizza = Category.objects.get(pk="Sicilian Pizza")
	topping = Category.objects.get(pk="Toppings")
	context = {
		"regularpizzas": regularpizza.itemname.all(),
		#"sicilianpizzas": sicilianpizza.itemname.all(),
		"toppings": topping.itemname.all(),
	}

	return render(request, "orders/menu.html", context)

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		return HttpResponseRedirect(reverse("index"))
	else:
		return render(request, "orders/login.html", {"message": "Invalid Credentials"})

def logout_view(request):
	logout(request)
	return render(request, "orders/login.html", {"message": "Logged Out"})


def register_view(request):
	username = request.POST["username"]
	password = request.POST["password"]
	email = request.POST["email"]

	user = User.objects.create_user(username, email, password)
	user.first_name = request.POST["first"]
	user.last_name = request.POST["last"]
	user.save()
	login(request, user)

	return HttpResponseRedirect(reverse("index"))



def cart(request, item_id):
	if request.method == "POST":
		
