

from modeltranslation.translator import translator, TranslationOptions
#from models.my_model import MyModel


class MyModelTranslation(TranslationOptions):
	fields = ('name',)
	required_languages = {
		'ne': ('name',),
		'en': ('name',),
		'zh': (),
	}


#translator.register(MyModel, MyModelTranslation)


