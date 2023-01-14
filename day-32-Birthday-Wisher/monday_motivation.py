# Monday Motivational Quotes Email Generator
import smtplib
import datetime as dt
import random

# Constants
MY_EMAIL = "nortepedro294@gmail.com"
MY_PASS = "hgarrnsctzecxxtx"
QUOTE = ""


# Functions
def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASS)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="dr.pedronorte@yahoo.com",
                            msg=f"Subject:Happy Monday!\n\nHere's a Monday Motivation Quote:\n\n {QUOTE}.")


def get_quotes():
    global QUOTE
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        QUOTE = random.choice(all_quotes)


# Conditionals
now = dt.datetime.now()
day_of = now.weekday()

if day_of == 0:
    get_quotes()
    send_email()
