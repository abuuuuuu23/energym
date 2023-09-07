from django.db import models

# Create your models here.

class user_account(models.Model):
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    account_type=models.CharField(max_length=30)
    class meta:
        db_table="user_account"

class user_details(models.Model):
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    photo=models.CharField(max_length=30)
    class meta:
        db_table="user_details"

class trainer_account(models.Model):
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    account_type=models.CharField(max_length=30)
    class meta:
        db_table="trainer_account"

class trainer_details(models.Model):
    username=models.CharField(max_length=30)
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    age=models.IntegerField()
    experience=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    phone=models.IntegerField()
    address=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    photo=models.CharField(max_length=30)
    class meta:
        db_table="trainer_details"
