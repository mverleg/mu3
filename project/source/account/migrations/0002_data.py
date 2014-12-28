# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import get_user_model
from django.db import migrations
from sys import stderr
from account.models.user import MyUser


def initial_user(apps, schema_editor):
	user_model_name = MyUser.__name__  # complicated way to make sure an error is raised when user is renamed
	User = apps.get_model('account', user_model_name)  # get the historical version, not the latest one
	INITIAL_EMAIL, INITIAL_PASSWD = 'admin@localhost', 'admin'
	if not User.objects.filter(email = INITIAL_EMAIL):
		get_user_model().objects.create_superuser(email = INITIAL_EMAIL, password = INITIAL_PASSWD).save()
		stderr.write('\n\ncreated initial user \'{0}\' with password \'{1}\'; please change the password a.s.a.p.\n\n'.format(INITIAL_EMAIL, INITIAL_PASSWD))


class Migration(migrations.Migration):

	dependencies = [
		('account', '0001_initial'),
	]

	operations = [
		migrations.RunPython(initial_user),
	]


