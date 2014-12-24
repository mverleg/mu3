
from syncdb_completed.signals import syncdb_completed
from .initial_data import initial_data


syncdb_completed.connect(initial_data)


