from django.db import models

# Create your models here.

# Define the FoodTruck model
class FoodTruck(models.Model):
    applicant = models.CharField(max_length=255)  # Name of the food truck
    facility_type = models.CharField(max_length=100)  
    location_description = models.CharField(max_length=255)  # Description of the location
    address = models.CharField(max_length=255)  # Address of the food truck
    latitude = models.FloatField()  
    longitude = models.FloatField()  

    def __str__(self):
        return self.applicant