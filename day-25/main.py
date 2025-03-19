# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# monday_temp_f = monday.temp[0] * (9/5) + 32
# print(monday_temp_f)
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 55, 78]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_csv_file")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrels_colors = data["Primary Fur Color"]
gray_squirrels = data[squirrels_colors == "Gray"]
red_squirrels = data[squirrels_colors == "Cinnamon"]
black_squirrels = data[squirrels_colors == "Black"]

squirrel_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(gray_squirrels), len(red_squirrels), len(black_squirrels)]
}

squirrel_count_data = pandas.DataFrame(squirrel_count)
squirrel_count_data.to_csv("squirrel_count")

print(gray_squirrels)

