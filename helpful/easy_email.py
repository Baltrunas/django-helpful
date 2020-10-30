import re
import hashlib
import pynliner
import os

from email.mime.image import MIMEImage

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def mail(subject, context, template, from_email, to_email, connection=None, reply_to=None, attach_files=[], cc=None, bcc=None):

	html_template = render_to_string(template + '.html', context)
	txt_template = render_to_string(template + '.txt', context)

	# email debug mode
	if hasattr(settings, 'EMAIL_DEBUG'):
		if not cc:
			cc = []
		if not bcc:
			bcc = []

		if hasattr(settings, 'EMAIL_DEBUG_INFO') and settings.EMAIL_DEBUG_INFO:
			pre_info = 'to_email: ' + ', '.join(to_email) + '\n'\
							+ 'cc: ' + ', '.join(cc) + '\n'\
							+ 'bcc: ' + ', '.join(bcc)
			html_template = '<pre>' + pre_info + '\n\n</pre>' + html_template
			txt_template = pre_info + '\n\n' + txt_template

		to_email = settings.EMAIL_DEBUG
		cc = None
		bcc = None
	elif settings.DEBUG:
		return

	plinper = pynliner.Pynliner()
	plinper.relative_url = 'file://localhost/'

	html_email = plinper.from_string(html_template).run()

	email = EmailMultiAlternatives(subject, txt_template, from_email, to_email, reply_to=reply_to, cc=cc, bcc=bcc)
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

	for attach_file in attach_files:
		attachment = open(attach_file, 'rb')
		file_name = os.path.basename(attach_file)
		email.attach(file_name, attachment.read()) # , 'text/csv'

	email.attach_alternative(html_email, "text/html")

	if connection:
		connection.open()

	email.send()
