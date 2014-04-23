
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


'''
    custom user model
'''
class MuUser(AbstractUser):
    
    objects = UserManager()
    
    def __unicode__(self):
        return self.get_full_name()
    
    def get_full_name(self):
        if self.first_name or self.last_name:
            return super(MuUser, self).get_full_name()
        else:
            return self.username
    
    class Meta:
        app_label = 'account'
        verbose_name = 'user'
        verbose_name_plural = 'users'


