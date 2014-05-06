
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from account.models import MuUser
from account.forms.register import RegistrationForm
from base.views.notification import notification


'''
	wrapper for django login view
'''
def register(request, *args, **kwargs):
	if request.user.is_authenticated():
		return redirect(to = reverse('logout'))
	form = RegistrationForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			user = form.save()
			user = authenticate(username = user.email, password = form.cleaned_data['password'])
			login(request, user)
			return notification(request, message = 'Your account %s has been created! Welcome to the site!' % user.email, subject = 'Welcome, %s' % user, next = reverse('profile'))
	return render(request, 'register.html', {
		'form': form,
	})


