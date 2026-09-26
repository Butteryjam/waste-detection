from django.db import models
from django.contrib.auth.models import User


class UserPersonalModel(models.Model):


    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)   
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


def __str__(self):
    return self.firstname, self.lastname, self.age,self.address,self.phone,self.city,self.state,self.country


class Detected(models.Model):
    frame_number = models.IntegerField()
    class_name = models.CharField(max_length=100)
    confidence = models.IntegerField()
    coordinates = models.CharField(max_length=100)
    # latitude = models.DecimalField(max_digits=9, decimal_places=6)  # Decimal field for latitude (adjust max_digits and decimal_places as needed)
    # longitude = models.DecimalField(max_digits=9, decimal_places=6)  # Decimal field for longitude (adjust max_digits and decimal_places as needed)
    timestamp = models.DateTimeField(auto_now_add=True)  # Add this line to store the detection time

    def __str__(self):
        return f"Frame {self.frame_number}: {self.class_name} - Confidence: {self.confidence}"