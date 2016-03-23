from django import template

register = template.Library()

@register.filter
def get_item(obj, key):
	if hasattr(obj, key):
		return getattr(obj, key)
	else:
		return obj.__dict__.get(key)

@register.filter
def get_property_value(value, key):
	return value.get_property_value(key)
