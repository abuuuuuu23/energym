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
    district=models.CharField(max_length=30)
    photo=models.CharField(max_length=300)
    class meta:
        db_table="user_details"



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
    photo=models.CharField(max_length=300)
    class meta:
        db_table="trainer_details"


class packages(models.Model):
    trainername=models.CharField(max_length=30)
    typeofsession=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    price=models.IntegerField()
    photo=models.CharField(max_length=30)
    available_slot=models.CharField(max_length=30)
    catagory=models.CharField(max_length=30)
    starting_date=models.DateField(max_length=30)
    status=models.CharField(max_length=30)

    class meta:
        db_table="packages"


class usergym_data(models.Model):
    username=models.ForeignKey(user_details,on_delete=models.CASCADE)
    trainername=models.CharField(max_length=30)
    packgname=models.CharField(max_length=30)
    price=models.IntegerField()
    joining_date=models.DateField(max_length=30)
    start_date=models.DateField(max_length=30)
    photo=models.CharField(max_length=30)
    height=models.IntegerField()
    weight=models.IntegerField()
    selfinto=models.CharField(max_length=30)
    status=models.CharField(max_length=30)

    class meta:
        db_table="usergym_data"