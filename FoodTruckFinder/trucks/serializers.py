from rest_framework import serializers
from .models import FoodTruck

# Define the serializer for the FoodTruck model
class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = ['applicant', 'facility_type', 'location_description', 'address', 'latitude', 'longitude']
