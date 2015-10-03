from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ShowcaseMenuItem)
admin.site.register(Slide)
admin.site.register(FrontPageCategory)