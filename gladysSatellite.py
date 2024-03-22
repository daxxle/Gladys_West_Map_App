
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

    pathToJSONDataFiles = "C:/Users/dle/Documents/GitHub/Gladys_West_Map_App/data"

    # read the satellite data
    data = readSat(sat, pathToJSONDataFiles)
    value = -1
    for i,j,k in data.items():
        if x==i and y==j:
            print(k)
            value=k
            return value
    return value       

    
    
