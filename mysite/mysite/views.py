import account.views
import mysite.forms
from mysite.models import user_profile
from django.contrib.auth.models import AbstractBaseUser, UserManager

class SignupView(account.views.SignupView):

	form_class = mysite.forms.SignupForm

	def after_signup(self, form):
		self.create_profile(form)
		super(SignupView, self).after_signup(form)

	def create_profile(self, form):	
		profile = self.created_user.profile
		profile.save()

	#	user_profile.objects.creat(
	#		user = self.created_user,		
	#	)
