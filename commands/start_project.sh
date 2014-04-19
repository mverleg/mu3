#!/bin/bash

## 
## create a Django project in the current directory which has the
## name of said directory, including virtualenv, git, base apps etc
## 

name=${PWD##*/};
dir="$( dirname $( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd ))";

chmod -x "${BASH_SOURCE[0]}";

# check if we can activate virtualenv
if ! [[ $_ != $0 ]];
then
	printf "this file needs to be sourced rather than executed ('source name.sh')\n";
	exit;
fi

# check if the correct dpkg packages are installed
packages=$(cat "$dir/files/apt_get_list");
missing="";
for package in $packages;
do
	if ! dpkg -L $package &> /dev/null;
	then
		printf "package '$package' is not installed\n";
		missing+=" $package";
	fi
done
if [ ! -z "$missing" ];
then
	printf "a superuser can install these missing packages by running\nsudo apt-get install$missing\n"
	return;
fi

# create a git repository only if needed
if ! [ -d ".git" ];
then
	printf "creating git repository and making initial commit\n";
	git init;
	cp $dir/files/gitignore .gitignore;
elif [ -z "$(git commit --dry-run | grep 'nothing to commit')" ];
then
	printf "this directory is already a git repository and has non-committed changes; please commit any changes and consider if you want to create a project in an active git directory\n";
	return;
fi

printf 'adding everything to git\n';
git add -A;
git commit -m "initial commit for '$name'";

# create and activate virtual environment
if ! [ -d "env" ];
then
	virtualenv env;
fi
source env/bin/activate;

# install the mu3 base project for this virtualenv
# pip install git+https://bitbucket.org/mverleg/mu3;
#echo "USING LOCAL DIR FOR TESTING PURPOSES";
pip install ~/mu3 1> /dev/null;

printf "copying initial project files\n";
rsync -arhH --ignore-existing $dir/project/ .;
if [ ! -f source/local.py ];
then
	secret_key=$(python -c 'import random; print "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])');
	echo $secret_key
	sed "s/\[secret_key\]/$secret_key/g" $dir/files/local.py > source/local.py;
	chmod 600 source/local.py;
fi

printf "turning into Eclipse project\n";
sed "s/\[name\]/$name/g" "$dir/files/project_template" > source/.project;
sed "s/\[name\]/$name/g" "$dir/files/pydevproject_template" > source/.pydevproject;
name_static=$name"_static";
sed "s/\[name\]/$name_static/g" "$dir/files/project_template" > static/.project;
sed "s/\[name\]/$name_static/g" "$dir/files/pydevproject_template" > static/.pydevproject;

printf "setting up ssl testing\n";
if [ ! -f dev/ssl/devssl.conf ];
then
	cp $dir/files/dev_https_config dev/ssl/devssl.conf;
	openssl genrsa 1024 > dev/ssl/devssl.key;
	openssl req -new -x509 -nodes -sha256 -days 365 -key dev/ssl/devssl.key -batch > dev/ssl/devssl.cert;
	cat dev/ssl/devssl.key dev/ssl/devssl.cert > dev/ssl/devssl.pem;
fi

printf 'adding changes to git\n';
git add -A;
git commit -m "directory structure for '$name'";

printf 'installing modules for %s\n' "$name";
#pip install django six django-dbsettings johnny-cache git+https://bitbucket.org/mverleg/django_admin_settings;
pip install $(cat "$dir/files/pip_list") 1> /dev/null;
if [ -f "dev/modules.pip" ];
then
	pip install $(cat dev/modules.pip) 1> /dev/null;
else
	pip freeze > dev/modules.pip;
fi
pip install git+https://bitbucket.org/mverleg/django_admin_settings;

printf 'creating Django project %s\n' "$name";
python manage.py syncdb --noinput;

printf 'adding changes to git\n';
git add -A;
git commit -m "other structural files for '$name'";

printf "type 'deactivate' to leave virtualenv\n";



# test-based development
# 
# user should add a git remote




