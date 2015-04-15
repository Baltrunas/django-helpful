from os.path import dirname

import re
import hashlib
import pynliner

from email.MIMEImage import MIMEImage

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string
from django.template.loader import get_template


def mail(subject, context, template, email_to, email_from):
	email_puth = get_template(template + '.html')
	email_dir = dirname(email_puth.origin.name) + '/'

	email_html = render_to_string(template + '.html', context)
	email_txt = render_to_string(template + '.txt', context)

	plinper = pynliner.Pynliner()
	plinper.relative_url = 'file://localhost/' + email_dir
	email_html = plinper.from_string(email_html).run()

	email = EmailMultiAlternatives(subject, email_txt, email_from, email_to)
	email.mixed_subtype = 'related'

	# Find all images in html
	img_regex = '<img(.*?)src="(.*?)"(.*?)>'
	compiled_img_regex = re.compile(img_regex)
	images = compiled_img_regex.findall(email_html)
	# Replace src to cid
	for image in images:
		img_path = email_dir + image[1]
		img_file = open(img_path , 'rb')
		img = MIMEImage(img_file.read())
		img_file.close()

		img_cid = hashlib.md5(open(img_path, 'rb').read()).hexdigest()
		img.add_header('Content-ID', '<%s>' % img_cid)
		img.add_header('Content-Disposition', 'inline')

		email.attach(img)

		replace = 'cid:%s' % img_cid
		email_html = re.sub(image[1], replace , email_html)

	email.attach_alternative(email_html, "text/html")
	email.send()
