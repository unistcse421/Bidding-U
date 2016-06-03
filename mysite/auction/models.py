from __future__ import unicode_literals

from django.db import models
from datetime import datetime, timedelta
# Create your models here.

class auction_list(models.Model):
	now = datetime.now()
	Period = (
		(now + timedelta(days=1), '1 days'),
		(now + timedelta(days=3), '3 days'),
		(now + timedelta(days=5), '5 days'),
		(now + timedelta(days=7), '7 days'),
	)
	auction_id = models.AutoField(primary_key=True)
	item_id = models.IntegerField(default=0)
	due_date = models.DateTimeField(choices=Period)
	current_price = models.IntegerField(default=0)
	book_id =  models.IntegerField(default=0)
	bidding_state = models.BooleanField(default=True)

class success_auction(models.Model):
	auction_id = models.AutoField(primary_key=True)
	user_id = models.IntegerField(default=0)
	item_id = models.IntegerField(default=0)
	price = models.IntegerField(default=0)
	winner_id = models.IntegerField(default=0)
