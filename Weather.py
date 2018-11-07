import requests
import json

# zip=11237&apikey=0ba6294d35fd4d0ade6224193d18de15")
payload = {"zip": "11237", "apikey": "0ba6294d35fd4d0ade6224193d18de15"}

weather_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=payload)

json_root = weather_requests.text

json_string = json.loads(json_root)

# weather temp
main = json_string["main"]
temp = main["temp"]
coord = json_string["coord"]


lat = coord["lat"]
lon = coord["lon"]

print("Temperature: {}".format(temp))
print("Lattitude: {} \nLongitude: {}".format(lat, lon))

print(json_root)

