from django.db import models

class user(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    level = models.CharField(max_length=10)
    phone_number = models.IntegerField(default=0)

class auction_list(models.Model):
    item_id = models.IntegerField(default=0)
    due_date = models.DateField()
    current_price = models.IntegerField(default=0)

class list(models.Model):
    book_number = models.IntegerField(default=0)
    book_name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

class candidate_list(models.Model):
    user_id = models.IntegerField(default=0)
    item_id = models.IntegerField(default=0)
    suggest_price = models.IntegerField(default=0)
    suggest_time = models.DateField()

class item(models.Model):
    user_id = models.IntegerField(default=0)
    reserved_price = models.IntegerField(default=0)
    state = models.CharField(max_length=3)
    book_number = models.IntegerField(default=0)

    
# Create your models here.
