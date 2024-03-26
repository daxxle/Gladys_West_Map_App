
import json
from datascience import *
import numpy as np
"""
    Student: Dang Le
    Module: gladysSatellite
    Description: This module does …
"""


def readSat(sat, pathToJSONDataFiles):
    """
     reads satellite data from a json file
     Students do NOT need to change the readSat function.
    """

    # data file path
    fileName = sat + "-satellite.json"
    file_path = pathToJSONDataFiles + "/" + fileName

    # open the file
    try:
        fileHandle = open(file_path)
    except IOError:
        print("ERROR: Unable to open the file " + file_path)
        raise IOError

    # print("file_path = ", file_path)

    # read the file
    data = json.load(fileHandle)

    return data


def gpsValue(x, y, sat):
    """
     document your function definition here. what does it do?
    """

    pathToJSONDataFiles = "C:/Users/haida/Documents/GitHub/Gladys_West_Map_App/data"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)
    for i in data:  
        xpos = i.get("x")
        ypos = i.get("y")
        value = i.get("value")
        if (x==i.get("x")) and (y==ypos):
            return value     
    print(f"ERROR: Can't find the value for ({x},{y}) in satellite = {sat}")
    return -1       

    
    
