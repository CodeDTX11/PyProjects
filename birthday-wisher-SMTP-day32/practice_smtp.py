import smtplib
import datetime as dt
import random

password= "kkkq pbcd ygya zmhb"
# pwd = "na"

my_email = "dm5messerly@gmail.com"
test_email = "dylan.messerly@gmail.com"

# message = "Subject: Hello\n\nHello from the other side"
subject_field = "Subject: Motivational Quote of the Day"
now = dt.datetime.now()

if now.weekday() == 2:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()

    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=test_email,
                            msg=f"{subject_field}\n\n{quote}")
        # connection.close() #not needed if using the with syntax above


# dob = dt.datetime(year=1991, month=10, day=28, hour=11)

# print(dob)
