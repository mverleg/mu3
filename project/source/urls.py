
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.contrib import admin
from haystack.views import SearchView
from misc.views.notification import notification
import smuggler.urls, statix.urls
import account.urls


admin.autodiscover()


#urlpatterns = patterns('',
urlpatterns = i18n_patterns('',
	#url(r'^$', home, name = 'home'),
	url(r'^account/', include(account.urls)),
	url(r'^admin/', include(smuggler.urls)),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^search/', SearchView(template = 'search.html'), name = 'search'),
	url(r'^lang/set/', set_language, name = 'set_language'),
	url(r'^$', notification, {'subject': 'Welcome', 'message': 'This is the default home page. More will probably appear soon!', 'home_button': False}, name = 'home'),
	url(r'^', include(statix.urls)),
)


