from __future__ import unicode_literals

from django.db import models

# Create your models here.


class auction_list(models.Model):
	auction_id = models.AutoField(primary_key=True)
	item_id = models.IntegerField(default=0)
	due_date = models.DateTimeField()
	current_price = models.IntegerField(default=0)
	book_id =  models.IntegerField(default=0)
	bidding_state = models.IntegerField(default=0)
	

class success_auction(models.Model):
	auction_id = models.AutoField(primary_key=True)
	user_id = models.IntegerField(default=0)
	item_id = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

