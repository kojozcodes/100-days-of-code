import requests
from datetime import datetime

MY_LAT = 9.076479
MY_LONG = 7.398574

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position_tuple = (longitude, latitude)
# print(iss_position_tuple)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = str(int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 1)
sunset = str(int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 1)
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
