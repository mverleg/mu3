
'''
	callback to change form widgets for datetime objects
	class MyForm(ModelForm):
		formfield_callback = datetimefield
'''

from django.db import models


def datetimefield(modelfield):
	formfield = modelfield.formfield()
	if isinstance(modelfield, models.DateTimeField):
		#formfield.widget.format = '%m/%d/%Y'
		formfield.widget.attrs.update({'class': 'date-time-picker'})
	elif isinstance(modelfield, models.DateField):
		formfield.widget.attrs.update({'class': 'date-picker'}) 
	elif isinstance(modelfield, models.TimeField):
		formfield.widget.attrs.update({'class': 'time-picker'})
	return formfield


#class SomeForm(forms.ModelForm)
#formfield_callback = datetimefield
