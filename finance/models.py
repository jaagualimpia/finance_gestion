from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 30, primary_key = True)
    password = models.CharField(max_length=100)

class Transaction(models.Model):
    id = models.BigAutoField(primary_key = True)
    description = models.CharField(max_length = 50)
    amount = models.FloatField()
    date = models.DateField()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    transaction_type = models.BooleanField()
    isPocketTransaction = models.BooleanField()

class Pocket(models.Model):
    id = models.BigAutoField(primary_key = True)
    pocket_name = models.CharField(max_length = 50)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)