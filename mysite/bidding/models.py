from __future__ import unicode_literals

from django.db import models

# Create your models here.
class candidate_list(models.Model):
        candidate_id = models.AutoField(primary_key=True)
        user_id = models.IntegerField(default=0)
        auction_id = models.IntegerField(default=0)
        suggest_price = models.IntegerField(default=0)
        suggest_time = models.DateTimeField(auto_now_add = True)

