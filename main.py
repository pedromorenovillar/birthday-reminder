import pandas
import os
import datetime as dt
from email_sender import send_email

# Load birthday data from csv and check if birthday found
data = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
month_letters = dt.datetime.now().strftime("%B")
this_month = now.month
this_day = now.day
found_birthday = data.query(f'month == {this_month} and day == {this_day}')
recipient_email = os.getenv("email_recipient")

if found_birthday.empty:
    pass
else:
    name = found_birthday["name"].item()
    subject = f"Today is {name}'s birthday! 🎂"
    email_contents = f"Say 'Happy Birthday' to {name}, who was born today, {this_day} of {month_letters}."
    send_email(recipient_email=recipient_email, subject=subject,
               contents=f"{email_contents}")
