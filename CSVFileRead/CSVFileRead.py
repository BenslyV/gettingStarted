import csv

# opening the CSV file
with open('weather_data.csv') as file:
    # reading the CSV file
    csvFile = csv.reader(file)
    temp = []
    print(type(temp))

    # displaying the contents of the CSV file
    for lines in csvFile:
        print(lines)


