import math
import gladysSatellite as satellite
"""
    Student: Dang Le
    Module: gladysCompute
    Description: This module does …
"""

def gpsPrint(x, y):
    latitude = satellite.gpsValue(x, y, "latitude")
    longitude = satellite.gpsValue(x, y, "longitude")
    altitude = satellite.gpsValue(x, y, "altitude")
    timesat = satellite.gpsValue(x, y, "time")
    str=f"({x},{y})\tSatellite: Latitude={latitude}\tLongitude={latitude}\tAltitude={altitude}\tTime={timesat}"
    return str

def gpsCheck(x, y):
    latitude = satellite.gpsValue(x, y, "latitude")
    longitude = satellite.gpsValue(x, y, "longitude")
    altitude = satellite.gpsValue(x, y, "altitude")
    timesat = satellite.gpsValue(x, y, "time")
    mapCheck=False
    if (latitude>=0) and (longitude>=0) and (altitude>=0) and (timesat>=0):
        mapCheck=True
    else:
        print("This point is not on map. Please re-input:")	
    return mapCheck

def gpsAverage(x, y):

    value = satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "time") 

    average = value / 4

    return average


def distance(cur, dest):

    distance = math.sqrt(gpsAverage(cur[0], cur[1])**2 + gpsAverage(dest[0], dest[1])**2)

    return distance
