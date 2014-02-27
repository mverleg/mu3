'''
    WSGI config.
    
    Created by mu3.
    
    It exposes the WSGI callable as a module-level variable named ``application``.
    
    For more information on this file, see
    https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
'''

import os, sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'source.settings')
sys.path.append('/home/mark') # mu3 dir

application = get_wsgi_application()


