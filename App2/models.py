from django.db import models
import random

def generate_unique_uid():
    return random.randint(1, 1000000)  # Replace with your logic to generate uid

class Course(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    img = models.ImageField()
    info = models.CharField(max_length=100)
    price = models.IntegerField()

class usrData(models.Model):
    usrid = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True, max_length=30,unique=True)
    mobile = models.IntegerField()
    gender = models.CharField(max_length=10)
    edu = models.CharField(max_length=40)
    cors = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    usr = models.CharField(unique=True, max_length=30)