import csv

with open("File/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter the name of the city:")

for row in data:
    if row[0] == city:
        print(row[1])