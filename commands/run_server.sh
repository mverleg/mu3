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

if [[ -e "init.sh" ]];
then
	printf "source init.sh\n";
	source init.sh;
else
	printf "init.sh not found; skipping\n";
fi

printf 'make sure memcached is running\n  sudo service memcached start;\n';

printf "starting ssl server\n";
stunnel4 dev/ssl/devssl.conf &> /dev/null &
stunnel_pid=$!;
sleep 0.3;
if [ -n "$(ps aux | awk '{print $2 }' | grep "$stunnel_pid")" ];
then
	HTTPS=1 python manage.py runserver 0.0.0.0:8001 --traceback & # the https server
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
	python manage.py runserver 0.0.0.0:8000 --traceback ; # the http server
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



