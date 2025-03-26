import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 9.076479  # Your latitude
MY_LONG = 7.398574  # Your longitude
MY_EMAIL = "kojozpythontesting@gmail.com"
MY_PASSWORD = "onjqkpvjmjcpqgan"


def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 1
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 1

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="kojolihamza@gmail.com",
                msg="Subject:ISS Is Above Your City\n\nHi Hamza,"
                    "\n\nLook Up, The International Space Station is right above you."
            )
