from django.urls import path
from .views import find_food_trucks, load_food_trucks

urlpatterns = [
    path('find_food_trucks/', find_food_trucks),
    path('load_food_trucks/', load_food_trucks),  
]

