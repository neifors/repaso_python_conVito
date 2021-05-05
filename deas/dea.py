from math import sqrt
from geopy.geocoders import Nominatim
from geopy import distance
import utm


class Dea():
    
    def __init__(self, x, y, id_code, address):
        self.x = float(x)
        self.y = float(y)
        self.id = id_code
        self.address = address
        
    @property
    def longitude(self):
        return utm.to_latlon(self.x, self.y, 30, "N")[0]
        # geo = Nominatim(user_agent="MyApp")
        # loc = geo.geocode(self.address)
        # return loc.longitude
    
    @property
    def latitude(self):
        return utm.to_latlon(self.x, self.y, 30, "N")[1]
        # geo = Nominatim(user_agent="MyApp")
        # loc = geo.geocode(self.address)
        # return loc.latitude
    
    def get_distance(self,x_user,y_user):
        leg1 = abs(x_user - self.x)
        leg2 = abs(y_user - self.y)
        distance = sqrt(leg1**2 + leg2**2)
        return distance
        
    def get_real_distance(self,user_coordinates):
        dea_pos = (self.latitude,self.longitude)
        return distance.distance(user_coordinates,dea_pos ).m
        
    