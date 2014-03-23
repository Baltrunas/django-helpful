# -*- coding: utf-8 -*-
from django import template

import base64
import mimetypes

register = template.Library()


@register.filter()
def image2base64(image):
	if image:
		with open(image.path, 'rb') as image_bin:
			image_base64 = base64.b64encode(image_bin.read())

		image_mimetype = mimetypes.guess_type(image.path)[0]

		return 'data:%s;base64,%s' % (image_mimetype, image_base64)
