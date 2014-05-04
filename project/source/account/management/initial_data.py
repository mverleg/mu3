
'''
    create initial data for this model, on syncdb
    make sure to check if it doesn't yet exist
'''

from account.models.user import MuUser
from admin_settings import Setting


INITIAL_USER = 'mark.verleg@gmail.com'

def initial_data(*args, **kwargs):
    '''
        create an admin user
    '''
    if not MuUser.objects.filter(email = INITIAL_USER):
        first_user = MuUser.objects.create_superuser(email = INITIAL_USER, password = 'admin')
        first_user.set_password('admin')
        first_user.save()
        print 'created initual user \'%s\'; please change password a.s.a.p.' % INITIAL_USER
    
    '''
        initialize user setting(s)
    '''
    if not Setting.objects.filter(name = 'DEFAULT_COUNTRY'):
        Setting(name = 'DEFAULT_COUNTRY', value = 'Netherlands').save()
        print 'created user settings'
    
    


