from django import template

register = template.Library()


@register.filter
def up_tri(value):
	html=""
	c=0
	for (i,j) in [(0,4),(4,7),(7,9)]:
		html+="""<div class="row d up-tri">"""
		
		for item in value[i:j]:
			html+="""
			<a class="col-md-3 up-tri-%s" href="/%s" title="This is a dress" data-gallery="">
		      <img src="/%s" alt="this is not banana">
		  	</a>
		  	""" % (c,item.image.url,item.image.url)
		  	c+=1
		
		html+="""</div>"""

	html+="""<div class="row d up-tri">
					<a class="col-md-3 text-center vcenter up-tri-%s others" >
	                  <img src="/media/logo.png">
	                  Our other items like this
	                </a>
	             </div>
              """ % c
	return html


@register.filter
def down_tri(value):
	html=""
	c=0
	for (i,j) in [(0,1),(1,3),(3,6),(6,9)]:
		html+="""<div class="row l down_tri">"""
		for item in value[i:j]:
			html+="""
			<a class="col-md-3 down-tri-%s" href="/%s" title="This is a dress" data-gallery="">
		      <img src="/%s" alt="this is not banana">
		  	</a>
		  	""" % (c,item.image.url,item.image.url)
		  	c+=1
		if j == 9:
		  	html+="""<div class="row l down-tri">
					<div class="col-md-3 text-center vcenter down-tri-%s others" >
	                   <img src="/media/logo.png">
	                  Our other items like this
	                </div>
	             </div>
              """% c
		
		html+="""</div>"""


	return html