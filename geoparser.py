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


# eturns city names from raw text
def get_cities(raw):
    places = GeoText(raw)
    cities = list(places.cities)
    return cities


# searchs OpenStreetMap API for city coordinates
def get_coordinates(cities):

    geolocator = Nominatim(user_agent="geoparser", timeout=2)

    coordinates = []

    for city in cities: 
        try:
            location = geolocator.geocode(city)
            if location:
                coordinates.append(location)
        except GeocoderTimedOut as e:
            print("Error: geocode failed on input %s with message %s"%(city, e))
        
    return coordinates


# returns geopandas dataframe from list of coordinates 
def get_geo_df(coordinates):
    df = pd.DataFrame(coordinates, columns=['City Name', 'Coordinates'])

    # switches latitute and longitute order because that's the order my map uses
    geometry = [Point(x[1], x[0]) for x in df['Coordinates']]

    # coordinate system I'm using
    crs = {'init': 'epsg:4326'}

    geo_df = gpd.GeoDataFrame(df, crs=crs, geometry=geometry)

    return geo_df

# returns plot of geopandas df geometry series
def plot_coordinates(geo_df):
    # world map .shp file 
    countries_map = gpd.read_file('files/Countries_WGS84.shp')

    f, ax = plt.subplots()
    countries_map.plot(ax=ax, alpha=0.4, color='grey')
    return geo_df['geometry'].plot(ax=ax, markersize = 30, color = 'b', marker = '^', alpha=.2)


# aggregate function
def geoparse(raw):
    cities = get_cities(raw)
    lat_lon = get_coordinates(cities)
    geo_df = get_geo_df(lat_lon)
    plot_coordinates(geo_df)
    plt.show(block=True)


geoparse(raw)