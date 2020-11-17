
from geopy.geocoders import Nominatim


class Location:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


    def get_alias_name(self):
        return Nominatim.geolocator.reverse(self.lat, self.lon)


