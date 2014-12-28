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
	cp -n $dir/files/gitignore .gitignore;
elif [ -z "$(git commit --dry-run | grep 'nothing to commit')" ];
then
	printf "this directory is already a git repository and has non-committed changes; please commit any changes and consider if you want to create a project in an active git directory\n";
	return;
fi

printf 'adding everything to git\n';
git add -A;
git commit -q -m "initial commit for '$name'";

# create and activate virtual environment
mkdir -p data static media;
if ! [ -d "env" ];
then
	# for python 2 use:
	# virtualenv -q env;
	# for Python3 use:
	virtualenv -q -p /usr/bin/python3.4 env
	ln -s /usr/lib/python3/dist-packages/numpy env/lib/python3.4/site-packages/
	ln -s /usr/lib/python3/dist-packages/scipy env/lib/python3.4/site-packages/
	ln -s /usr/lib/python3/dist-packages/matplotlib env/lib/python3.4/site-packages/
fi
source env/bin/activate;

printf "copying supporting files\n";
rsync -larhH --ignore-existing --exclude=source/* $dir/project/ .;
printf "copying django files\n";
for appdir in $dir/project/source/*
do
    if [ ! -e "source/$(basename $appdir)" ]
    then
        /bin/cp -rnp "$dir/project/source/$(basename $appdir)" "source/$(basename $appdir)"
    fi
done
if [ ! -f source/local.py ];
then
	secret_key=$(python -c 'import random; print("".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)]))');
	sed "s/\[secret_key\]/$secret_key/g" $dir/files/local.py > source/local.py;
fi

if [[ -e "dev/init.sh" ]];
then
	printf "source dev/init.sh\n";
	source dev/init.sh;
fi

if ! [ -d "$name" ];
then
	printf "symlink project name for IDE's\n";
	ln -s source $name;
fi

printf "turning into Eclipse project\n";
printf "...skipped\n";
#sed "s/\[name\]/$name/g" "$dir/files/project_template" > source/.project;
#sed "s/\[name\]/$name/g" "$dir/files/pydevproject_template" > source/.pydevproject;
name_static=$name"_static";
#sed "s/\[name\]/$name_static/g" "$dir/files/project_template" > static/.project;
#sed "s/\[name\]/$name_static/g" "$dir/files/pydevproject_template" > static/.pydevproject;

printf "setting up ssl testing\n";
if [ ! -f dev/ssl/devssl.conf ];
then
	cp -n $dir/files/dev_https_config dev/ssl/devssl.conf;
	openssl genrsa 1024 > dev/ssl/devssl.key;
	openssl req -new -x509 -nodes -sha256 -days 365 -key dev/ssl/devssl.key -batch > dev/ssl/devssl.cert;
	cat dev/ssl/devssl.key dev/ssl/devssl.cert > dev/ssl/devssl.pem;
fi

printf 'adding changes to git\n';
git add -A;
git commit -q -m "directory structure for '$name'";

printf 'installing bower modules for %s\n' "$name";
bower --no-color install -q $(cat ~/mods/PY/mu3/files/bower_list);
if [ -f "dev/bower.json" ];
then
	bower install --no-color -q;
fi
bower_freeze > dev/bower.json;

printf 'installing pip modules for %s\n' "$name";
# pip -q install django six django-dbsettings johnny-cache git+https://bitbucket.org/mverleg/django_admin_settings;
pip -q install $(cat "$dir/files/pip_list");
if [ -f "dev/pip.txt" ];
then
	pip -q install $(cat dev/pip.txt);
fi
pip freeze > dev/pip.txt;

printf 'creating database for %s\n' "$name";
python manage.py syncdb -v0 --noinput;

printf 'adding changes to git\n';
git add -A;
git commit -q -m "other structural files for '$name'";

#todo: make documentation

printf 'adding initial documentation to git\n';
git add -A;
git commit -q -m "other structural files for '$name'";

printf "type 'deactivate' to leave virtualenv\n";



# test-based development
#
# user should add a git remote




