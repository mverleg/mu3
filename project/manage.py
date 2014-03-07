#!/usr/bin/env python
'''
    Run management commands.
    
    Created by mu3.
'''

import sys
from os import path, environ
from django.core.management import execute_from_command_line

sys.path.append(path.join(path.dirname(path.abspath(__file__)), 'source'))
sys.path.append('/home/mark') #TMP: when installed with PIP, mu3 should be known
environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

if __name__ == "__main__":
    execute_from_command_line(sys.argv)


