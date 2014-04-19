
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    #url(r'^$', my_view, name = 'my_view'),
    #url(r'^appname/', include(app.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

