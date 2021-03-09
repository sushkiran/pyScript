"""
Q3: Create a script called weather that return the environmental parameters
(temperature (min, max), windspeed, humidity, cloud, pressure, sunrise and sunset) of any location you want;
after passing arguments (like user api and city id).
"""

# pip install pyowm

from pytz import timezone
from pyowm import OWM

my_api_key = 'dab84445806ee7dc52aabaa47276f95d'
wm = OWM(my_api_key).weather_manager()

city= 'Singapore'
weather = wm.weather_at_place(city).weather

print('------------------------------------------')
print('City Weather Details:', str.upper(city))
print('------------------------------------------')

print('Current Weather:', weather.detailed_status)

print('Temperature:', weather.temperature('celsius').get('temp'), 'deg celsius')
print('Min Temperature:', weather.temperature('celsius').get('temp_min'), 'deg celsius')
print('Max Temperature:', weather.temperature('celsius').get('temp_max'), 'deg celsius')

print('Wind Speed:', weather.wind().get('speed'), 'metres per second')
print('Humidity:', weather.humidity, '%')
print('Number of clouds:', weather.clouds)

print('Pressure:', weather.pressure.get('press'))
print('Sunrise:', weather.sunrise_time(timeformat='date').astimezone(timezone('Asia/Singapore')).strftime('%X'))
print('Sunset:', weather.sunset_time(timeformat='date').astimezone(timezone('Asia/Singapore')).strftime('%X'))




