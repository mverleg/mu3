#!/bin/sh

printf 'creating database for %s\n' "$name";
python manage.py syncdb -v0 --noinput;

printf 'setting permissions\n';
chmod 750 source -R;
chmod 750 static -R;
chmod 770 data -R;

printf 'MAKE SURE CRON IS SET UP TO CALL manage.py hourly AND manage.py daily\n';

# check if the default name for sites-enabled is set

# check if apache is running

# update search index


