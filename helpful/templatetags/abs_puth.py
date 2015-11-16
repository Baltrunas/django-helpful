import os

from django.conf import settings

from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def abs_puth(context, place, file_name):
	if place == 'static':
		return os.path.abspath(settings.STATIC_ROOT + '/' + file_name)
	elif place == 'media':
		return os.path.abspath(settings.MEDIA_ROOT + '/' + file_name)
	elif place == 'base':
		return os.path.abspath(settings.BASE_DIR + '/' + file_name)
	elif place == 'parent':
		return os.path.abspath(settings.BASE_DIR + '/../' + file_name)
