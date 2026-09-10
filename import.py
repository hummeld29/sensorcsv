import csv

readings = []
distance = 0

unusual_readings = 0

reading_below_20 = 0
reading_above_60 = 0




def calc_avg(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)


with open('Robot_Sensor_Readings_1000.csv', 'r') as reading:
    reader = csv.reader(reading)

    next(reader)  # Skip the header row


    for row in reader:
        readings.append(float(row[2]))
        distance += readings[-1]
        if readings[-1] < 20 or readings[-1] > 60:
            unusual_readings += 1
        if readings[-1] < 20:
            reading_below_20 +=1
        if readings[-1] > 60:
            reading_above_60 +=1




print("import report")
print("number of readings:", len(readings))
print("first reading:", readings[0])
print("last reading:", readings[-1])
print("total distance:", distance)
print("min reading:", min(readings))
print("max reading:", max(readings))
print("number of readings below 20:", reading_below_20)
print("number of readings above 60:", reading_above_60)
print("average reading:", calc_avg(readings))
print("number of unusual readings:", unusual_readings) 
print("percentage of unusual readings:", (unusual_readings / len(readings)) * 100, "%")