import math
import gladysSatellite as satellite
"""
    Student: Dang Le
    Module: gladysCompute
    Description: This module does …
"""



def gpsAverage(x, y):

    value = satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "time") 

    average = value / 4

    return average


def distance(cur, dest):

    distance = math.sqrt(gpsAverage(cur[0], cur[1])**2 + gpsAverage(dest[0], dest[1])**2)

    return distance
