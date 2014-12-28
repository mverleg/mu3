# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations
from admin_settings import Setting as LatestSetting


def initial_settings(apps, schema_editor):
	Setting = apps.get_model('admin_settings', 'Setting')  # get the historical version, not the latest one
	if not Setting.objects.filter(name = 'TITLE_BASE'):
		Setting(name = 'TITLE_BASE', value_str = '(change in admin)', explanation = 'the base part of the title of pages', type = LatestSetting.STR, template = 2).save()
		Setting(name = 'TITLE_SEPARATOR', value_str = '&laquo;', explanation = 'the base part of the title of pages', type = LatestSetting.STR, template = 2).save()


class Migration(migrations.Migration):

	dependencies = [
		('base', '0001_initial'),
		('admin_settings', '0002_data'),
	]

	operations = [
		migrations.RunPython(initial_settings),
	]


