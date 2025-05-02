#The headlights of a car should only automatically turn on when the daylight outside is below 
# a certain threshold. If a sensor threshold is below the number 8, print "Headlights On"; 
# otherwise, print "Headlights Off".

sensor_value = int(input("Enter the daylight threshold (0–10): "))

if sensor_value < 8:
    print("Headlights On")
else:
    print("Headlights Off")
