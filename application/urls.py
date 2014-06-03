
from views.my_view import my_view
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^my_view/$', my_view, name = 'my_view'),
)


