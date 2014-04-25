
from django.conf.urls import patterns, url
from base.views.credits import credits
from views.login import login
from views.logout import logout
from views.register import register
from views.profile import profile, profile_submit, profile_password, profile_password_done
from django.contrib.auth.views import password_change, password_change_done, password_reset, \
    password_reset_done, password_reset_confirm, password_reset_complete
from forms.login import LoginForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


urlpatterns = patterns('',
    url(r'^login/$', login, {'template_name': 'login.html', 'authentication_form': LoginForm, }, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^register/$', register, name = 'register'),
    url(r'^profile/$', profile, name = 'profile'),
    url(r'^profile/submit/$', profile_submit, name = 'profile_submit'),
    url(r'^password/$', profile_password, name = 'profile_password'),
    url(r'^password/done/$', profile_password_done, name = 'profile_password_done'),
    url(r'^$', lambda request: redirect(reverse('profile'))),
    
    url(r'^password_change/$', password_change, name = 'password_change'),
    url(r'^password_change/done/$', password_change_done, name = 'password_change_done'),
    url(r'^password_reset/$', password_reset, name = 'password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),
)


