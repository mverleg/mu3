
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from account.models import MuUser
from django.contrib.auth.views import login as django_login


'''
	wrapper for django login view
	#todo: redirect url?
'''
def login(request, *args, **kwargs):
	if request.user.is_authenticated():
		return redirect(to = reverse('logout'))
	return django_login(request, *args, **kwargs)


