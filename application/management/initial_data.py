
'''
    create initial data for this model, on syncdb
    make sure to check if it doesn't yet exist
    (the signal is connected in management.__init__.py)
'''


def initial_data(verbosity, *args, **kwargs):
    '''
        create an admin user
    '''
    """
    if not MuUser.objects.filter(username = INITIAL_USER):
        first_user = MuUser(username = INITIAL_USER, is_staff = True, is_superuser = True)
        first_user.set_password('admin')
        first_user.save()
        if verbosity:
            print 'created initual user \'%s\'; please change password a.s.a.p.' % INITIAL_USER
    """



