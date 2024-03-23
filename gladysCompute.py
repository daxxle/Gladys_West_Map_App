import math
import gladysSatellite as satellite
"""
    Student: Dang Le
    Module: gladysCompute
    Description: This module does …
"""

def gpsCheck(x, y):
    latitude = longitude = altitude = timesat = -1
    latitude = satellite.gpsValue(x, y, "latitude")
    longitude = satellite.gpsValue(x, y, "longitude")
    altitude = satellite.gpsValue(x, y, "altitude")
    timesat = satellite.gpsValue(x, y, "time")
    print(f"Latitude={latitude}\tLongitude={latitude}\tAltitude={altitude}\tTime={timesat}\t")
    mapCheck=False
    if (latitude>=0) and (longitude>=0) and (altitude>=0) and (timesat>=0):
        print(f"Latitude={latitude}\tLongitude={latitude}\tAltitude={altitude}\tTime={timesat}\t")
        print("This point is on map\n")
        mapCheck=True
    else:
        print("This point is not on map\n")
    return mapCheck

def gpsAverage(x, y):

    value = satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "time") 

    average = value / 4

    return average


def distance(cur, dest):

    distance = math.sqrt(gpsAverage(cur[0], cur[1])**2 + gpsAverage(dest[0], dest[1])**2)

    return distance
