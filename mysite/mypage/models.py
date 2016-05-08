from __future__ import unicode_literals

from django.db import models

# Create your models here.

class item_list(models.Model):
        item_id = models.IntegerField(auto_now_add=True)
	user_id = models.IntegerField(default=0)
	reserved_price = models.IntegerField(default=0)
	state = models.CharField(max_length=3)
	book_number = models.IntegerField(default=0)

class book_list(models.Model):
	book_id = models.IntegerField(auto_now_add=True)
	book_name = models.CharField(max_length=200)
	author =
	price = models.IntegerField(default=0)
	edition = 
