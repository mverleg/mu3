
from misc.signals.daily import daily
from misc.signals.hourly import hourly
from syncdb_completed import syncdb_completed
from initial_data import initial_data
from timing import run_hourly, run_daily


'''
	install initial data when syncdb-ing
'''
syncdb_completed.connect(initial_data)


'''
	connect timing signals
'''
hourly.connect(run_hourly)
daily.connect(run_daily)


