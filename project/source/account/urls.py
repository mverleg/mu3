
from views.my_view import my_view
from django.conf.urls import patterns, url
from base.views.credits import credits


urlpatterns = patterns('',
    url(r'^my_view/$', my_view, name = 'my_view'),
)


