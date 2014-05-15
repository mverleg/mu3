
'''
	decorator makes the page redirect to https if the connection is not secure.
	credits go to http://www.redrobotstudios.com/blog/2009/02/18/securing-django-with-ssl/
	note that this is still not very secure if you allow sending session cookies over http
'''

from django.http import HttpResponseRedirect
import settings


'''
	turns a request into a securified redirect
'''
def secure_redirect(request, url = None):
	if url is None:
		url = request.build_absolute_uri(request.get_full_path())
	url = request.build_absolute_uri(url)
	url = url.replace('http://', 'https://')
	if settings.DEBUG:
		url = url.replace(':8000/', ':8443/')
	return HttpResponseRedirect(url)

def desecure_redirect(request, url = None):
	if url is None:
		url = request.get_full_path()
	url = request.build_absolute_uri(url)
	url = url.replace('https://', 'http://')
	if settings.DEBUG:
		url = url.replace(':8443/', ':8000/')
	print url
	return HttpResponseRedirect(url)


'''
	always redirect to https if on http
'''
def redirect_to_secure(view_func):
	def guarantee_secure_view(request, *args, **kwargs):
		if not request.is_secure():
			return secure_redirect(request)
		return view_func(request, *args, **kwargs)
	return guarantee_secure_view


'''
	redirect to https if on http and the settings say so
'''
def conditional_redirect_to_secure(view_func):
	def guarantee_secure_view(request, *args, **kwargs):
		if not request.is_secure():
			if getattr(settings, 'AUTH_REQUIRE_SECURE', False):
				return secure_redirect(request)
		return view_func(request, *args, **kwargs)
	return guarantee_secure_view

secure = conditional_redirect_to_secure


