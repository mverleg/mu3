
from django.conf.urls import patterns, url
from base.views.credits import credits
from views.login import login
from views.logout import logout
from views.register import register
from views.profile import profile, profile_submit, profile_password, profile_password_done
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


urlpatterns = patterns('',
    url(r'^$', lambda request: redirect(reverse('profile'))),
    url(r'^login/$', login, name = 'login'),
    url(r'^logout/$', logout, name = 'logout'),
    url(r'^register/$', register, name = 'register'),
    url(r'^profile/$', profile, name = 'profile'),
    url(r'^profile/submit/$', profile_submit, name = 'profile_submit'),
    url(r'^password/$', profile_password, name = 'profile_password'),
    url(r'^password/done/$', profile_password_done, name = 'profile_password_done'),
    
    url(r'^reset/$', password_reset, {'template_name': 'reset_form.html', 'email_template_name': 'reset_email.html'}, name = 'password_reset'),
    url(r'^reset/sent/$', password_reset_done, {'template_name': 'reset_done.html'}, name = 'password_reset_done'),
    url(r'^reset/new/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'reset_confirm.html'}, name = 'password_reset_confirm'),
    url(r'^reset/complete/$', password_reset_complete, {'template_name': 'reset_complete.html'}, name = 'password_reset_complete'),
)


#reset_complete.html  reset_done.html   reset_form.html
#reset_confirm.html     reset_email.html