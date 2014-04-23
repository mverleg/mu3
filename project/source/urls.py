
from django.conf.urls import patterns, include, url
from django.contrib import admin
import base.urls
admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^$', my_view, name = 'my_view'),
    #url(r'^appname/', include(a[[.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^', include(base.urls)),
)

