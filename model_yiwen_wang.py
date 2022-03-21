# + endofcell="--"

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
IN_PATH_AUSTIN_PM25_2020 = os.path.join('air_pollution','austin','pm25','austin_2020_pm25.csv')
IN_PATH_AUSTIN_PM25_2019 = os.path.join('air_pollution','austin','pm25','austin_2019_pm25.csv')
IN_PATH_AUSTIN_PM25_2018 = os.path.join('air_pollution','austin','pm25','austin_2018_pm25.csv')
IN_PATH_AUSTIN_PM25_2017 = os.path.join('air_pollution','austin','pm25','austin_2017_pm25.csv')
IN_PATH_AUSTIN_PM25_2016 = os.path.join('air_pollution','austin','pm25','austin_2016_pm25.csv')
IN_PATH_AUSTIN_PM25_2015 = os.path.join('air_pollution','austin','pm25','austin_2015_pm25.csv')
IN_PATH_AUSTIN_PM25_2014 = os.path.join('air_pollution','austin','pm25','austin_2014_pm25.csv')
IN_PATH_AUSTIN_PM25_2013 = os.path.join('air_pollution','austin','pm25','austin_2013_pm25.csv')
IN_PATH_AUSTIN_PM25_2012 = os.path.join('air_pollution','austin','pm25','austin_2012_pm25.csv')
IN_PATH_AUSTIN_PM25_2011 = os.path.join('air_pollution','austin','pm25','austin_2011_pm25.csv')
IN_PATH_AUSTIN_PM25_2010 = os.path.join('air_pollution','austin','pm25','austin_2010_pm25.csv')
IN_PATH_HOUSTON_PM25_2020 = os.path.join('air_pollution','houston','pm25','houston_2020_pm25.csv')
IN_PATH_HOUSTON_PM25_2019 = os.path.join('air_pollution','houston','pm25','houston_2019_pm25.csv')
IN_PATH_HOUSTON_PM25_2018 = os.path.join('air_pollution','houston','pm25','houston_2018_pm25.csv')
IN_PATH_HOUSTON_PM25_2017 = os.path.join('air_pollution','houston','pm25','houston_2017_pm25.csv')
IN_PATH_HOUSTON_PM25_2016 = os.path.join('air_pollution','houston','pm25','houston_2016_pm25.csv')
IN_PATH_HOUSTON_PM25_2015 = os.path.join('air_pollution','houston','pm25','houston_2015_pm25.csv')
IN_PATH_HOUSTON_PM25_2014 = os.path.join('air_pollution','houston','pm25','houston_2014_pm25.csv')
IN_PATH_HOUSTON_PM25_2013 = os.path.join('air_pollution','houston','pm25','houston_2013_pm25.csv')
IN_PATH_HOUSTON_PM25_2012 = os.path.join('air_pollution','houston','pm25','houston_2012_pm25.csv')
IN_PATH_HOUSTON_PM25_2011 = os.path.join('air_pollution','houston','pm25','houston_2011_pm25.csv')
IN_PATH_HOUSTON_PM25_2010 = os.path.join('air_pollution','houston','pm25','houston_2010_pm25.csv')
IN_PATH_DALLAS_PM25_2020 = os.path.join('air_pollution','dallas','pm25','dallas_2020_pm25.csv')
IN_PATH_DALLAS_PM25_2019 = os.path.join('air_pollution','dallas','pm25','dallas_2019_pm25.csv')
IN_PATH_DALLAS_PM25_2018 = os.path.join('air_pollution','dallas','pm25','dallas_2018_pm25.csv')
IN_PATH_DALLAS_PM25_2017 = os.path.join('air_pollution','dallas','pm25','dallas_2017_pm25.csv')
IN_PATH_DALLAS_PM25_2016 = os.path.join('air_pollution','dallas','pm25','dallas_2016_pm25.csv')
IN_PATH_DALLAS_PM25_2015 = os.path.join('air_pollution','dallas','pm25','dallas_2015_pm25.csv')
IN_PATH_DALLAS_PM25_2014 = os.path.join('air_pollution','dallas','pm25','dallas_2014_pm25.csv')
IN_PATH_DALLAS_PM25_2013 = os.path.join('air_pollution','dallas','pm25','dallas_2013_pm25.csv')
IN_PATH_DALLAS_PM25_2012 = os.path.join('air_pollution','dallas','pm25','dallas_2012_pm25.csv')
IN_PATH_DALLAS_PM25_2011 = os.path.join('air_pollution','dallas','pm25','dallas_2011_pm25.csv')
IN_PATH_DALLAS_PM25_2010 = os.path.join('air_pollution','dallas','pm25','dallas_2010_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2020 = os.path.join('air_pollution','los_angeles','pm25','la_2020_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2019 = os.path.join('air_pollution','los_angeles','pm25','la_2019_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2018 = os.path.join('air_pollution','los_angeles','pm25','la_2018_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2017 = os.path.join('air_pollution','los_angeles','pm25','la_2017_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2016 = os.path.join('air_pollution','los_angeles','pm25','la_2016_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2015 = os.path.join('air_pollution','los_angeles','pm25','la_2015_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2014 = os.path.join('air_pollution','los_angeles','pm25','la_2014_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2013 = os.path.join('air_pollution','los_angeles','pm25','la_2013_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2012 = os.path.join('air_pollution','los_angeles','pm25','la_2012_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2011 = os.path.join('air_pollution','los_angeles','pm25','la_2011_pm25.csv')
IN_PATH_LOS_ANGELES_PM25_2010 = os.path.join('air_pollution','los_angeles','pm25','la_2010_pm25.csv')
IN_PATH_NEW_YORK_PM25_2020 = os.path.join('air_pollution','new_york','pm25','ny_2020_pm25.csv')
IN_PATH_NEW_YORK_PM25_2019 = os.path.join('air_pollution','new_york','pm25','ny_2019_pm25.csv')
IN_PATH_NEW_YORK_PM25_2018 = os.path.join('air_pollution','new_york','pm25','ny_2018_pm25.csv')
IN_PATH_NEW_YORK_PM25_2017 = os.path.join('air_pollution','new_york','pm25','ny_2017_pm25.csv')
IN_PATH_NEW_YORK_PM25_2016 = os.path.join('air_pollution','new_york','pm25','ny_2016_pm25.csv')
IN_PATH_NEW_YORK_PM25_2015 = os.path.join('air_pollution','new_york','pm25','ny_2015_pm25.csv')
IN_PATH_NEW_YORK_PM25_2014 = os.path.join('air_pollution','new_york','pm25','ny_2014_pm25.csv')
IN_PATH_NEW_YORK_PM25_2013 = os.path.join('air_pollution','new_york','pm25','ny_2013_pm25.csv')
IN_PATH_NEW_YORK_PM25_2012 = os.path.join('air_pollution','new_york','pm25','ny_2012_pm25.csv')
IN_PATH_NEW_YORK_PM25_2011 = os.path.join('air_pollution','new_york','pm25','ny_2011_pm25.csv')
IN_PATH_NEW_YORK_PM25_2010 = os.path.join('air_pollution','new_york','pm25','ny_2010_pm25.csv')

IN_PATH_AUSTIN_PM10_2020 = os.path.join('air_pollution','austin','pm10','austin_2020_pm10.csv')
IN_PATH_AUSTIN_PM10_2019 = os.path.join('air_pollution','austin','pm10','austin_2019_pm10.csv')
IN_PATH_AUSTIN_PM10_2018 = os.path.join('air_pollution','austin','pm10','austin_2018_pm10.csv')
IN_PATH_AUSTIN_PM10_2017 = os.path.join('air_pollution','austin','pm10','austin_2017_pm10.csv')
IN_PATH_AUSTIN_PM10_2016 = os.path.join('air_pollution','austin','pm10','austin_2016_pm10.csv')
IN_PATH_AUSTIN_PM10_2015 = os.path.join('air_pollution','austin','pm10','austin_2015_pm10.csv')
IN_PATH_AUSTIN_PM10_2014 = os.path.join('air_pollution','austin','pm10','austin_2014_pm10.csv')
IN_PATH_AUSTIN_PM10_2013 = os.path.join('air_pollution','austin','pm10','austin_2013_pm10.csv')
IN_PATH_AUSTIN_PM10_2012 = os.path.join('air_pollution','austin','pm10','austin_2012_pm10.csv')
IN_PATH_AUSTIN_PM10_2011 = os.path.join('air_pollution','austin','pm10','austin_2011_pm10.csv')
IN_PATH_AUSTIN_PM10_2010 = os.path.join('air_pollution','austin','pm10','austin_2010_pm10.csv')

IN_PATH_HOUSTON_PM10_2020 = os.path.join('air_pollution','houston','pm10','houston_2020_pm10.csv')
IN_PATH_HOUSTON_PM10_2019 = os.path.join('air_pollution','houston','pm10','houston_2019_pm10.csv')
IN_PATH_HOUSTON_PM10_2018 = os.path.join('air_pollution','houston','pm10','houston_2018_pm10.csv')
IN_PATH_HOUSTON_PM10_2017 = os.path.join('air_pollution','houston','pm10','houston_2017_pm10.csv')
IN_PATH_HOUSTON_PM10_2016 = os.path.join('air_pollution','houston','pm10','houston_2016_pm10.csv')
IN_PATH_HOUSTON_PM10_2015 = os.path.join('air_pollution','houston','pm10','houston_2015_pm10.csv')
IN_PATH_HOUSTON_PM10_2014 = os.path.join('air_pollution','houston','pm10','houston_2014_pm10.csv')
IN_PATH_HOUSTON_PM10_2013 = os.path.join('air_pollution','houston','pm10','houston_2013_pm10.csv')
IN_PATH_HOUSTON_PM10_2012 = os.path.join('air_pollution','houston','pm10','houston_2012_pm10.csv')
IN_PATH_HOUSTON_PM10_2011 = os.path.join('air_pollution','houston','pm10','houston_2011_pm10.csv')
IN_PATH_HOUSTON_PM10_2010 = os.path.join('air_pollution','houston','pm10','houston_2010_pm10.csv')

IN_PATH_DALLAS_PM10_2020 = os.path.join('air_pollution','dallas','pm10','dallas_2020_pm10.csv')
IN_PATH_DALLAS_PM10_2019 = os.path.join('air_pollution','dallas','pm10','dallas_2019_pm10.csv')
IN_PATH_DALLAS_PM10_2018 = os.path.join('air_pollution','dallas','pm10','dallas_2018_pm10.csv')
IN_PATH_DALLAS_PM10_2017 = os.path.join('air_pollution','dallas','pm10','dallas_2017_pm10.csv')
IN_PATH_DALLAS_PM10_2016 = os.path.join('air_pollution','dallas','pm10','dallas_2016_pm10.csv')
IN_PATH_DALLAS_PM10_2015 = os.path.join('air_pollution','dallas','pm10','dallas_2015_pm10.csv')
IN_PATH_DALLAS_PM10_2014 = os.path.join('air_pollution','dallas','pm10','dallas_2014_pm10.csv')
IN_PATH_DALLAS_PM10_2013 = os.path.join('air_pollution','dallas','pm10','dallas_2013_pm10.csv')
IN_PATH_DALLAS_PM10_2012 = os.path.join('air_pollution','dallas','pm10','dallas_2012_pm10.csv')
IN_PATH_DALLAS_PM10_2011 = os.path.join('air_pollution','dallas','pm10','dallas_2011_pm10.csv')
IN_PATH_DALLAS_PM10_2010 = os.path.join('air_pollution','dallas','pm10','dallas_2010_pm10.csv')

IN_PATH_LOS_ANGELES_PM10_2020 = os.path.join('air_pollution','los_angeles','pm10','la_2020_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2019 = os.path.join('air_pollution','los_angeles','pm10','la_2019_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2018 = os.path.join('air_pollution','los_angeles','pm10','la_2018_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2017 = os.path.join('air_pollution','los_angeles','pm10','la_2017_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2016 = os.path.join('air_pollution','los_angeles','pm10','la_2016_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2015 = os.path.join('air_pollution','los_angeles','pm10','la_2015_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2014 = os.path.join('air_pollution','los_angeles','pm10','la_2014_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2013 = os.path.join('air_pollution','los_angeles','pm10','la_2013_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2012 = os.path.join('air_pollution','los_angeles','pm10','la_2012_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2011 = os.path.join('air_pollution','los_angeles','pm10','la_2011_pm10.csv')
IN_PATH_LOS_ANGELES_PM10_2010 = os.path.join('air_pollution','los_angeles','pm10','la_2010_pm10.csv')

IN_PATH_NEW_YORK_PM10_2020 = os.path.join('air_pollution','new_york','pm10','ny_2020_pm10.csv')
IN_PATH_NEW_YORK_PM10_2019 = os.path.join('air_pollution','new_york','pm10','ny_2019_pm10.csv')
IN_PATH_NEW_YORK_PM10_2018 = os.path.join('air_pollution','new_york','pm10','ny_2018_pm10.csv')
IN_PATH_NEW_YORK_PM10_2017 = os.path.join('air_pollution','new_york','pm10','ny_2017_pm10.csv')
IN_PATH_NEW_YORK_PM10_2016 = os.path.join('air_pollution','new_york','pm10','ny_2016_pm10.csv')
IN_PATH_NEW_YORK_PM10_2015 = os.path.join('air_pollution','new_york','pm10','ny_2015_pm10.csv')
IN_PATH_NEW_YORK_PM10_2014 = os.path.join('air_pollution','new_york','pm10','ny_2014_pm10.csv')
IN_PATH_NEW_YORK_PM10_2013 = os.path.join('air_pollution','new_york','pm10','ny_2013_pm10.csv')
IN_PATH_NEW_YORK_PM10_2012 = os.path.join('air_pollution','new_york','pm10','ny_2012_pm10.csv')
IN_PATH_NEW_YORK_PM10_2011 = os.path.join('air_pollution','new_york','pm10','ny_2011_pm10.csv')
IN_PATH_NEW_YORK_PM10_2010 = os.path.join('air_pollution','new_york','pm10','ny_2010_pm10.csv')

IN_PATH_AUSTIN_NO2_2020 = os.path.join('air_pollution','austin','no2','austin_2020_no2.csv')
IN_PATH_AUSTIN_NO2_2019 = os.path.join('air_pollution','austin','no2','austin_2019_no2.csv')
IN_PATH_AUSTIN_NO2_2018 = os.path.join('air_pollution','austin','no2','austin_2018_no2.csv')
IN_PATH_AUSTIN_NO2_2017 = os.path.join('air_pollution','austin','no2','austin_2017_no2.csv')
IN_PATH_AUSTIN_NO2_2016 = os.path.join('air_pollution','austin','no2','austin_2016_no2.csv')
IN_PATH_AUSTIN_NO2_2015 = os.path.join('air_pollution','austin','no2','austin_2015_no2.csv')
IN_PATH_AUSTIN_NO2_2014 = os.path.join('air_pollution','austin','no2','austin_2014_no2.csv')
IN_PATH_AUSTIN_NO2_2013 = os.path.join('air_pollution','austin','no2','austin_2013_no2.csv')
IN_PATH_AUSTIN_NO2_2012 = os.path.join('air_pollution','austin','no2','austin_2012_no2.csv')
IN_PATH_AUSTIN_NO2_2011 = os.path.join('air_pollution','austin','no2','austin_2011_no2.csv')
IN_PATH_AUSTIN_NO2_2010 = os.path.join('air_pollution','austin','no2','austin_2010_no2.csv')

IN_PATH_DALLAS_NO2_2020 = os.path.join('air_pollution','dallas','no2','dallas_2020_no2.csv')
IN_PATH_DALLAS_NO2_2019 = os.path.join('air_pollution','dallas','no2','dallas_2019_no2.csv')
IN_PATH_DALLAS_NO2_2018 = os.path.join('air_pollution','dallas','no2','dallas_2018_no2.csv')
IN_PATH_DALLAS_NO2_2017 = os.path.join('air_pollution','dallas','no2','dallas_2017_no2.csv')
IN_PATH_DALLAS_NO2_2016 = os.path.join('air_pollution','dallas','no2','dallas_2016_no2.csv')
IN_PATH_DALLAS_NO2_2015 = os.path.join('air_pollution','dallas','no2','dallas_2015_no2.csv')
IN_PATH_DALLAS_NO2_2014 = os.path.join('air_pollution','dallas','no2','dallas_2014_no2.csv')
IN_PATH_DALLAS_NO2_2013 = os.path.join('air_pollution','dallas','no2','dallas_2013_no2.csv')
IN_PATH_DALLAS_NO2_2012 = os.path.join('air_pollution','dallas','no2','dallas_2012_no2.csv')
IN_PATH_DALLAS_NO2_2011 = os.path.join('air_pollution','dallas','no2','dallas_2011_no2.csv')
IN_PATH_DALLAS_NO2_2010 = os.path.join('air_pollution','dallas','no2','dallas_2010_no2.csv')

IN_PATH_HOUSTON_NO2_2020 = os.path.join('air_pollution','houston','no2','houston_2020_no2.csv')
IN_PATH_HOUSTON_NO2_2019 = os.path.join('air_pollution','houston','no2','houston_2019_no2.csv')
IN_PATH_HOUSTON_NO2_2018 = os.path.join('air_pollution','houston','no2','houston_2018_no2.csv')
IN_PATH_HOUSTON_NO2_2017 = os.path.join('air_pollution','houston','no2','houston_2017_no2.csv')
IN_PATH_HOUSTON_NO2_2016 = os.path.join('air_pollution','houston','no2','houston_2016_no2.csv')
IN_PATH_HOUSTON_NO2_2015 = os.path.join('air_pollution','houston','no2','houston_2015_no2.csv')
IN_PATH_HOUSTON_NO2_2014 = os.path.join('air_pollution','houston','no2','houston_2014_no2.csv')
IN_PATH_HOUSTON_NO2_2013 = os.path.join('air_pollution','houston','no2','houston_2013_no2.csv')
IN_PATH_HOUSTON_NO2_2012 = os.path.join('air_pollution','houston','no2','houston_2012_no2.csv')
IN_PATH_HOUSTON_NO2_2011 = os.path.join('air_pollution','houston','no2','houston_2011_no2.csv')
IN_PATH_HOUSTON_NO2_2010 = os.path.join('air_pollution','houston','no2','houston_2010_no2.csv')

IN_PATH_LOS_ANGELES_NO2_2020 = os.path.join('air_pollution','los_angeles','no2','la_2020_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2019 = os.path.join('air_pollution','los_angeles','no2','la_2019_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2018 = os.path.join('air_pollution','los_angeles','no2','la_2018_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2017 = os.path.join('air_pollution','los_angeles','no2','la_2017_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2016 = os.path.join('air_pollution','los_angeles','no2','la_2016_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2015 = os.path.join('air_pollution','los_angeles','no2','la_2015_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2014 = os.path.join('air_pollution','los_angeles','no2','la_2014_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2013 = os.path.join('air_pollution','los_angeles','no2','la_2013_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2012 = os.path.join('air_pollution','los_angeles','no2','la_2012_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2011 = os.path.join('air_pollution','los_angeles','no2','la_2011_no2.csv')
IN_PATH_LOS_ANGELES_NO2_2010 = os.path.join('air_pollution','los_angeles','no2','la_2010_no2.csv')

IN_PATH_NEW_YORK_NO2_2020 = os.path.join('air_pollution','new_york','no2','ny_2020_no2.csv')
IN_PATH_NEW_YORK_NO2_2019 = os.path.join('air_pollution','new_york','no2','ny_2019_no2.csv')
IN_PATH_NEW_YORK_NO2_2018 = os.path.join('air_pollution','new_york','no2','ny_2018_no2.csv')
IN_PATH_NEW_YORK_NO2_2017 = os.path.join('air_pollution','new_york','no2','ny_2017_no2.csv')
IN_PATH_NEW_YORK_NO2_2016 = os.path.join('air_pollution','new_york','no2','ny_2016_no2.csv')
IN_PATH_NEW_YORK_NO2_2015 = os.path.join('air_pollution','new_york','no2','ny_2015_no2.csv')
IN_PATH_NEW_YORK_NO2_2014 = os.path.join('air_pollution','new_york','no2','ny_2014_no2.csv')
IN_PATH_NEW_YORK_NO2_2013 = os.path.join('air_pollution','new_york','no2','ny_2013_no2.csv')
IN_PATH_NEW_YORK_NO2_2012 = os.path.join('air_pollution','new_york','no2','ny_2012_no2.csv')
IN_PATH_NEW_YORK_NO2_2011 = os.path.join('air_pollution','new_york','no2','ny_2011_no2.csv')
IN_PATH_NEW_YORK_NO2_2010 = os.path.join('air_pollution','new_york','no2','ny_2010_no2.csv')

austin_pm25_2020 = pd.read_csv(IN_PATH_AUSTIN_PM25_2020)
austin_pm25_2019 = pd.read_csv(IN_PATH_AUSTIN_PM25_2019)
austin_pm25_2018 = pd.read_csv(IN_PATH_AUSTIN_PM25_2018)
austin_pm25_2017 = pd.read_csv(IN_PATH_AUSTIN_PM25_2017)
austin_pm25_2016 = pd.read_csv(IN_PATH_AUSTIN_PM25_2016)
austin_pm25_2015 = pd.read_csv(IN_PATH_AUSTIN_PM25_2015)
austin_pm25_2014 = pd.read_csv(IN_PATH_AUSTIN_PM25_2014)
austin_pm25_2013 = pd.read_csv(IN_PATH_AUSTIN_PM25_2013)
austin_pm25_2012 = pd.read_csv(IN_PATH_AUSTIN_PM25_2012)
austin_pm25_2011 = pd.read_csv(IN_PATH_AUSTIN_PM25_2011)
austin_pm25_2010 = pd.read_csv(IN_PATH_AUSTIN_PM25_2010)


austin_pm10_2020 = pd.read_csv(IN_PATH_AUSTIN_PM10_2020)
austin_pm10_2019 = pd.read_csv(IN_PATH_AUSTIN_PM10_2019)
austin_pm10_2018 = pd.read_csv(IN_PATH_AUSTIN_PM10_2018)
austin_pm10_2017 = pd.read_csv(IN_PATH_AUSTIN_PM10_2017)
austin_pm10_2016 = pd.read_csv(IN_PATH_AUSTIN_PM10_2016)
austin_pm10_2015 = pd.read_csv(IN_PATH_AUSTIN_PM10_2015)
austin_pm10_2014 = pd.read_csv(IN_PATH_AUSTIN_PM10_2014)
austin_pm10_2013 = pd.read_csv(IN_PATH_AUSTIN_PM10_2013)
austin_pm10_2012 = pd.read_csv(IN_PATH_AUSTIN_PM10_2012)
austin_pm10_2011 = pd.read_csv(IN_PATH_AUSTIN_PM10_2011)
austin_pm10_2010 = pd.read_csv(IN_PATH_AUSTIN_PM10_2010)


austin_no2_2020 = pd.read_csv(IN_PATH_AUSTIN_NO2_2020)
austin_no2_2019 = pd.read_csv(IN_PATH_AUSTIN_NO2_2019)
austin_no2_2018 = pd.read_csv(IN_PATH_AUSTIN_NO2_2018)
austin_no2_2017 = pd.read_csv(IN_PATH_AUSTIN_NO2_2017)
austin_no2_2016 = pd.read_csv(IN_PATH_AUSTIN_NO2_2016)
austin_no2_2015 = pd.read_csv(IN_PATH_AUSTIN_NO2_2015)
austin_no2_2014 = pd.read_csv(IN_PATH_AUSTIN_NO2_2014)
austin_no2_2013 = pd.read_csv(IN_PATH_AUSTIN_NO2_2013)
austin_no2_2012 = pd.read_csv(IN_PATH_AUSTIN_NO2_2012)
austin_no2_2011 = pd.read_csv(IN_PATH_AUSTIN_NO2_2011)
austin_no2_2010 = pd.read_csv(IN_PATH_AUSTIN_NO2_2010)

houston_pm25_2020 = pd.read_csv(IN_PATH_HOUSTON_PM25_2020)
houston_pm25_2019 = pd.read_csv(IN_PATH_HOUSTON_PM25_2019)
houston_pm25_2018 = pd.read_csv(IN_PATH_HOUSTON_PM25_2018)
houston_pm25_2017 = pd.read_csv(IN_PATH_HOUSTON_PM25_2017)
houston_pm25_2016 = pd.read_csv(IN_PATH_HOUSTON_PM25_2016)
houston_pm25_2015 = pd.read_csv(IN_PATH_HOUSTON_PM25_2015)
houston_pm25_2014 = pd.read_csv(IN_PATH_HOUSTON_PM25_2014)
houston_pm25_2013 = pd.read_csv(IN_PATH_HOUSTON_PM25_2013)
houston_pm25_2012 = pd.read_csv(IN_PATH_HOUSTON_PM25_2012)
houston_pm25_2011 = pd.read_csv(IN_PATH_HOUSTON_PM25_2011)
houston_pm25_2010 = pd.read_csv(IN_PATH_HOUSTON_PM25_2010)


houston_pm10_2020 = pd.read_csv(IN_PATH_HOUSTON_PM10_2020)
houston_pm10_2019 = pd.read_csv(IN_PATH_HOUSTON_PM10_2019)
houston_pm10_2018 = pd.read_csv(IN_PATH_HOUSTON_PM10_2018)
houston_pm10_2017 = pd.read_csv(IN_PATH_HOUSTON_PM10_2017)
houston_pm10_2016 = pd.read_csv(IN_PATH_HOUSTON_PM10_2016)
houston_pm10_2015 = pd.read_csv(IN_PATH_HOUSTON_PM10_2015)
houston_pm10_2014 = pd.read_csv(IN_PATH_HOUSTON_PM10_2014)
houston_pm10_2013 = pd.read_csv(IN_PATH_HOUSTON_PM10_2013)
houston_pm10_2012 = pd.read_csv(IN_PATH_HOUSTON_PM10_2012)
houston_pm10_2011 = pd.read_csv(IN_PATH_HOUSTON_PM10_2011)
houston_pm10_2010 = pd.read_csv(IN_PATH_HOUSTON_PM10_2010)

houston_no2_2020 = pd.read_csv(IN_PATH_HOUSTON_NO2_2020)
houston_no2_2019 = pd.read_csv(IN_PATH_HOUSTON_NO2_2019)
houston_no2_2018 = pd.read_csv(IN_PATH_HOUSTON_NO2_2018)
houston_no2_2017 = pd.read_csv(IN_PATH_HOUSTON_NO2_2017)
houston_no2_2016 = pd.read_csv(IN_PATH_HOUSTON_NO2_2016)
houston_no2_2015 = pd.read_csv(IN_PATH_HOUSTON_NO2_2015)
houston_no2_2014 = pd.read_csv(IN_PATH_HOUSTON_NO2_2014)
houston_no2_2013 = pd.read_csv(IN_PATH_HOUSTON_NO2_2013)
houston_no2_2012 = pd.read_csv(IN_PATH_HOUSTON_NO2_2012)
houston_no2_2011 = pd.read_csv(IN_PATH_HOUSTON_NO2_2011)
houston_no2_2010 = pd.read_csv(IN_PATH_HOUSTON_NO2_2010)


dallas_pm25_2020 = pd.read_csv(IN_PATH_DALLAS_PM25_2020)
dallas_pm25_2019 = pd.read_csv(IN_PATH_DALLAS_PM25_2019)
dallas_pm25_2018 = pd.read_csv(IN_PATH_DALLAS_PM25_2018)
dallas_pm25_2017 = pd.read_csv(IN_PATH_DALLAS_PM25_2017)
dallas_pm25_2016 = pd.read_csv(IN_PATH_DALLAS_PM25_2016)
dallas_pm25_2015 = pd.read_csv(IN_PATH_DALLAS_PM25_2015)
dallas_pm25_2014 = pd.read_csv(IN_PATH_DALLAS_PM25_2014)
dallas_pm25_2013 = pd.read_csv(IN_PATH_DALLAS_PM25_2013)
dallas_pm25_2012 = pd.read_csv(IN_PATH_DALLAS_PM25_2012)
dallas_pm25_2011 = pd.read_csv(IN_PATH_DALLAS_PM25_2011)
dallas_pm25_2010 = pd.read_csv(IN_PATH_DALLAS_PM25_2010)


dallas_pm10_2020 = pd.read_csv(IN_PATH_DALLAS_PM10_2020)
dallas_pm10_2019 = pd.read_csv(IN_PATH_DALLAS_PM10_2019)
dallas_pm10_2018 = pd.read_csv(IN_PATH_DALLAS_PM10_2018)
dallas_pm10_2017 = pd.read_csv(IN_PATH_DALLAS_PM10_2017)
dallas_pm10_2016 = pd.read_csv(IN_PATH_DALLAS_PM10_2016)
dallas_pm10_2015 = pd.read_csv(IN_PATH_DALLAS_PM10_2015)
dallas_pm10_2014 = pd.read_csv(IN_PATH_DALLAS_PM10_2014)
dallas_pm10_2013 = pd.read_csv(IN_PATH_DALLAS_PM10_2013)
dallas_pm10_2012 = pd.read_csv(IN_PATH_DALLAS_PM10_2012)
dallas_pm10_2011 = pd.read_csv(IN_PATH_DALLAS_PM10_2011)
dallas_pm10_2010 = pd.read_csv(IN_PATH_DALLAS_PM10_2010)


dallas_no2_2020 = pd.read_csv(IN_PATH_DALLAS_NO2_2020)
dallas_no2_2019 = pd.read_csv(IN_PATH_DALLAS_NO2_2019)
dallas_no2_2018 = pd.read_csv(IN_PATH_DALLAS_NO2_2018)
dallas_no2_2017 = pd.read_csv(IN_PATH_DALLAS_NO2_2017)
dallas_no2_2016 = pd.read_csv(IN_PATH_DALLAS_NO2_2016)
dallas_no2_2015 = pd.read_csv(IN_PATH_DALLAS_NO2_2015)
dallas_no2_2014 = pd.read_csv(IN_PATH_DALLAS_NO2_2014)
dallas_no2_2013 = pd.read_csv(IN_PATH_DALLAS_NO2_2013)
dallas_no2_2012 = pd.read_csv(IN_PATH_DALLAS_NO2_2012)
dallas_no2_2011 = pd.read_csv(IN_PATH_DALLAS_NO2_2011)
dallas_no2_2010 = pd.read_csv(IN_PATH_DALLAS_NO2_2010)


los_angeles_pm25_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2020)
los_angeles_pm25_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2019)
los_angeles_pm25_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2018)
los_angeles_pm25_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2017)
los_angeles_pm25_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2016)
los_angeles_pm25_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2015)
los_angeles_pm25_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2014)
los_angeles_pm25_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2013)
los_angeles_pm25_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2012)
los_angeles_pm25_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2011)
los_angeles_pm25_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_PM25_2010)


los_angeles_pm10_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2020)
los_angeles_pm10_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2019)
los_angeles_pm10_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2018)
los_angeles_pm10_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2017)
los_angeles_pm10_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2016)
los_angeles_pm10_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2015)
los_angeles_pm10_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2014)
los_angeles_pm10_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2013)
los_angeles_pm10_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2012)
los_angeles_pm10_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2011)
los_angeles_pm10_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_PM10_2010)


los_angeles_no2_2020 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2020)
los_angeles_no2_2019 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2019)
los_angeles_no2_2018 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2018)
los_angeles_no2_2017 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2017)
los_angeles_no2_2016 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2016)
los_angeles_no2_2015 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2015)
los_angeles_no2_2014 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2014)
los_angeles_no2_2013 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2013)
los_angeles_no2_2012 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2012)
los_angeles_no2_2011 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2011)
los_angeles_no2_2010 = pd.read_csv(IN_PATH_LOS_ANGELES_NO2_2010)


new_york_pm25_2020 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2020)
new_york_pm25_2019 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2019)
new_york_pm25_2018 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2018)
new_york_pm25_2017 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2017)
new_york_pm25_2016 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2016)
new_york_pm25_2015 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2015)
new_york_pm25_2014 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2014)
new_york_pm25_2013 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2013)
new_york_pm25_2012 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2012)
new_york_pm25_2011 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2011)
new_york_pm25_2010 = pd.read_csv(IN_PATH_NEW_YORK_PM25_2010)


new_york_pm10_2020 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2020)
new_york_pm10_2019 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2019)
new_york_pm10_2018 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2018)
new_york_pm10_2017 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2017)
new_york_pm10_2016 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2016)
new_york_pm10_2015 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2015)
new_york_pm10_2014 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2014)
new_york_pm10_2013 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2013)
new_york_pm10_2012 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2012)
new_york_pm10_2011 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2011)
new_york_pm10_2010 = pd.read_csv(IN_PATH_NEW_YORK_PM10_2010)

new_york_no2_2020 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2020)
new_york_no2_2019 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2019)
new_york_no2_2018 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2018)
new_york_no2_2017 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2017)
new_york_no2_2016 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2016)
new_york_no2_2015 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2015)
new_york_no2_2014 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2014)
new_york_no2_2013 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2013)
new_york_no2_2012 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2012)
new_york_no2_2011 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2011)
new_york_no2_2010 = pd.read_csv(IN_PATH_NEW_YORK_NO2_2010)

def clean_weather_data_city(IN_PATH):
    city_weather_data = (pd.read_csv(IN_PATH))
    city_weather_data.set_index(pd.DatetimeIndex(city_weather_data['DATE']),inplace=True)   
    city_weather_data.drop(['DATE','STATION','NAME'],axis=1,inplace=True)
    #city_weather_data.columns[14:]=city_weather_data.columns[14:].fillna(0，inplace = True)
    city_weather_data.iloc[:,13:] = city_weather_data.iloc[:,13:].fillna(value = 0)
    return city_weather_data

austin_weather = clean_weather_data_city(AUSTIN_WEATHER_URL)
dallas_weather = clean_weather_data_city(DALLAS_WEATHER_URL)
houston_weather = clean_weather_data_city(HOUSTON_WEATHER_URL)
los_angeles_weather = clean_weather_data_city(LOS_ANGELES_WEATHER_URL)
new_york_weather = clean_weather_data_city(NEW_YORK_WEATHER_URL)

def clean_city_pm25(city_pm25_data):    
    city_pm25_data['Date']=pd.to_datetime(city_pm25_data['Date'])
    
    pm25_station_date_mean=city_pm25_data.groupby(['Date','Site ID'])['Daily Mean PM2.5 Concentration'].mean()
    pm25_date_mean=pm25_station_date_mean.groupby('Date').mean().to_frame()
    pm25_aqi_station_date_mean=city_pm25_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    pm25_aqi_date_mean=pm25_aqi_station_date_mean.groupby('Date').mean().to_frame()
    
    city_pm25_data=pd.merge(pm25_date_mean,pm25_aqi_date_mean,how='outer', left_index=True, right_index=True)
    city_pm25_data.columns = ['Daily Mean PM2.5 Concentration', 'DAILY AQI VALUE PM25']
    return city_pm25_data

def merge_10_years_pm25(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    d0 = clean_city_pm25(a0)
    d1 = clean_city_pm25(a1)
    d2 = clean_city_pm25(a2)
    d3 = clean_city_pm25(a3)
    d4 = clean_city_pm25(a4)
    d5 = clean_city_pm25(a5)
    d6 = clean_city_pm25(a6)
    d7 = clean_city_pm25(a7)
    d8 = clean_city_pm25(a8)
    d9 = clean_city_pm25(a9)
    d10 = clean_city_pm25(a10)
    frames=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
    merge_data=pd.concat(frames,join='outer')
    return merge_data

austin_pm25 = merge_10_years_pm25(austin_pm25_2010,austin_pm25_2011,austin_pm25_2012,austin_pm25_2013,austin_pm25_2014,austin_pm25_2015,austin_pm25_2016,austin_pm25_2017,austin_pm25_2018,austin_pm25_2019,austin_pm25_2020)

dallas_pm25 = merge_10_years_pm25(dallas_pm25_2010,dallas_pm25_2011,dallas_pm25_2012,dallas_pm25_2013,dallas_pm25_2014,dallas_pm25_2015,dallas_pm25_2016,dallas_pm25_2017,dallas_pm25_2018,dallas_pm25_2019,dallas_pm25_2020)

houston_pm25 = merge_10_years_pm25(houston_pm25_2010,houston_pm25_2011,houston_pm25_2012,houston_pm25_2013,houston_pm25_2014,houston_pm25_2015,houston_pm25_2016,houston_pm25_2017,houston_pm25_2018,houston_pm25_2019,houston_pm25_2020)

los_angeles_pm25 = merge_10_years_pm25(los_angeles_pm25_2010,los_angeles_pm25_2011,los_angeles_pm25_2012,los_angeles_pm25_2013,los_angeles_pm25_2014,los_angeles_pm25_2015,los_angeles_pm25_2016,los_angeles_pm25_2017,los_angeles_pm25_2018,los_angeles_pm25_2019,los_angeles_pm25_2020)

new_york_pm25 = merge_10_years_pm25(new_york_pm25_2010,new_york_pm25_2011,new_york_pm25_2012,new_york_pm25_2013,new_york_pm25_2014,new_york_pm25_2015,new_york_pm25_2016,new_york_pm25_2017,new_york_pm25_2018,new_york_pm25_2019,new_york_pm25_2020)






def clean_city_pm10(city_pm10_data):
    city_pm10_data['Date']=pd.to_datetime(city_pm10_data['Date'])
    
    pm10_station_date_mean=city_pm10_data.groupby(['Date','Site ID'])['Daily Mean PM10 Concentration'].mean()
    pm10_date_mean=pm10_station_date_mean.groupby('Date').mean().to_frame()
    
    pm10_aqi_station_date_mean=city_pm10_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    pm10_aqi_date_mean=pm10_aqi_station_date_mean.groupby('Date').mean().to_frame()
    
    city_pm10_data=pd.merge(pm10_date_mean,pm10_aqi_date_mean,how='outer', left_index=True, right_index=True)
    city_pm10_data.columns = ['Daily Mean PM10 Concentration', 'DAILY AQI VALUE PM10']
    return city_pm10_data

def merge_10_years_pm10(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    d0 = clean_city_pm10(a0)
    d1 = clean_city_pm10(a1)
    d2 = clean_city_pm10(a2)
    d3 = clean_city_pm10(a3)
    d4 = clean_city_pm10(a4)
    d5 = clean_city_pm10(a5)
    d6 = clean_city_pm10(a6)
    d7 = clean_city_pm10(a7)
    d8 = clean_city_pm10(a8)
    d9 = clean_city_pm10(a9)
    d10 = clean_city_pm10(a10)
    frames=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
    merge_data=pd.concat(frames,join='outer')
    return merge_data

austin_pm10 = merge_10_years_pm10(austin_pm10_2010,austin_pm10_2011,austin_pm10_2012,austin_pm10_2013,austin_pm10_2014,austin_pm10_2015,austin_pm10_2016,austin_pm10_2017,austin_pm10_2018,austin_pm10_2019,austin_pm10_2020)

dallas_pm10 = merge_10_years_pm10(dallas_pm10_2010,dallas_pm10_2011,dallas_pm10_2012,dallas_pm10_2013,dallas_pm10_2014,dallas_pm10_2015,dallas_pm10_2016,dallas_pm10_2017,dallas_pm10_2018,dallas_pm10_2019,dallas_pm10_2020)

houston_pm10 = merge_10_years_pm10(houston_pm10_2010,houston_pm10_2011,houston_pm10_2012,houston_pm10_2013,houston_pm10_2014,houston_pm10_2015,houston_pm10_2016,houston_pm10_2017,houston_pm10_2018,houston_pm10_2019,houston_pm10_2020)

los_angeles_pm10 = merge_10_years_pm10(los_angeles_pm10_2010,los_angeles_pm10_2011,los_angeles_pm10_2012,los_angeles_pm10_2013,los_angeles_pm10_2014,los_angeles_pm10_2015,los_angeles_pm10_2016,los_angeles_pm10_2017,los_angeles_pm10_2018,los_angeles_pm10_2019,los_angeles_pm10_2020)

new_york_pm10 = merge_10_years_pm10(new_york_pm10_2010,new_york_pm10_2011,new_york_pm10_2012,new_york_pm10_2013,new_york_pm10_2014,new_york_pm10_2015,new_york_pm10_2016,new_york_pm10_2017,new_york_pm10_2018,new_york_pm10_2019,new_york_pm10_2020)





def clean_city_no2(city_no2_data):
    city_no2_data['Date']=pd.to_datetime(city_no2_data['Date'])
    
    no2_station_date_mean=city_no2_data.groupby(['Date','Site ID'])['Daily Max 1-hour NO2 Concentration'].mean()
    no2_date_mean=no2_station_date_mean.groupby('Date').mean().to_frame()
    
    no2_aqi_station_date_mean=city_no2_data.groupby(['Date','Site ID'])['DAILY_AQI_VALUE'].mean()
    no2_aqi_date_mean=no2_aqi_station_date_mean.groupby('Date').mean().to_frame()
    
    city_no2_data=pd.merge(no2_date_mean,no2_aqi_date_mean,how='outer', left_index=True, right_index=True)
    city_no2_data.columns = ['Daily Mean NO2 Concentration', 'DAILY AQI VALUE NO2']
    return city_no2_data

def merge_10_years_no2(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10):
    d0 = clean_city_no2(a0)
    d1 = clean_city_no2(a1)
    d2 = clean_city_no2(a2)
    d3 = clean_city_no2(a3)
    d4 = clean_city_no2(a4)
    d5 = clean_city_no2(a5)
    d6 = clean_city_no2(a6)
    d7 = clean_city_no2(a7)
    d8 = clean_city_no2(a8)
    d9 = clean_city_no2(a9)
    d10 = clean_city_no2(a10)
    frames=[d0,d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
    merge_data=pd.concat(frames,join='outer')
    return merge_data

austin_no2 = merge_10_years_no2(austin_no2_2010,austin_no2_2011,austin_no2_2012,austin_no2_2013,austin_no2_2014,austin_no2_2015,austin_no2_2016,austin_no2_2017,austin_no2_2018,austin_no2_2019,austin_no2_2020)

dallas_no2 = merge_10_years_no2(dallas_no2_2010,dallas_no2_2011,dallas_no2_2012,dallas_no2_2013,dallas_no2_2014,dallas_no2_2015,dallas_no2_2016,dallas_no2_2017,dallas_no2_2018,dallas_no2_2019,dallas_no2_2020)

houston_no2 = merge_10_years_no2(houston_no2_2010,houston_no2_2011,houston_no2_2012,houston_no2_2013,houston_no2_2014,houston_no2_2015,houston_no2_2016,houston_no2_2017,houston_no2_2018,houston_no2_2019,houston_no2_2020)

los_angeles_no2 = merge_10_years_no2(los_angeles_no2_2010,los_angeles_no2_2011,los_angeles_no2_2012,los_angeles_no2_2013,los_angeles_no2_2014,los_angeles_no2_2015,los_angeles_no2_2016,los_angeles_no2_2017,los_angeles_no2_2018,los_angeles_no2_2019,los_angeles_no2_2020)

new_york_no2 = merge_10_years_no2(new_york_no2_2010,new_york_no2_2011,new_york_no2_2012,new_york_no2_2013,new_york_no2_2014,new_york_no2_2015,new_york_no2_2016,new_york_no2_2017,new_york_no2_2018,new_york_no2_2019,new_york_no2_2020)







def city_merge_air_pollution(pm25data, pm10data, no2data):
    city_air_pollution = pd.merge(pm25data, pm10data, how='outer', left_index=True, right_index=True)
    city_air_pollution = pd.merge(city_air_pollution, no2data, how='outer', left_index=True, right_index=True)
    
    return city_air_pollution

austin_air_pollution = city_merge_air_pollution(austin_pm25, austin_pm10, austin_no2)
dallas_air_pollution = city_merge_air_pollution(dallas_pm25, dallas_pm10, dallas_no2)
houston_air_pollution = city_merge_air_pollution(houston_pm25, houston_pm10, houston_no2)
los_angeles_air_pollution = city_merge_air_pollution(los_angeles_pm25, los_angeles_pm10, los_angeles_no2)
new_york_air_pollution = city_merge_air_pollution(new_york_pm25, new_york_pm10, new_york_no2)


def city_merge_weather_pollution(city_weather_data, city_air_pollution_data):
    city_merge = pd.merge(city_weather_data, city_air_pollution_data, how = 'outer', left_index = True, right_index= True )
    return city_merge

austin = city_merge_weather_pollution(austin_weather, austin_air_pollution)
dallas = city_merge_weather_pollution(dallas_weather, dallas_air_pollution)
houston = city_merge_weather_pollution(houston_weather, houston_air_pollution)
los_angeles = city_merge_weather_pollution(los_angeles_weather, los_angeles_air_pollution)
new_york = city_merge_weather_pollution(new_york_weather, new_york_air_pollution)


austin['CITY'] = 'AUSTIN'
dallas['CITY'] = 'DALLAS'
houston['CITY'] = 'HOUSTON'
los_angeles['CITY'] = 'LOS_ANGELES'
new_york['CITY'] = 'NEW_YORK'
city_frame = [austin, dallas, houston, los_angeles, new_york]
data_five_cities = pd.concat(city_frame, axis = 0, join='inner')
# -
# --

print(austin.info())

import statsmodels.formula.api as sm

# +
new_york_select = new_york.loc[(new_york['PRCP'] > 0) & (new_york['AWND'] > 0) & (new_york['SNWD'] > 0) , :].assign(log_base_PRCP = lambda x:np.log(x['PRCP'])).assign(log_base_AWND = lambda x:np.log(x['AWND'])).assign(log_base_SNWD = lambda x:np.log(x['SNWD']))


results = sm.ols('Q("Daily Mean PM2.5 Concentration") ~log_base_PRCP + log_base_AWND + log_base_SNWD', data=new_york_select).fit()

results.summary()

# +
new_york_select = new_york.loc[(new_york['PRCP'] > 0) & (new_york['AWND'] > 0) & (new_york['SNWD'] > 0) , :].assign(log_base_PRCP = lambda x:np.log(x['PRCP'])).assign(log_base_AWND = lambda x:np.log(x['AWND'])).assign(log_base_SNWD = lambda x:np.log(x['SNWD']))


results = sm.ols('Q("DAILY AQI VALUE PM25") ~log_base_PRCP + log_base_AWND + log_base_SNWD', data=new_york_select).fit()

results.summary()

# +
data_five_cities_select = data_five_cities.loc[(data_five_cities['PRCP'] > 0) & (data_five_cities['AWND'] > 0) & (data_five_cities['SNWD'] > 0),:].assign(lag_WT01 = lambda x:x['WT01'].shift()).assign(log_base_PRCP = lambda x:np.log(x['PRCP'])).assign(log_base_AWND = lambda x:np.log(x['AWND'])).assign(log_base_SNWD = lambda x:np.log(x['SNWD'])).assign(log_base_TAVG =lambda x:np.log(x['TAVG'])).assign(lag_PM25  = lambda x:x['Daily Mean PM2.5 Concentration'].shift())

results = sm.ols('Q("Daily Mean PM2.5 Concentration") ~lag_WT01 + log_base_PRCP + log_base_AWND + log_base_SNWD + lag_PM25', data=data_five_cities_select).fit()
results.summary()

# +
data_five_cities_select = data_five_cities.loc[(data_five_cities['PRCP'] > 0) & (data_five_cities['AWND'] > 0) & (data_five_cities['SNWD'] > 0),:].assign(lag_WT01 = lambda x:x['WT01'].shift()).assign(log_base_PRCP = lambda x:np.log(x['PRCP'])).assign(log_base_AWND = lambda x:np.log(x['AWND'])).assign(log_base_SNWD = lambda x:np.log(x['SNWD'])).assign(log_base_TAVG =lambda x:np.log(x['TAVG'])).assign(lag_PM25  = lambda x:x['Daily Mean PM2.5 Concentration'].shift())

results = sm.ols('Q("DAILY AQI VALUE PM25") ~lag_WT01 + log_base_PRCP + log_base_AWND + log_base_SNWD + lag_PM25', data=data_five_cities_select).fit()
results.summary()
# -






