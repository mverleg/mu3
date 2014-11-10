#!/bin/sh

printf 'creating database for %s\n' "$name";
python manage.py syncdb -v0 --noinput;

printf 'setting permissions\n';
chmod 750 source -R;
chmod 750 static -R;
chmod 770 data -R;

printf '\nChecklist for release:\n'
printf ' - Unit tests pass\n'
printf ' - Build documentation and README\n'
printf ' - Update CHANGELOG and TODO\n'
printf ' - Update version numbers:\n   - doc/conf.py\n'
printf ' - Move code to git master branch\n'
printf ' - Update template for local settings\n'
printf ' - Make sure pip, bower, aptitude freezes are up-to-date'

printf '\nChecklist for deployment:\n'
printf ' - Make sure cron is set up to call manage.py hourly and manage.py daily\n';
printf ' - Update the search index: python manage.py update_index\n'
# check if the default name for sites-enabled is set
printf '\n'

if [ ! -f 'LICENSE.txt' ]
then
	printf 'Warning! Your project has no LICENSE.txt! (see dev/package/)\n';
fi

if test -z "$(find . -maxdepth 1 -name 'README*' -print -quit)"
then
	printf 'Warning! Your project has no README file! (see dev/package/)\n';
fi


