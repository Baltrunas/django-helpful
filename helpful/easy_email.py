import re
import hashlib
import pynliner

from email.MIMEImage import MIMEImage

from django.core.mail import EmailMultiAlternatives

from django.template.loader import render_to_string


def mail(subject, context, template, from_email, to_email, connection=None, reply_to=None):
	html_template = render_to_string(template + '.html', context)
	txt_template = render_to_string(template + '.txt', context)

	plinper = pynliner.Pynliner()
	plinper.relative_url = 'file://localhost/'

	html_email = plinper.from_string(html_template).run()
	if reply_to:
		email = EmailMultiAlternatives(subject, txt_template, from_email, to_email, reply_to=reply_to)
	else:
		email = EmailMultiAlternatives(subject, txt_template, from_email, to_email)
	email.mixed_subtype = 'related'

	# Find all images in html
	img_regex = '<img(.*?)src=("|\')(.*?)("|\')(.*?)>'
	compiled_img_regex = re.compile(img_regex)
	images = compiled_img_regex.findall(html_email)

	# Replace src to cid
	for image in images:
		img_path = image[2]
		img_file = open(img_path , 'rb')
		img = MIMEImage(img_file.read())
		img_file.close()

		img_cid = hashlib.md5(open(img_path, 'rb').read()).hexdigest()
		img.add_header('Content-ID', '<%s>' % img_cid)
		img.add_header('Content-Disposition', 'inline')

		email.attach(img)
		html_email = re.sub(img_path, 'cid:%s' % img_cid , html_email)

	email.attach_alternative(html_email, "text/html")

	if connection:
		connection.open()

	email.send()
