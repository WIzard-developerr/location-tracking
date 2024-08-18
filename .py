import phonenumbers
import folium
from myphone import number  # Ensure myphone.py contains 'number = "<your_phone_number>"'

from phonenumbers import geocoder, carrier

# Parsing the phone number
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

# Getting the carrier name
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

# Using OpenCage Geocode API to get latitude and longitude
from opencage.geocoder import OpenCageGeocode

key = 'd221219de2b346748ae3e131ee3a9a2f'  # This key should be kept secret

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(lat, lng)

    
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    
    myMap.save("mylocation.html")
else:
    print("Location not found")



