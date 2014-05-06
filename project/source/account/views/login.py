
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from account.models import MuUser
from account.forms.login import LoginForm
from django.contrib.auth import authenticate, login as auth_login
from account.functions.next_get import next_GET


'''
	wrapper for django login view
'''
@next_GET
def login(request, next, *args, **kwargs):
	if request.user.is_authenticated():
		return redirect(to = reverse('logout'))
	if request.method == 'POST':
		form = LoginForm(data = request.POST)
		if form.is_valid():
			auth_login(request, form.user)
			return redirect(to = form.cleaned_data['next'])
	else:
		form = LoginForm(initial = {'next': next})
	return render(request, 'login.html', {
		'form': form,
	})


