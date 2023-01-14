# import smtplib
#
# my_email = "nortepedro294@gmail.com"
# password = "hgarrnsctzecxxtx"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="dr.pedronorte@yahoo.com",
#                         msg="Subject:Hello World!\n\nThis is the body of my email. Version 3")


import datetime as dt
now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of = now.weekday()

# create own datetime object
date_of_birth = dt.datetime(year=2000, month=1, day=1)
print(date_of_birth)
