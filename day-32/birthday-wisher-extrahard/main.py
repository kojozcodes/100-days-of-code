# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and
# replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

MY_EMAIL = "kojozpythontesting@gmail.com"
MY_PASSWORD = "onjqkpvjmjcpqgan"

now = dt.datetime.now()
month = now.month
day = now.day

birthdays_data = pandas.read_csv("./birthdays.csv")
birthdays_data_dict = birthdays_data.to_dict(orient="records")

for person in birthdays_data_dict:
    if person["month"] == month and person["day"] == day:
        random_number = random.randint(1, 3)

        with open(f"./letter_templates/letter_{random_number}.txt") as template_file:
            letter = template_file.read()
            letter = letter.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person["email"],
                msg=f"Subject: HAPPY BIRTHDAY\n\n{letter}"
            )
