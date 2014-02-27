#!/usr/bin/env python
'''
    Run management commands.
    
    Created by mu3.
'''

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'source.settings')

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)


