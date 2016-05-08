from __future__ import unicode_literals

from django.db import models

# Create your models here.


class auction_list(models.Model):
	auction_id = models.IntegerField(auto_now_add=True)
	item_id = models.IntegerField(default=0)
	due_date = models.DateTimeField()
	current_price = models.IntegerField(default=0)
	book_id =  models.IntegerField(default=0)
	bidding_state = 

class success_auction(models.Model):
	auction_id = models.IntegerField(auto_now_add=True)
	user_id = models.IntegerField(default=0)
	item_id = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

