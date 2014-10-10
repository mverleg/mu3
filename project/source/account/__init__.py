
from syncdb_completed.signals import syncdb_completed
from management.initial_data import initial_data


"""
	install initial data when syncdb-ing
"""
syncdb_completed.connect(initial_data)


