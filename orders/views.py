from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from .models import Category, Item, Cart, Topping, Order

def index(request):
	if not request.user.is_authenticated:
		return render(request, "orders/login.html", {"message": None})
	regularpizza = Category.objects.get(pk="Regular Pizza")
	sicilianpizza = Category.objects.get(pk="Sicilian Pizza")
	sub = Category.objects.get(pk="Subs")
	pasta = Category.objects.get(pk="Pasta")
	salad = Category.objects.get(pk="Salads")
	platter = Category.objects.get(pk="Dinner Platters")

	fname = request.user.first_name
	print(f"User is: {fname}")
	cart = Cart.objects.filter(user=fname)
	print(f"cart is this: {cart}")
	user_cart = []


	#getting cart total
	total = 0
	for c in cart:
		user_cart.append(c)
		total += c.grand_total

	print(user_cart)


	order = Order.objects.filter(customer=fname)
	print(f"order is {order}")
	context = {
		"user": request.user,
		"regularpizzas": regularpizza.itemname.all(),
		"sicilianpizzas": sicilianpizza.itemname.all(),
		"subs": sub.itemname.all(),
		"pastas": pasta.itemname.all(),
		"salads": salad.itemname.all(),
		"platters": platter.itemname.all(),
		"toppings": Topping.objects.all(),
		"user_cart": user_cart,
		"total": total,
		"order": order,
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
		item = Item.objects.get(pk=item_id)
		print(f"item is {item.name}")
		item_price = request.POST['price']
		print(f"item price is {item_price}")
		topping_id = request.POST.getlist('toppings')
		print(f"topping ids is/are : {topping_id}")

		#updating the total price after considering additional topping
		total_cost = float(item_price)
		for t in topping_id:
			total_cost = total_cost + float(Topping.objects.get(pk=int(t)).rate)
			print(f"Total cost in loop is :: {total_cost}")

		#creating the cart for a user
		cart = Cart(user=request.user.first_name, item=item, base_price=item_price, grand_total=total_cost)
		cart.save()

		#adding the topping to cart
		for t in topping_id:
			topping = Topping.objects.get(pk=int(t))
			cart.topping.add(topping)

		return HttpResponseRedirect(reverse("index"))



def submit_order(request):
	user = request.user.first_name
	print(f"Ordered placed by {user}")
	c = Cart.objects.filter(user=user)
	print(f"contents of cart for {user} are {c}")
	#move the data to the order table
	for cart in c:
		order = Order(customer=cart.user, item=cart.item, base_price=cart.base_price, grand_total=cart.grand_total)
		order.save()
		for topping in cart.topping.all():
			order.topping.add(topping)
	#clear the cart
	for cart in c:
		cart.delete()

	return HttpResponseRedirect(reverse("index"))


def remove_cart_item(request):
	print("removing cart item")
	item_id = request.POST['item_id']

	item = Cart.objects.get(pk=item_id)
	user = item.user
	item.delete()
	items = Cart.objects.filter(user=user)
	total = 0
	for item in items:
		total += item.grand_total

	return JsonResponse({"total": total})