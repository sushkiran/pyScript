'''
Write a program to find distance between two locations when their latitude and
longitudes are given.
Hint: Use math module.
'''

from math import radians, cos, sin, asin, sqrt


class City:

    def __init__(self, lat, lon):
        self.latitude = radians(lat)
        self.longitude = radians(lon)


def calc_dist(city1, city2):
    dlon = city2.longitude - city1.longitude
    dlat = city2.latitude - city1.latitude

    a = sin(dlat / 2) ** 2 + cos(city1.latitude) * cos(city2.latitude) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))

    # Radius of earth = 6371 kilometers. Or 3956 miles
    return c * 6371, c * 3956


singapore = City(1.29016, 103.852)
hongkong = City(22.279812, 114.161766)

distance = calc_dist(singapore, hongkong)
text = 'Distance between Singapore & HK is {:.2f} kms or {:.2f} miles'
print(text.format(distance[0], distance[1]))
