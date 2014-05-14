
from django.contrib import admin
from muuser.models.address import Address
from django.contrib.admin.options import ModelAdmin


class AddressAdmin(ModelAdmin):
	
	fields = ('street_name', 'street_nr', 'postal_code', 'city', 'country', 'longitude', 'latitude',)
	readonly_fields = ('longitude', 'latitude',)


admin.site.register(Address, AddressAdmin)


