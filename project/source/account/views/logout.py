
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from account.models import MuUser
from account.forms.logout import LogoutForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from base.views.notification import notification
from django.contrib.auth import logout as logout_request


'''
	logs out user through a form (to prevent csrf)
	#todo: redirect url
'''
def logout(request):
	if not request.user.is_authenticated():
		return redirect(to = reverse('login'))
	form = LogoutForm(request)
	if request.method == 'POST':
		if 'logout' in request.POST:
			logout_request(request)
			return redirect(to = reverse('login'))
		else:
			raise Exception('That\'s not the logout form')
	else:
		return render(request, 'logout.html', {
			'form': form,
		})


