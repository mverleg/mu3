
from django.contrib import admin
from account.models.user import MyUser
from muuser.admin.user import MuUserAdmin
from muuser.admin.address import ADDRESS_FIELDSET, ADDRESS_READONLY_FIELDS
from muuser.models.address import MuAddress
from django.contrib.admin.options import ModelAdmin


class MyUserAdmin(MuUserAdmin):

	fieldsets = MuUserAdmin.fieldsets
	fieldsets.insert(2, ['Address', {'fields': ADDRESS_FIELDSET}])
	readonly_fields = MuUserAdmin.readonly_fields# + ADDRESS_READONLY_FIELDS


class AddressAdmin(ModelAdmin):

	fields = ('street_name', 'street_nr', 'postal_code', 'city', 'country', 'longitude', 'latitude',)
	readonly_fields = ('longitude', 'latitude',)

	class Meta:
		model = MuAddress


admin.site.register(MyUser, MyUserAdmin)
#admin.site.register(AddressAdmin)


