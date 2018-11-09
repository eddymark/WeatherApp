import requests
import json

class WeatherRequest:
    def __init__(self):
        self.url = "http://api.openweathermap.org/data/2.5/weather?"
        self.key = "0ba6294d35fd4d0ade6224193d18de15"
        self.data = None
        self.getTmp = None
        self.getMax = None
        self.getMin = None

    def makeRequest(self, zipcode):
        payload = {"zip": zipcode, "units": "imperial", "apikey": self.key}
        weather_requests = requests.get(self.url, params=payload)

        json_root = weather_requests.text
        json_string = json.loads(json_root)

        self.setData(json_string)

    def setData(self, json_string):
        # Get all data
        main = json_string["main"]

        # Set data to dictionary
        self.data = {'temp_max': int(main["temp_max"]),
                     'temp_min': int(main["temp_min"]),
                     'humidity': main["humidity"],
                     'weather': json_string["weather"],
                     'main_description': json_string["weather"][0]["main"],
                     'city': json_string["name"],
                     'temperature': int(main["temp"])
                     }

    def get_val(self, key):
        return self.data[key]

    def getData(self):
        return self.data



# print(city)
# print("Temperature: {}".format(temp))
# print("Humidity: {}%".format(humidity))
# print("Max/Min: {}/{}".format(temp_max, temp_min))
# print("Description: {}".format(main_description))
# print("Lattitude: {} \nLongitude: {}".format(lat, lon))
#
# print(json_root)