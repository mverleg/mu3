
'''
	create initial data for this model, on syncdb
	make sure to check if it doesn't yet exist
'''

from admin_settings import Setting
from admin_settings.type_functions import STR, TEMPL


INITIAL_USER = u'mark.verleg@gmail.com'

def initial_data(*args, **kwargs):
	'''
		initialize display parameters (as settings)
	'''
	if not Setting.objects.filter(name = 'TITLE_BASE'):
		Setting(name = u'TITLE_BASE', value = u'(change in admin)', explanation = u'the base part of the title of pages', type = STR, template = 2).save()
		Setting(name = u'TITLE_SEPARATOR', value = u'&laquo;', explanation = u'the base part of the title of pages', type = STR, template = 2).save()
		print u'created display settings'
	'''
		initialize pages (as settings)
	'''
	if not Setting.objects.filter(name = 'CREDITS_PAGE'):
		Setting(name = u'CREDITS_PAGE', value = u'''
			<p>This website was made possible by material from various sources. Gratitude is due for making this project possible! These include, in any order:</p>
			<ul>
				<li>Python: the server-side language <a href="https://www.python.org/">python.org</a></li>
				<li>Django: the web development framework <a href="https://www.djangoproject.com/">djangoproject.com</a></li>
				<li>jQuery: client-side library for javascript <a href="http://jquery.com/">jquery.com</a></li>
			</ul>
		''', explanation = u'the credits for the site, as displayed on the credits page (see also CREDITS_PAGE_SUBJECT)', type = TEMPL, template = 2).save()
		Setting(name = u'CREDITS_PAGE_SUBJECT', value = u'''Gratitute to ...''', explanation = u'the header for the credits page', type = TEMPL, template = 1).save()
		print u'created credits page'
	
	if not Setting.objects.filter(name = 'CONTACT_PAGE'):
		Setting(name = u'CONTACT_PAGE', value = u'''
			{% load misc %}
			<p>Feel free to contact us; we can be reached in many ways:</p>
			<p>Email: {{ "company@spam.la"|obfuscate }}</p>
			<p>Phone: 06 1234 5678</p>
			<p>Address: etc etc</p>
			<p>Messenger pigeon: on Wednesday, have your pigeon deliver your message in the garden of aforementioned address, if weather allows</p>
		''', explanation = u'the contact details, as displayed on the contact page (see also CONTACT_PAGE_SUBJECT)', type = TEMPL, template = 2).save()
		Setting(name = u'CONTACT_PAGE_SUBJECT', value = u'''Contact us''', explanation = u'the header for the contact page', type = TEMPL, template = 1).save()
		print u'created contact page'


