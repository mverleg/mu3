
'''
    create initial data for this model, on syncdb
    make sure to check if it doesn't yet exist
'''

from account.models import MuUser


INITIAL_USER = 'admin'

def initial_data(*args, **kwargs):
    '''
        create an admin user
    '''
    if not MuUser.objects.filter(username = INITIAL_USER):
        first_user = MuUser(username = INITIAL_USER, is_staff = True, is_superuser = True)
        first_user.set_password('admin')
        first_user.save()
        print 'created initual user \'%s\'; please change password a.s.a.p.' % INITIAL_USER


