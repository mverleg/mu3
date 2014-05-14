
from django.conf.urls import patterns, include, url
from django.contrib import admin
import base.urls, account.urls
admin.autodiscover()


urlpatterns = patterns('',
	#url(r'^$', home, name = 'home'),
	url(r'^account/', include(account.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^', include(base.urls)),
)

