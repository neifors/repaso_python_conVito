
from functools import partial
from geopy.geocoders import Nominatim
import utm


geo = Nominatim(user_agent="MyApp")

geopy_loc = geo.geocode("calle director don jose valverde alvarez 11")
print("\nInformación total dirección:\n",geopy_loc)
print("\nCoordenates using geopy: ",geopy_loc.latitude, geopy_loc.longitude)
utm_loc = utm.to_latlon(442920, 4476081, 30, "N")
print("\nCoordenates using utm: ", utm_loc)

print(f"https://www.google.com/maps/dir/{utm_loc[0]},+{utm_loc[1]}/{geopy_loc.latitude},{geopy_loc.longitude}") #/@40.4326309,-3.67317,17.82z/data=!4m7!4m6!1m3!2m2!1d-3.6729712!2d40.4334126!1m0!3e2
geolocator = Nominatim(user_agent="caca")
location = geolocator.reverse("52.509669, 13.376294")
print(location.address)
# Potsdamer Platz, Mitte, Berlin, 10117, Deutschland, European Union
print((location.latitude, location.longitude))



# geocode = partial(geolocator.geocode, language="es")
# print(geocode("london"))
# # Londres, Greater London, Inglaterra, SW1A 2DX, Gran Bretaña
# print(geocode("paris"))
# # París, Isla de Francia, Francia metropolitana, Francia
# print(geocode("paris", language="en"))
# # Paris, Ile-de-France, Metropolitan France, France

# reverse = partial(geolocator.reverse, language="es")
# print(reverse("52.509669, 13.376294"))


##? CALCULAR DISTANCIAS

from geopy import distance
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)

madrid_silvela = (40.433412600752696, -3.672971216681718)
wellington = (-41.32, 174.81)
salamanca = (40.96, -5.50)
print(distance.distance(madrid_silvela, salamanca).m)