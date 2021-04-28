import csv
reader = csv.reader(open("2021-04-26_dht22_sensor_3660.csv"), delimiter=";")
for row in reader:
   print(f'Zeit: {row[5]} Temperatur: {row[6]} C°')
