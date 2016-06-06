from django import forms
#from django.forms.extras.widgets import SelectDateWidget
from mysite.models import user_profile
import account.forms

class SignupForm(account.forms.SignupForm):
		userid = forms.IntegerField()
		phone = forms.IntegerField()
#		username = forms.CharField()
#		model = user_profile
#		fileds = ('userid', 'phone', )
