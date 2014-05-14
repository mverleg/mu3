
from django.contrib import admin
from account.models.user import MyUser
from muuser.admin.user import MuUserAdmin


class MyUserAdmin(MuUserAdmin):
	
	fieldsets = MuUserAdmin.fieldsets
	fieldsets.insert(2, ['Address', {'fields': ['address']}])
	
	class Meta:
		model = MyUser


admin.site.register(MyUser, MyUserAdmin)


