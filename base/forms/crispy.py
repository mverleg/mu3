
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from django.core.urlresolvers import reverse


'''
	the default actions already implemented, but not overriding __init__ so that you
	can add more actions (actually a generator, not a class)
'''
def BaseFormHelper(url_name = None, submit_name = 'Submit', back = '', back_name = 'Back'):
	helper = FormHelper()
	if url_name:
		helper.form_action = reverse(url_name)
	if back:
		self.helper.add_input(Button('back', 'Back', onclick = 'location.href=\'%s\'' % back, css_class = 'btn-danger'))
	''' it is not advisable to use 'submit' or 'post' as input names, because jquery gets confused  '''
	helper.add_input(Submit('go', submit_name))
	return helper


'''
	a simply form (like 80%) with just an action and a submit button (possibly a back button)		
'''
class SimpleCrispyModelForm(ModelForm):
	
	def __init__(self, data = None, url_name = None, submit_name = 'Submit', back = '', back_name = 'Back', *args, **kwargs):
		self.helper = BaseFormHelper(url_name, submit_name, back)
		super(LikeForm, self).__init__(data, *args, **kwargs)


