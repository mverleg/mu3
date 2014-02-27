# -*- coding: utf-8 -*-

'''
    for installing with pip
'''

from distutils.core import setup
from setuptools import find_packages

setup(
    name='mu3',
    version='0.0.1',
    author=u'Mark V',
    author_email='noreply.mail.nl',
    packages=find_packages(),
    include_package_data=True,
    url='git+https://bitbucket.org/mverleg/mu3',
    license='free to use without permission, but only at your own risc',
    description='base for my Django projects',
    zip_safe=False,
    install_requires = [
    	'django',
    	'django-reversion',
#    	'django-profiles',
#		'django-uni-forms',
    ],
)
