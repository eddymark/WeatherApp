import requests
import json

# params=payload
# zip=11237&apikey=0ba6294d35fd4d0ade6224193d18de15")
payload = {"zip": "11237", "apikey": "0ba6294d35fd4d0ade6224193d18de15"}

weather_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=payload)

json_root = weather_requests.text

todo = json.loads(json_root)
print(todo)
print(json_root)

