import requests

API_KEY = "924af808b5caa988a7e03d7bc7fbbb06"

URL="https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat" : 29.882080,
    "lon" : -97.939987,
    "appid" : API_KEY,
    "cnt" : 4
}

response = requests.get(url=URL, params=parameters)
response.raise_for_status()

weather_data = response.json()

need_umbrella = False
for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        need_umbrella = True
    print(item["weather"])

if need_umbrella:
    print("Bring umbrella")
# print(weather_data)

# shiz = {
#   'cod': '200',
#   'message': 0,
#   'cnt': 1,
#   'list': [
#     {
#       'dt': 1740722400,
#       'main': {
#         'temp': 288.04,
#         'feels_like': 286.84,
#         'temp_min': 287.51,
#         'temp_max': 288.04,
#         'pressure': 1023,
#         'sea_level': 1023,
#         'grnd_level': 996,
#         'humidity': 48,
#         'temp_kf': 0.53
#       },
#       'weather': [
#         {
#           'id': 804,
#           'main': 'Clouds',
#           'description': 'overcast clouds',
#           'icon': '04n'
#         }
#       ],
#       'clouds': {
#         'all': 100
#       },
#       'wind': {
#         'speed': 2.78,
#         'deg': 7,
#         'gust': 5.05
#       },
#       'visibility': 10000,
#       'pop': 0,
#       'sys': {
#         'pod': 'n'
#       },
#       'dt_txt': '2025-02-28 06:00:00'
#     }
#   ],
#   'city': {
#     'id': 4726491,
#     'name': 'San Marcos',
#     'coord': {
#       'lat': 29.8821,
#       'lon': -97.94
#     },
#     'country': 'US',
#     'population': 44894,
#     'timezone': -21600,
#     'sunrise': 1740661179,
#     'sunset': 1740702573
#   }
# }