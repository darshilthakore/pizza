# Project 3

Web Programming with Python and JavaScript

The project Pizza contains the app called orders in which we have the following files:
1. models.py
1. admin.py
1. views.py
1. urls.py
1. templates/orders/menu.html
1. templates/orders/login.html
1. static/orders/style.css


## models.py

In the __models.py__ file, all the models required for the application to work are defined.

We have a __Category__ model for determining the category our item in the menu _(eg. Regular Pizza, Sicilian Pizza, Subs, Salads, Dinner Platters, Pasta...)_

__Item__ model defines all the items of our menu alongwith its _name,category and price_ (category name of the Category model acts as a foreign key here)

__Cart__ model is used to store the items, that a user enters to the cart. Here __item__ field is a foreign key of __Item__ model and __topping__ is a ManyToMany field which helps for creating a through table for storing multiple toppings on an item in the cart. __Cart__ also stores the name of the user, base price of the item and grand total of the order if there are extra toppings.


Lastly, __Order__ model is used when the order is placed by the user, where the data of cart is passed in this model. This model is stored for the record of the orders made by the user, which is helpful for the admin side(restaurant side) for keeping tracks of orders.


## admin.py

In the __admin.py__ file, we have registered all the models defined in __models.py__, so that we can use the admin site to enter and manage the menu and orders over database.

Here with the use of __ModelAdmin__, the __Order__ model's admin site is customized, providing the option to confirm the orders placed by the user with the help of the function `order_confirmation`.

`OrderAdmin` class provides for how the details will be visible on the admin page for this model.

## login.html

When the app runs for the first time, login page would be loaded, where user can register with new account or login with an existing account.

When user registers for a new account, he is redirected to the `register_view` in __views.py__, where all the details are used to register a new user and that user is logged in and redirected to `index` view.

If a user logins with existing account, he redirected to `login_view` in __views.py__ and then he/she is authenticated. If successful, the it redirects to __login.html__, else to `index` view.

`index` view checks if there is any user authenticated or not, if not then he/she is asked to login again. `index` view retrieves all the required information used for loading the __menu.html__ page from the databases by running the queries and passing them as context to the __menu.html__ page.


## menu.html

__menu.html__ contains all the code needed to display the menu defined in database. Users can select from the menu the item of their choice, alongwith options to select their own size of the item with extra toppings on the available items.

On selecting the choices of an item, user can then click __Add to Cart__ button to add that item to their cart. Cart is present on the right side of the page, where user can keep track of the items that he/she wants to order alongwith the Total cost of the order.

When a user clicks the __Add to Cart__ button, the details selected for that item is passed through the __POST__ request on the `cart` view in __views.py__, where the selection is stored in the __Cart__ model. This results in calling the `index` view again which updates the cart of __menu.html__.

Also in the cart area of __menu.html__, for each item, user can remove the item from the cart, by clicking the __Remove item__ which will call an AJAX request to `remove_cart_item`, which will remove that item from the __Cart__ and will update the cart details.

On clicking the __Order__ button calls the view `submit_order` in __views.py__, which will transfer the items in the cart for the user to the __Order__ table. This will update the cart area of the menu.html with the details of the order which is placed, along with a status for our order, whether it's confirmed or not from the restaurant.

On clicking the logout button, `logout_view` of __views.py__ will be called and the user will be logged out to the __login.html__ page.


## admin side

The admin can login to admin page and navigate to the __Orders__ and then can see the pending orders, and can confirm the status of the orders, which is customized behaviour implemented for this app, which will update the status of the orders visible to user on refreshing the page.

Admin can enter new items to the menu by navigating to __Items__ and then add items alongwith price, size etc.


## urls.py

All the views from the views.py are imported here in __urls.py__, and path for each view is defined in here.


## style.css

It includes the necessary stylings for __menu.html__ and __login.html__.



# Steps for running

## using the application.

1. Navigate to the root directory of project in terminal.
1. Enter `pip3 install -r requirements.txt`.
1. Enter `python3 manage.py runserver`
1. Now open the url displayed on terminal on a browser.

## using the admin interface.

1. Create an admin superuser.
1. Add /admin at the end of the url for opening admin interface.
1. eg. `127.0.0.1:8000/admin`.
