from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class trains(models.Model):
    train_name=models.CharField(max_length=50)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField(auto_now=False, auto_now_add=False)
    price=models.FloatField(default=120)
    seats_available=models.IntegerField()

class person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=50,choices=(("MALE","MALE"),("FEMALE","FEMALE"),("OTHER","OTHER")))
    email=models.EmailField(max_length=254)
    date_and_time_of_booking=models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField(max_length=10)
    train=models.ForeignKey(trains, on_delete=models.CASCADE)

