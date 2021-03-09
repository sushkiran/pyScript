"""
Q2: Create a script called location that return the location parameters of any location you want.
"""

from geopy.geocoders import Nominatim
import time
from pprint import pprint


# This function returns a location as raw from an address will repeat until success
def get_location_by_address(address):
    time.sleep(1)
    try:
        return app.geocode(address).raw
    except:
        return get_location_by_address(address)


if __name__ == '__main__':
    # instantiate a new Nominatim client
    app = Nominatim(user_agent="tutorial")
    address = "617C, Punggol Drive, Singapore"
    location = get_location_by_address(address)
    pprint(location)
