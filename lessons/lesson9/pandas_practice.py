import pandas as pd

# reading data using pandas library
data = pd.read_csv("../lesson9/data/weather_data.csv")
print(data)

# getting column data with pandas
temperature = data["temp"]
print(temperature)

# converting data to dictionary
data_dict = data.to_dict()
print(data_dict)

# converting data to list
temp_list = data["temp"].to_list()
print(temp_list)

# finding the average of temperature
total = 0
length = len(temp_list)
for temp in temp_list:
    total += temp

average = total / length

print(f"Average: {round(average, 2)}")

# finding the highest temperature using pandas.Series
print(f"The highest temperature: {data["temp"].max()}")

# get data in columns
print(data["day"])
print(data.condition)

# get data in rows
data_row = data[data.day == "Wednesday"]
print(data_row)
print(data[data.temp == data.temp.max()])


# convert thursday's temperature to fahrenheit
thursday = data[data.day == "Thursday"]
thursday_temp = thursday.temp[3]

celsius = thursday_temp
fahrenheit = (celsius * 1.8) + 32
print(f"Fahrenheit: {fahrenheit}")


# create a dataframe from scratch
data_student_dict = {"students": ["juliette", "lucas", "leo"], "scores": [78, 68, 84]}

student_data = pd.DataFrame(data_student_dict)
print(student_data)

# creating csv file
student_data.to_csv("students.csv")
