
from django.db import models
from muuser.models.user import MuUser
from muuser.models.address import Address


class MyUser(MuUser):
	
	address = models.ForeignKey(Address, blank = True, null = True)
	
	class Meta:
		app_label = 'account'
		verbose_name = 'user'
		verbose_name_plural = 'users'


