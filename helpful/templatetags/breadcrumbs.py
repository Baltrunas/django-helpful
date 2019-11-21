from django import template
register = template.Library()


def get_br(obj):
	br = [obj]
	if hasattr(obj, 'parent') and obj.parent:
		br += get_br(obj.parent)
	elif hasattr(obj, 'category') and obj.category:
		br += get_br(obj.category)
	return br

@register.simple_tag(takes_context=True)
def breadcrumbs(context, obj):
	context = {}
	context['breadcrumbs'] = reversed(get_br(obj))

	tpl = template.loader.get_template('helpful/breadcrumbs.html')
	return tpl.render(context)
