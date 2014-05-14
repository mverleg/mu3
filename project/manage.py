#!/usr/bin/env python
'''
	Run management commands.
	
	Created by mu3.
'''

import sys
from os import path, environ
from django.core.management import execute_from_command_line

sys.path.append(path.join(path.dirname(path.abspath(__file__)), 'source'))
environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if __name__ == "__main__":
	execute_from_command_line(sys.argv)


