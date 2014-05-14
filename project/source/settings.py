
'''
	specific settings for your project;
	always extend existing lists
'''

from mu3.settings import *
from local import *
from os import path


BASE_DIR = path.dirname(path.dirname(__file__))

''' path of the site-wide base template, which should contain a {% block content %} '''
BASE_TEMPLATE = 'base.html'
BASE_EMAIL_TEMPLATE = 'base_email.html'

AUTH_USER_MODEL = 'account.MyUser'

INSTALLED_APPS += (
	'base',
	'account',
	
	'django.contrib.admin',
)

MEDIA_ROOT = path.join(BASE_DIR, 'data')

TEMPLATE_CONTEXT_PROCESSORS += (
	'base.context.context_settings.context_settings',
)

EMAIL_HOST = 'smtp.mail.google.com'
EMAIL_HOST_USER = 'markdjangosmtptest424'
EMAIL_HOST_PASSWORD = 'ta7hbjv4762F'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

SITE_URL = 'markv.nl'

ALLOWED_HOSTS = ['.%s' % SITE_URL]

DEBUG = True


