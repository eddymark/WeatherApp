import requests
import json

# zip=11237&apikey=0ba6294d35fd4d0ade6224193d18de15")
payload = {"zip": "11237", "units": "imperial", "apikey": "0ba6294d35fd4d0ade6224193d18de15"}

weather_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=payload)

json_root = weather_requests.text

json_string = json.loads(json_root)

# Weather temp
main = json_string["main"]
temp = int(main["temp"])

# Max/Min temp
temp_max = int(main["temp_max"])
temp_min = int(main["temp_min"])

# Humidity
humidity = main["humidity"]

# Description
weather = json_string["weather"]
weather_arr = weather[0]
main_description = weather_arr["main"]

# Coordinates
coord = json_string["coord"]
lat = coord["lat"]
lon = coord["lon"]

# City
city = json_string["name"]

print(city)
print("Temperature: {}".format(temp))
print("Humidity: {}%".format(humidity))
print("Max/Min: {}/{}".format(temp_max, temp_min))
print("Description: {}".format(main_description))
print("Lattitude: {} \nLongitude: {}".format(lat, lon))

print(json_root)

