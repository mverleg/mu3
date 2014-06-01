
from django.contrib import admin
from django.contrib.admin import ModelAdmin
#from models.my_model import MyModel


class MyModelAdmin(ModelAdmin):
	
	fields = ('name',)

#admin.site.register(MyModel, MyModelAdmin)


