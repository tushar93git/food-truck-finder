# Food Truck Finder

This is a Django project that helps users find nearby food trucks based on a given latitude and longitude in San Francisco.

## Features

- Load food truck data from a CSV file.
- Find the nearest food trucks based on latitude and longitude.
- Return at least 5 food trucks even if fewer are available.

## Requirements

- Python 
- Django
- Django REST Framework
- Pandas
- Geopy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/tushar93git/food-truck-finder.git

2.Create and activate a virtual environment:

3.Install the required packages:
pip install -r requirements.txt

4.Run the development server:
python manage.py runserver

5.Find Food Trucks:
http://127.0.0.1:8000/api/find_food_trucks/?latitude=<latitude>&longitude=<longitude>
Example:
To find food trucks near Union Square, you can use the following URL:
http://127.0.0.1:8000/api/find_food_trucks/?latitude=37.7880&longitude=-122.4075
