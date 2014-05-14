
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.core.urlresolvers import reverse


'''
	the default actions already implemented, but not overriding __init__ so that you
	can add more actions (actually a generator, not a class)
'''
def BaseFormHelper(url_name = None, submit_name = 'submit', back = '', back_name = 'back', submit_css = '', back_css = 'btn_danger'):
	helper = FormHelper()
	if url_name:
		helper.form_action = reverse(url_name)
	if back:
		helper.add_input(Button('back', back_name, onclick = 'location.href=\'%s\'' % back, css_class = back_css))
	''' it is not advisable to use 'submit' or 'post' as input names, because jquery gets confused  '''
	helper.add_input(Submit('go', submit_name, css_class = submit_css))
	return helper


'''
	a simply form (like 80%) with just an action and a submit button (possibly a back button)		
'''
class SimpleCrispyModelForm(ModelForm):
	
	URL_NAME = None
	SUBMIT_NAME = 'submit'
	SUBMIT_CSS = '' #'btn-warning btn-xs'
	BACK = ''
	BACK_NAME = 'back'
	BACK_CSS = 'btn-danger'
	
	def __init__(self, data = None, url_name = None, submit_name = None, back = None, back_name = None, submit_css = None, back_css = None, *args, **kwargs):
		self.helper = BaseFormHelper(
			url_name = url_name or self.URL_NAME, 
			submit_name = submit_name or self.SUBMIT_NAME, 
			back = back or self.BACK, 
			back_name = back_name or self.BACK_NAME, 
			submit_css = submit_css or self.SUBMIT_CSS, 
			back_css = back_css or self.BACK_CSS,
		)
		super(SimpleCrispyModelForm, self).__init__(data, *args, **kwargs)


