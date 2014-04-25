
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


class LogoutForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_action = 'logout'
        self.helper.add_input(Submit('logout', 'Logout'))
        super(LogoutForm, self).__init__(*args, **kwargs)


