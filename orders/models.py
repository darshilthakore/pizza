from django.db import models

# Create your models here.
# class Category(models.Model):
# 	name = models.CharField(max_length=64, primary_key=True)

# 	def __str__(self):
# 		return f"{self.name}"

# class Item(models.Model):
# 	name = models.CharField(max_length=64)
# 	cname = models.CharField(max_length=64)
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="itemname")
# 	price_small = models.FloatField(default=0)
# 	price_large = models.FloatField(default=0)

# 	def __str__(self):
# 		return f"{self.category} - {self.name} | Small : ${self.price_small} | Large : ${self.price_large}"ategory = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="itemname")
# 	price_small = models.FloatField(default=0)
# 	price_large = models.FloatField(default=0)

# 	def __str__(self):
# 		return f"{self.category} - {self.name} | Small : ${self.price_small} | Large : ${self.price_large}"


class Category(models.Model):
	name = models.CharField(max_length=64, primary_key=True)

	def __str__(self):
		return f"{self.name}"

class Item(models.Model):
	name = models.CharField(max_length=64)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="itemname")
	price_small = models.FloatField(default=0)
	price_large = models.FloatField(default=0)

	def __str__(self):
		return f"{self.category} - {self.name} | Small : ${self.price_small} | Large : ${self.price_large}"


class Cart(models.Model):
	user = models.CharField(max_length=64)
	item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="cartitem")
