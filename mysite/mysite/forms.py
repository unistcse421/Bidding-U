from django import forms
#from django.forms.extras.widgets import SelectDateWidget

import account.forms


class SignupForm(account.forms.SignupForm):
	userid = forms.IntegerField()
	phone = forms.IntegerField()
