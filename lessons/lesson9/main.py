import csv

filename = "python-lab/lessons/lesson9/data/weather_data.csv"

# reading csv data
with open(filename) as data_file:
    data = csv.reader(data_file)
    temperature = []

    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))

    print(temperature)
