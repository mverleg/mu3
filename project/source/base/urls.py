
from django.conf.urls import patterns, include, url
from django.contrib import admin
from base.views.notification import notification
from base.views.setting_flatpage import setting_flatpage
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', notification, {'subject': 'Welcome', 'message': 'This is the default home page. More will probably appear soon!', 'home_button': False}, name = 'home'),
    url(r'^credits/$', setting_flatpage, {'setting': 'CREDITS_PAGE'}, name = 'credits'),
    url(r'^contact/$', setting_flatpage, {'setting': 'CONTACT_PAGE'}, name = 'contact'),
)

