from django.shortcuts import render

# Create your views here.
from showcase.models import *
from items.models import *
def index(request):
	front_page_cat=FrontPageCategory.objects.all()
	recent =Item.objects.all().order_by("-created_at")[0:5]


	return render(request, 'items/index.html',{'showcase_items': ShowcaseMenuItem.objects.all(),
    											'slide':Slide.objects.all(),
    											'front_page_categories': front_page_cat,
    											'recent':recent,
    											'trending':Item.objects.filter(category_id=1)[0:5],
    											}
    											)