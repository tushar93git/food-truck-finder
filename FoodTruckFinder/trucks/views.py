import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodTruck
from .serializers import FoodTruckSerializer
from geopy.distance import geodesic
from django.conf import settings

@api_view(['POST'])
def load_food_trucks(request):
    # Use pandas for data loading
    file_path = settings.BASE_DIR / 'data/food-truck-data.csv'
    data = pd.read_csv(file_path)

    # Clear existing data
    FoodTruck.objects.all().delete()

    # Load data from CSV file to database
    for i, row in data.iterrows():
        # Split the Location field into latitude and longitude
        location = row['Location'].strip("()").split(", ")
        FoodTruck.objects.create(
            applicant=row['Applicant'],
            facility_type=row['FacilityType'],
            location_description=row['LocationDescription'],
            address=row['Address'],
            latitude=float(location[0]),
            longitude=float(location[1])
        )

    return Response({'status': 'Data loaded successfully'})

@api_view(['GET'])
def find_food_trucks(request):
    # Extract latitude and longitude from the GET request parameters
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))
    user_location = (latitude, longitude)
    # Query all FoodTruck objects from the database
    trucks = FoodTruck.objects.all()
    results = []
    # Calculate the distance of each truck from the user's location
    for truck in trucks:
        truck_location = (truck.latitude, truck.longitude)
        distance = geodesic(user_location, truck_location).kilometers
        results.append({
            'truck': truck,
            'distance': distance
        })
    results = sorted(results, key=lambda x: x['distance'])
    if len(results) < 5:
        results = (results * 5)[:5]
    else:
        results = results[:5]
    serializer = FoodTruckSerializer([result['truck'] for result in results], many=True)
    return Response(serializer.data)
