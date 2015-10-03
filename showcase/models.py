from django.db import models

# Create your models here.
from django.conf import settings

class ShowcaseMenuItem(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	url=models.URLField(null=True, blank=True)
	image = models.ImageField(upload_to="showcase_menu_images")

class Slide(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	url=models.URLField(null=True, blank=True)
	image = models.ImageField(upload_to="slide_images")


import items

class FrontPageCategory(models.Model):
	category = models.ForeignKey(items.models.Category)
	order = models.IntegerField()
#	is_visible_in_front_page = models.BooleanField(default=True)

	def __str__(self):
		return self.category.name