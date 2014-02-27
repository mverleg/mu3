#!/bin/bash

## 
## run test server on localhost :8000, including https version
## and virtual environment
## 

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

printf 'activating virtual environment; type "deactivate" to stop\n';
source ./env/bin/activate;


