#!/bin/bash

## 
## create a Django app with the given name
## 

dir="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))";

if [ -z "$1" ];
then
	printf "provide an app name\n";
	return;
fi;

if [ -d "source/$1" ];
then
	printf "'$1' already exists\n";
	return;
fi;

printf "creating app '$1'\n";

/bin/cp -r $dir/application source/$1;

printf "don't forget to add it to INSTALLED_APPS\n";


