#!/bin/bash

##
## run test server on localhost :8000, including https version
## and virtual environment
##

dir="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))";

if ! [[ $_ != $0 ]];
then
	printf "this file needs to be sourced rather than executed ('source name.sh')\n";
	exit;
fi

if ! [ -d "env" ];
then
	printf "environment not found\n";
	return;
fi

# try to kill stunnel and python using these ports
kill $(ps | grep "stunnel" | awk "{print $1}") &> /dev/null;
kill $(lsof -t -i:8000) 2>/dev/null;
kill $(lsof -t -i:8001) 2>/dev/null;
kill $(lsof -t -i:8443) 2>/dev/null;

printf 'activating virtual environment\n';
source ./env/bin/activate;

if [[ -e "dev/init.sh" ]];
then
	printf "source dev/init.sh\n";
	source dev/init.sh;
else
	printf "init.sh not found; skipping\n";
fi

for service in 'memcached' 'elasticsearch';
do
	if [[ $(service $service status) =~ 'is not running' ]];
	then
		if [ "$(id -u)" != "0" ];
		then
			printf 'SERVICE %s NOT RUNNING!\n superuser can start it like this:\n sudo service memchached start\n' $service;
		else
			printf 'starting memcached (sudo)...\n';
			sudo service $service start;
		fi
	else
		printf '%s is already running\n' $service;
	fi
done

printf "starting ssl server\n";
stunnel4 dev/ssl/devssl.conf &> /dev/null || return &
stunnel_pid=$!;
sleep 0.3;
if [ -n "$(ps aux | awk '{print $2 }' | grep "$stunnel_pid")" ];
then
	HTTPS=1 python manage.py runserver 0.0.0.0:8001 --traceback || return & # the https server
	printf " for https use post :8443 (NOT 8001)\n";
	https_pid=$!;
else
	printf "\nSTUNNEL4 TERMINATED; ONLY HTTP SERVER STARTING (NOT HTTPS)\n\n";
	return;
fi
# don't start http server if https failed
sleep 0.7;
if [[ ! -n "$(ps aux | awk '{print $2 }' | grep "$stunnel_pid")" || -n "$(ps aux | awk '{print $2 }' | grep "$https_pid")" ]];
then
	printf "starting http server\n";
	python manage.py runserver 0.0.0.0:8000 --traceback # the http server
	printf " stopping\n";
else
	printf "http server not starting because https failed\n";
fi

printf "killing background processes\n";
# try to kill the started background processes
kill $(ps | grep "stunnel" | awk "{print $1}") &> /dev/null;
kill $(lsof -t -i:8000) 2>/dev/null;
kill $(lsof -t -i:8001) 2>/dev/null;
kill $(lsof -t -i:8443) 2>/dev/null;

#printf "deactivating virtual environment\n";
#deactivate;



