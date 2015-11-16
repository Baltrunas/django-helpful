from django.utils.translation import ugettext_lazy as _
from django import template


register = template.Library()


def get_display(object, field):
	value = getattr(object, field.name)
	display = dict(field.flatchoices).get(value, value)
	if display is True:
		display = _('Yes')
	elif display is False:
		display = _('No')
	return display


@register.filter(name='object_dict')
def object_dict(object):
	fields = []
	for field in object._meta.fields:
		data = {}
		data['verbose_name'] = field.verbose_name
		data['display'] = get_display(object, field)
		data['field'] = field
		fields.append(data)
	return fields
