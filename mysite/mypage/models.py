from __future__ import unicode_literals

from django.db import models

# Create your models here.

class item_information(models.Model):
        State = (
                ('A', 'A'),
                ('B', 'B'),
                ('C', 'C'),
                ('D', 'D'),
        )
	
	item_id = models.AutoField(primary_key=True)
	user_id = models.IntegerField(default=0)
	reserved_price = models.IntegerField(default=0)
	state = models.CharField(max_length=1, choices=State)
	book_number = models.IntegerField(default=0)

class book_list(models.Model):
	book_id = models.AutoField(primary_key=True)
	book_name = models.CharField(max_length=200)
	author = models.CharField(max_length=20)
	price = models.IntegerField(default=0)
	edition = models.IntegerField(default=0)
