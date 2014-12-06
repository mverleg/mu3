
"""
	specific settings for your project;
	always extend existing lists
"""

from mu3.settings import *
from local import *
from os import path
from django.utils.translation import ugettext_lazy as _


BASE_DIR = path.dirname(path.dirname(__file__))

""" path of the site-wide base template, which should contain a {% block content %} """
BASE_TEMPLATE = 'base.html'
BASE_EMAIL_TEMPLATE = 'base_email.html'

AUTH_USER_MODEL = 'account.MyUser'

INSTALLED_APPS += (
	'base',
	'account',
	'reactables',
	'statix',
	'modeltranslation',
	'django.contrib.admin',
)

TEMPLATE_CONTEXT_PROCESSORS += (
	'django.core.context_processors.i18n',     # LANGAUGES, LANGUAGE_CODE
	'base.context.context_settings.context_settings',
	'base.context.javascript_settings.javascript_settings',
)

MEDIA_ROOT = path.join(BASE_DIR, 'media')
STATIC_ROOT = path.join(BASE_DIR, 'static')

STATIX_URL = '/'

STATICFILES_DIRS += (
	path.join(BASE_DIR, 'env/bower'),
)

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'mdilligaf'
EMAIL_HOST_PASSWORD = 'froink42'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

LANGUAGES = (
	('en', _('English')),
	('ne', _('Dutch')),
	#('zh', _('Mandarin')),  # using Simplified Chinese
)


