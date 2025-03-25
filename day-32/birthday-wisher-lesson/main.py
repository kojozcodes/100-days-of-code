import random
import datetime as dt
import smtplib

#
my_email = "kojozpythontesting@gmail.com"
password = "onjqkpvjmjcpqgan"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="kojozpythontesting@yahoo.com",
#         msg="Subject: Greetings\n\nHello world, This is the body"
#     )

now = dt.datetime.now()
day_of_the_week = now.weekday()

if day_of_the_week == 0:
    with open("./quotes.txt") as quotes_file:
        quotes = quotes_file.readlines()
        quote_for_the_day = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kojozpythontesting@yahoo.com",
            msg=f"Subject: Quote For The Day\n\n{quote_for_the_day}"
        )
