# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["temp"])
# data_dict = data.to_dict()

# TO PULL UP THE COLUMN
# temp_list = data["temp"].to_list()
# print(temp_list)
# print(f"Average is {sum(temp_list) / len(temp_list)}")

# average = data["temp"].mean()
# print(f"Average: {average}")
# print(data["temp"].max())

# TO PULL UP THE ROW
# row = data[data["day"] == "Monday"]
# print(row)

# maximum = data["temp"].max()
# hottest_day = data[data["temp"] == maximum]
# print(hottest_day)

# monday = data[data["day"] == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * (9/5) + 32
# print(monday_temp_F)

# Create a Dataframe from Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
#
# # Convert the Dataframe
# new_data.to_csv("new_file.csv")

# ---OUTPUT---
# 2018 Central Park Squirrel Census - Squirrel Data
# Source: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw
# Produce table : Fur Color, Count
# "Primary Fur Color" col 9
# "Gray" "Cinnamon" "Black"
data = pandas.read_csv("2018_Squirrel_Data.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrels = data[data["Primary Fur Color"] == "Black"]

gray_squirrels_count = len(gray_squirrels)
cinnamon_squirrels_count = len(cinnamon_squirrels)
black_squirrels_count = len(black_squirrels)

# TEST
# print(gray_squirrels_count)
# print(cinnamon_squirrels_count)
# print(black_squirrels_count)

# NEW TABLE OF SUMMARY
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Squirrel Fur Summary.csv")
