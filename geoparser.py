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
print(url)
response = request.urlopen(url)
raw = response.read().decode('utf-8')
print(f'{type(raw)}, \n{len(raw)}, \n{raw[:501]}')