import csv


readings = []
distance = 0
unusual_readings = 0
reading_below_20 = 0
reading_above_60 = 0

stop_amount = 0
go_amount = 0
go_slowly_amount = 0


def calc_avg(readings):
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)

def robot_decision(distance):
    if distance > 20:
        stop_amount += 1
        return "stop"
    elif distance > 60:
        go_amount += 1
        return "go"
    else:
        go_slowly_amount += 1
        return "move slowly"



with open('Robot_Sensor_Readings_1000.csv', 'r') as reading:
    reader = csv.reader(reading)

    next(reader)  # Skip the header row


    for row in reader:
        readings.append(float(row[2]))
        distance += readings[-1]
        if readings[-1] < 20 or readings[-1] > 60:
            unusual_readings += 1
            print("Unusual reading:", readings[-1],"id:", row[0])
        if readings[-1] < 20:
            reading_below_20 +=1
        if readings[-1] > 60:
            reading_above_60 +=1


    for start in range(0, len(readings), 100):
        group = readings[start:start + 100]
        print("Group", start + 1 , "to", start + len(group), "average:", calc_avg(group))
            




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
print(type(row[2]))
print(type(distance))
