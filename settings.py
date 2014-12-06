
"""
	base settings for mu3-derived projects
"""

from dogpile.cache import make_region
from django.conf.global_settings import *
from os import path
BASE_DIR = path.dirname(path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


mem_cache = make_region().configure(
	'dogpile.cache.pylibmc',
	expiration_time = 150,
	arguments = {
		'url':['127.0.0.1'],
	}
).cache_on_arguments()

HAYSTACK_CONNECTIONS = {
	'default': {
		'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
		'URL': 'http://127.0.0.1:9200/',
		'INDEX_NAME': 'haystack',
	},
}
HAYSTACK_ITERATOR_LOAD_PER_QUERY = HAYSTACK_SEARCH_RESULTS_PER_PAGE = 20
HAYSTACK_LIMIT_TO_REGISTERED_MODELS = True

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	#'django.core.context_processors.i18n',     # LANGAUGES, LANGUAGE_CODE
	#'django.core.context_processors.media',   # MEDIA_URL
	#'django.core.context_processors.static',  # STATIC_URL
	#'django.core.context_processors.tz',      # TIME_ZONE
	'django.core.context_processors.request',
	'admin_settings.context_processors.admin_settings',
	'misc.context.context_settings.context_settings',
	'misc.context.javascript_settings.javascript_settings',
)

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': '%s/data/default.sqlite3' % BASE_DIR,
	}
}

''' path of the site-wide base template, which should contain a {% block content %} '''
BASE_TEMPLATE = 'mu3_base.html'

TEMPLATE_LOADERS = (
	'django.template.loaders.app_directories.Loader',
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'misc',
	'crispy_forms',
	'admin_settings',
	'muuser',
	'smuggler',
	'haystack',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
	'misc.middleware.secure.RequireSecureMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

# johhny database cache does not work in Django 1.6 yet, turn this on when it does
"""
if False:
	MIDDLEWARE_CLASSES = (
		'johnny.middleware.LocalStoreClearMiddleware',
		'johnny.middleware.QueryCacheMiddleware',
	) + MIDDLEWARE_CLASSES

	CACHES = {
		'default' : dict(
			 BACKEND = 'johnny.backends.memcached.MemcachedCache',
			 LOCATION = ['127.0.0.1:11211'],
			 JOHNNY_CACHE = True,
		)
	}

	JOHNNY_MIDDLEWARE_KEY_PREFIX = 'jc_admin_settings' # automatically
"""

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True

TIME_ZONE = 'UTC'
USE_TZ = True

DATETIME_INPUT_FORMATS = ('%Y-%m-%d %H:%M',) + DATETIME_INPUT_FORMATS
DATE_INPUT_FORMATS = ('%Y-%m-%d',) + DATE_INPUT_FORMATS
TIME_INPUT_FORMATS = ('%H:%M',) + TIME_INPUT_FORMATS

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/account/profile/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CRISPY_FAIL_SILENTLY = not DEBUG

PREPEND_WWW = True
APPEND_SLASH = True

SESSION_COOKIE_NAME = 'session'
CSRF_COOKIE_NAME = 'csrf'

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

NOSCR_ALLOWED_TAGS = 'p:title h1:title h2:title h3:title div:title span:title a:href:title img:src:alt:title table:cellspacing:cellpadding tbody th tr td:title:colspan:rowspan ol ul li:title br'

USE_CDN = False

SESSION_COOKIE_SECURE = False
AUTH_REQUIRE_SECURE = False
DESECURE_AFTER_LOGOUT = False
REQUIRE_SECURE_PATHS = [
	'/admin/',
	'/account/',
]

SMUGGLER_EXCLUDE_LIST = ['sessions.Session',]
SMUGGLER_INDENT = None

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

#PREFIX_DEFAULT_LOCALE = True
#LOCALEURL_USE_ACCEPT_LANGUAGE = True
#LOCALE_REDIRECT_PERMANENT = False


