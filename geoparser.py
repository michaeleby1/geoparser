import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from urllib import request
from geotext import GeoText
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from shapely.geometry import Point, Polygon
import descartes
import sys

url = sys.argv[1]
response = request.urlopen(url)
raw = response.read().decode('utf-8')
# print(f'{type(raw)}, \n{len(raw)}, \n{raw[:501]}')

# takes raw text and extracts city names
def get_cities(raw):
    places = GeoText(raw)
    cities = list(places.cities)
    return cities

# searchs OpenStreetMap API for city coordinates
def get_coordinates(cities):
    
    geolocator = Nominatim(user_agent="geoparser", timeout=2)

    lat_lon = []
    for city in cities[:5]: 
        try:
            location = geolocator.geocode(city)
            if location:
                print(location.latitude, location.longitude)
                lat_lon.append(location)
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(city, e))
        
    return lat_lon



cities = get_cities(raw)
get_coordinates(cities)