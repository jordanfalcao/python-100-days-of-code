# # read 'weather_data.csv' file and add each line in a list:
# with open("weather_data.csv") as file:
#     data = []
#     for line in file:
#         new_line = line.strip()
#         data.append(new_line)

# # create a csv object with csv library:
# import csv
# with open("weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# using PANDAS library, very easier
import pandas as pd

# data = pd.read_csv('weather_data.csv')
# print(data['temp'])
# print(data.index)

# data_dict = data.to_dict()
# print(data_dict)

# # get Data in columns
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.temp.min())
#
# # get Data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # set a variable and then get only one column
# monday = data[data.day == "Monday"]
# print(monday.condition)  # print out only the condition of the variable monday
#
# # monday temperature in Fahrenheit
# monday_temp_F = monday.temp * (9/5) + 32
# print(monday_temp_F)

# # create a DataFrame from a scratch
# data_dict = {
#     "students": ["Jordan", "Jams", "Djonga"],
#     "scores": [90, 95, 86]
# }

# new_df = pd.DataFrame(data_dict)

# create a csv file from the DataFrame
# new_df.to_csv("new_data.csv")

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240209.csv')

# # how many squirrels of each color
# print(data.groupby('Primary Fur Color').count())

data_dict = {
    "Fur Color": ['Gray', 'Cinnamon', 'Black'],
    "Count": [2473, 392, 103]
}

#
# new_df = pd.DataFrame(data_dict, columns=['Fur Color', 'Count'], index=[0, 1, 2])
# new_df.to_csv("squirrel_count.csv")