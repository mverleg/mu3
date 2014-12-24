
"""
	Logging in and out, changing personal information, password reset, etc.
"""

from syncdb_completed.signals import syncdb_completed
from .management.initial_data import initial_data


syncdb_completed.connect(initial_data)


