'''
	WSGI config.
	
	Created by mu3.
	
	It exposes the WSGI callable as a module-level variable named ``application``.
	
	For more information on this file, see
	https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
'''

from sys import path
from os import environ
from os.path import dirname, abspath, join
from django.core.wsgi import get_wsgi_application

BASE_NAME = dirname(abspath(__file__))
path.append(join(BASE_NAME, 'source'))
path.append(join(BASE_NAME, '/mods/py/incl'))
environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()


