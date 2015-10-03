from django import template

register = template.Library()


@register.filter
def up_tri(value):
	html=""
	for i,j in [(0,4),(4,7),(7,9),(9,10)]
		html="""<div class="row d">"""
		for item in value[0:4]:
			html+="""
			<a class="col-md-3" href="/{{i.image.url}}" title="This is a dress" data-gallery="">
		      <img src="/%s" alt="this is not banana">
		  	</a>
		  	""" % item.image.url
		
		html+="""</div>"""
    return html