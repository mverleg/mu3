
from django.conf.urls import patterns, include, url
from django.contrib import admin
import testapp.urls
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^credits/$', credits, name = 'credits'),
)

