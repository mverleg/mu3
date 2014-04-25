
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from account.models import MuUser
from account.forms.register import RegistrationForm


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
			return redirect(to = reverse('profile'))
	return render(request, 'register.html', {
		'form': form,
	})


