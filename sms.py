import urllib
import urllib2

from django.conf import settings


def urlencode(string):
	string = urllib.unquote(string)
	string = u'' + urllib.quote(string.encode('utf-8'))
	return string


def send_sms(text, phone=settings.SMS_TO):
	url = 'http://sms.ru/sms/send?api_id=%s&to=%s&text=%s&from=%s&translit=0' % (
		settings.SMS_KEY,
		urlencode(phone),
		urlencode(text),
		urlencode(settings.SMS_NAME)
	)
	urllib2.urlopen(url)
