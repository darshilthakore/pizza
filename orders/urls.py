from django.urls import path


from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("<int:item_id>", views.cart, name="cart"),
	path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),
    path("order", views.submit_order, name="order"),
    path("removeitem", views.remove_cart_item, name="removeitem"),
]