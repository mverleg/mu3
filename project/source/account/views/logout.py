
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from account.models import MuUser
from account.forms.logout import LogoutForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from base.views.notification import notification
from django.contrib.auth import logout as auth_logout
from account.functions.next_get import next_GET


'''
	logs out user through a form (to prevent csrf)
	#todo: redirect url
'''
@next_GET
def logout(request, next):
	if not request.user.is_authenticated():
		return redirect(to = reverse('login'))
	if request.method == 'POST':
		form = LogoutForm(data = request.POST)
		if form.is_valid():
			auth_logout(request)
			return redirect(to = form.cleaned_data['next'])
	else:
		form = LogoutForm(initial = {'next': next})
	return render(request, 'logout.html', {
		'form': form,
	})


