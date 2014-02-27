# -*- coding: utf-8 -*-

'''
    for installing with pip
'''

from distutils.core import setup
from setuptools import find_packages

setup(
    name='django-mu3',
    version='0.0.1',
    author=u'Mark V',
    author_email='noreply.mail.nl',
    packages=find_packages(),
    include_package_data=True,
    url='https://bitbucket.org/mverleg/mu5/get/tip.tar.gz',
    license='free to use without permission, but only at your own risc',
    description='base for my Django projects',
    zip_safe=False,
    install_requires = [
    	'django',
#    	'django-profiles',
#		'django-uni-forms',
    ],
)
