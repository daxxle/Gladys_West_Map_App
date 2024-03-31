import math
import gladysSatellite as satellite
"""
    Student: Dang Le
    Module: gladysCompute
    Description: This module does print GPS Value/Check/Average/Distance
"""

def gpsPrint(x, y):
    '''
        return string of GPS value latitude, longitude, altitude, & time
    '''
    latitude = satellite.gpsValue(x, y, "latitude")
    longitude = satellite.gpsValue(x, y, "longitude")
    altitude = satellite.gpsValue(x, y, "altitude")
    timesat = satellite.gpsValue(x, y, "time")
    str=f"({x},{y})\tSatellite: Latitude={latitude}\tLongitude={latitude}\tAltitude={altitude}\tTime={timesat}"
    return str

def gpsCheck(x, y):
    ''' 
        return True/False of point (x,y) matched GPS value latitude, longitude, altitude, & time or not
    '''
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
    '''
        return Average of point (x,y) between GPS value latitude, longitude, altitude, & time
    '''
    value = satellite.gpsValue(x, y, "latitude") + satellite.gpsValue(x, y, "longitude") + satellite.gpsValue(x, y, "altitude") + satellite.gpsValue(x, y, "time") 
    average = value / 4

    return average


def distance(cur, dest):
    '''
        return distance of current point and destination point
    '''
    distance = math.sqrt(gpsAverage(cur[0], cur[1])**2 + gpsAverage(dest[0], dest[1])**2)
    return distance
