from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag(takes_context=True)
def render(context, content):
	try:
		tpl = template.Template(content)
		content = template.Context(context)
		return tpl.render(content)
	except Exception as e:
		return mark_safe("<div cllass='b-error'>Render Error: <code>%s</code></div>" % e.message)
