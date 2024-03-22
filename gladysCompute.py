import math
import gladysSatellite as satellite
"""
    Student: Dang Le
    Module: gladysCompute
    Description: This module does …
"""

def gpsCheck(x, y):
    print(x)
    print(y)
    print(satellite.gpsValue(x, y, "latitude"))
    print(satellite.gpsValue(x, y, "altitude"))
    print(satellite.gpsValue(x, y, "longitude"))
    print(satellite.gpsValue(x, y, "time"))

    '''mapCheck=False
    if satellite.gpsValue(x, y, "latitude")>=0 and satellite.gpsValue(x, y, "longitude")>=0 and satellite.gpsValue(x, y, "altitude")>=0 and satellite.gpsValue(x, y, "time")>=0:
        print("This point is on map\n")
        mapCheck=True
    else:
        print("This point is not on map\n")
    return mapCheck'''

def gpsAverage(x, y):

    value = satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "time") 

    average = value / 4

    return average


def distance(cur, dest):

    distance = math.sqrt(gpsAverage(cur[0], cur[1])**2 + gpsAverage(dest[0], dest[1])**2)

    return distance
