# +
from ast import Lambda
from operator import index
import os
import pandas as pd
import numpy as np

IN_PATH_AUSTIN_WEATHER = os.path.join('weather','austin','2010_2020_austin.csv')
IN_PATH_DALLAS_WEATHER = os.path.join('weather','dallas','2010_2020_dallas.csv')
IN_PATH_HOUSTON_WEATHER = os.path.join('weather','houston','2010_2020_houston.csv')
IN_PATH_LOS_ANGELES_WEATHER = os.path.join('weather','los_angeles','2010_2020_los_angeles.csv')
IN_PATH_NEW_YORK_WEATHER = os.path.join('weather','new_york','2010_2020_new_york.csv')
AUSTIN_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2909277.csv'
DALLAS_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905654.csv'
HOUSTON_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905669.csv'
LOS_ANGELES_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905675.csv'
NEW_YORK_WEATHER_URL = 'https://www.ncei.noaa.gov/orders/cdo/2905680.csv'
# -


