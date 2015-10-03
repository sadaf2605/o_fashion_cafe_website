from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)

	def items(self):
		return Item.objects.filter(category_id=self.id)

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image = models.ImageField(upload_to="item_images")
	category = models.ForeignKey(Category)

	show_in_front_page= models.BooleanField(default=True)
	always_show_in_front_page= models.BooleanField(default=True)
	is_trending=models.BooleanField(default=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name



