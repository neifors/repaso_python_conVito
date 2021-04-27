
from functools import partial
from geopy.geocoders import Nominatim
import time
import math

geo = Nominatim(user_agent="MyApp")

loc = geo.geocode("Calle de Francisco Silvela 76")
print(loc)
print(loc.latitude, loc.longitude)


# geolocator = Nominatim(user_agent="caca")
# location = geolocator.reverse("52.509669, 13.376294")
# print(location.address)
# # Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
# print((location.latitude, location.longitude))



# geocode = partial(geolocator.geocode, language="es")
# print(geocode("london"))
# # Londres, Greater London, Inglaterra, SW1A 2DX, Gran Bretaña
# print(geocode("paris"))
# # París, Isla de Francia, Francia metropolitana, Francia
# print(geocode("paris", language="en"))
# # Paris, Ile-de-France, Metropolitan France, France

# reverse = partial(geolocator.reverse, language="es")
# print(reverse("52.509669, 13.376294"))