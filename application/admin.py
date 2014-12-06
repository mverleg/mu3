
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
#from models.my_model import MyModel


class MyModelAdmin(TabbedTranslationAdmin):
#class MyModelAdmin(ModelAdmin):

	fields = ('name',)

#admin.site.register(MyModel, MyModelAdmin)


