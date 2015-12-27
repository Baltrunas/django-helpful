from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def render(context, content):
	try:
		tpl = template.Template(content)
		content = template.Context(context)
		return tpl.render(content)
	except:
		return 'Render Error'
