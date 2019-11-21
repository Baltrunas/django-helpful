from django.http import HttpResponseRedirect
from django.conf import settings

class LoginRequiredMiddleware(object):
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		response = self.get_response(request)

		if not request.user.is_authenticated:
			path = request.path_info.lstrip('/')

			if path not in ['accounts/login/', 'admin/', 'admin/login/?next=/admin/', 'admin/login/']:
				return HttpResponseRedirect(settings.LOGIN_URL)

		return response
