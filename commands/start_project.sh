#!/bin/bash

## 
## create a Django project in the current directory which has the
## name of said directory, including virtualenv, git, base apps etc
## 

name=${PWD##*/};

if ! [[ $_ != $0 ]];
then
	printf "this file needs to be sourced rather than executed ('source name.sh')\n";
	exit;
fi

if ! [ -d ".git" ];
then
	printf "creating git repository and making initial commit\n";
	git init;
fi

git add -A;
git commit -m "initial commit for '$name'";

if ! [ -d "env" ];
then
	virtualenv env;
	source ./env/bin/activate;
fi

pip install https://bitbucket.org/mverleg/mu3/get/tip.tar.gz;





printf 'creating Django project %s\n' "$name"




# create new secret key
