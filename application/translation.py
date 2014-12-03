

from modeltranslation.translator import translator, TranslationOptions
#from models.my_model import MyModel


class MyModelTranslation(TranslationOptions):
	fields = ('name', 'text',)
	required_languages = {
		'ne': ('name', 'text'),
		'en': ('name',),
		'zh': ('name',),
	}


#translator.register(MyModel, MyModelTranslation)


