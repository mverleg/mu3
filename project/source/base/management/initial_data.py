
'''
    create initial data for this model, on syncdb
    make sure to check if it doesn't yet exist
'''

from account.models.user import MuUser
from admin_settings import Setting


INITIAL_USER = 'mark.verleg@gmail.com'

def initial_data(*args, **kwargs):
    '''
        initialize display parameters (as settings)
    '''
    if not Setting.objects.filter(name = 'TITLE_BASE'):
        Setting(name = 'TITLE_BASE', value = '(change in admin)', explanation = 'the base part of the title of pages', template = 2).save()
        Setting(name = 'TITLE_SEPARATOR', value = '&laquo;', explanation = 'the base part of the title of pages', template = 2).save()
        print 'created display settings'
    '''
        initialize pages (as settings)
    '''
    if not Setting.objects.filter(name = 'CREDITS_PAGE'):
        Setting(name = 'CREDITS_PAGE', value = '''
            <p>This website was made possible by material from various sources. Gratitude is due for making this project possible! These include, in any order:</p>
            <ul>
                <li>Python: the server-side language <a href="https://www.python.org/">python.org</a></li>
                <li>Django: the web development framework <a href="https://www.djangoproject.com/">djangoproject.com</a></li>
                <li>jQuery: client-side library for javascript <a href="http://jquery.com/">jquery.com</a></li>
            </ul>
        ''', explanation = 'the credits for the site, as displayed on the credits page (see also CREDITS_PAGE_SUBJECT)', template = 2).save()
        Setting(name = 'CREDITS_PAGE_SUBJECT', value = '''Gratitute to ...''', explanation = 'the header for the credits page', template = 1).save()
        print 'created credits page'
    
    if not Setting.objects.filter(name = 'CONTACT_PAGE'):
        Setting(name = 'CONTACT_PAGE', value = '''
            <p>Feel free to contact us; we can be reached in many ways:</p>
            <p>Email: {{ "company@spam.la|obfuscate }}</p>
            <p>Phone: 06 1234 5678</p>
            <p>Address: etc etc</p>
            <p>Messenger pigeon: on Wednesday, have your pigeon deliver your message in the garden of aforementioned address, if weather allows</p>
        ''', explanation = 'the contact details, as displayed on the contact page (see also CONTACT_PAGE_SUBJECT)', template = 2).save()
        Setting(name = 'CONTACT_PAGE_SUBJECT', value = '''Contact us''', explanation = 'the header for the contact page', template = 1).save()
        print 'created contact page'


