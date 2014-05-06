
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from account.models import MuUser
from account.forms.register import RegistrationForm
from base.views.notification import notification
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login_required
from django.views.decorators.http import require_GET, require_POST
from account.forms.profile import ProfileForm
from account.forms.password import PasswordForm
from base.views.notification import notification


'''
	request a password reset email
'''
def reset_request(request, *args, **kwargs):
	if request.user.is_authenticated():
		return render(request, 'reset_logged_in.html', {})
	"""
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
	"""

'''
	password reset email has been sent
'''
def reset_sent(request, *args, **kwargs):
	return 


url(r'^reset/$', password_reset, {'template_name': 'reset_form.html', 'email_template_name': 'reset_email.html'}, name = 'password_reset'),
url(r'^reset/sent/$', password_reset_done, {'template_name': 'reset_done.html'}, name = 'password_reset_done'),
url(r'^reset/new/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'reset_confirm.html'}, name = 'password_reset_confirm'),
url(r'^reset/complete/$', password_reset_complete, {'template_name': 'reset_complete.html'}, name = 'password_reset_complete'),






'''
	wrapper for django login view
'''
@require_GET
@login_required
def profile(request, *args, **kwargs):
	form_profile = ProfileForm(request.POST or None, instance = request.user)
	form_password = PasswordForm(request.user, request.POST or None)
	return render(request, 'profile.html', {
		'form_profile': form_profile,
		'form_password': form_password,
	})


@require_POST
@login_required
def profile_submit(request, *args, **kwargs):
	form_profile = ProfileForm(request.POST, instance = request.user)
	if form_profile.is_valid():
		form_profile.save()
		return redirect(to = reverse('profile'))
	return render(request, 'profile.html', {
		'form_profile': form_profile,
	})


@require_POST
@login_required
def profile_password(request, *args, **kwargs):
	form_password = PasswordForm(request.user, request.POST)
	if form_password.is_valid():
		form_password.save()
		return redirect(to = reverse('profile_password_done'))
	else:
		print 'invalid'
	return render(request, 'profile.html', {
		'form_password': form_password,
	})


@login_required
def profile_password_done(request, *args, **kwargs):
	return notification(request, message = 'Your password has been changed!', subject = 'Password changed', next = reverse('profile'))


