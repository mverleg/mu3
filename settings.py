'''
    base settings for mu3-derived projects
'''

from dogpile.cache import make_region  # @UnresolvedImport
from django.conf.global_settings import *  # @UnusedWildImport
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


TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
    'admin_settings.context_processors.admin_settings', 
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
    'crispy_forms',
    'admin_settings',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/account/profile/'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

CRISPY_FAIL_SILENTLY = not DEBUG


