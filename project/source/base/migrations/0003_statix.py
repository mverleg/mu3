# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import migrations


def initial_pages(apps, schema_editor):
	Page = apps.get_model('statix', 'Page')  # get the historical version, not the latest one
	if not Page.objects.filter(path = 'credits'):
		Page(path = 'credits', title = 'Credits', content = '''
			<h1>Credits</h1>
			<p>This website was made possible by materials from various sources. Gratitude is due for making this project possible! These include, in any orders:</p>
			<ul>
				<li>Python: the server-side language <a href="https://www.python.org/">python.org</a></li>
				<li>Django: the web development framework <a href="https://www.djangoproject.com/">djangoproject.com</a></li>
				<li>jQuery: client-side library for javascript <a href="http://jquery.com/">jquery.com</a></li>
				{# #todo #}
			</ul>
		'''.replace('\t', '')).save()
	if not Page.objects.filter(path = 'contact'):
		Page(path = 'contact', title = 'Contact', content = '''
			{% load ext %}
			<h1>Contact</h1>
			<p>Feel free to contact us; we can be reached in many ways:</p>
			<p>Email: {{ "company@spam.la"|obfuscate }}</p>
			<p>Phone: 06 1234 5678</p>
			<p>Address: etc etc</p>
			<p>Messenger pigeon: on Wednesday, have your pigeon deliver your message in the garden of aforementioned address, if weather allows</p>
		'''.replace('\t', '')).save()
	if not Page.objects.filter(path = 'about'):
		Page(path = 'about', title = 'About', content = '''
			{% load statix_tags %}
			<h1>About</h1>
			<p>We are the best ones!</p>
		'''.replace('\t', '')).save()


class Migration(migrations.Migration):

	dependencies = [
		('base', '0002_settings'),
		('statix', '0001_initial'),
	]

	operations = [
		migrations.RunPython(initial_pages),
	]


