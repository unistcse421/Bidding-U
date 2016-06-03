from django.conf import settings
from django.db import models

class user_profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	phone = models.IntegerField(default=0)
