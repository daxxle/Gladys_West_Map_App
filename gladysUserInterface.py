import io
import random
import numpy as np 
import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

def setPosition():
    """
		Ask user to enter current/destination point and check if point is on map,
		Then return point(x,y)
    """
    mapCheck=False
    while (not mapCheck):
        x = int(input("Enter x:"))
        y = int(input("Enter y:"))
        mapCheck=compute.gpsCheck(x, y)
    return (x,y)

def getDistance(cur, dest):
    """
		Calculate distance between current and destination point
    """
    dist=compute.distance(cur,dest)
    print(f"Distance between current({cur[0]}, {cur[1]}) and ({dest[0]}, {dest[1]}): {dist}")
    input("Press Enter back to main menu ...")
    return dist

def runTests(cur, dest):
    """
		Run tests through all function: print out current/destination, GPS average, Distance
    """
    print("Hello!")
    print("Running a few tests")
    print(f"Current GPS:\t {compute.gpsPrint(cur[0], cur[1])}")
    print(f"Current GPS Average:\t {compute.gpsAverage(cur[0], cur[1])}")
    print(f"Dest GPS:\t {compute.gpsPrint(dest[0], dest[1])}")
    print(f"Dest GPS Average:\t {compute.gpsAverage(dest[0], dest[1])}")
    print(f"Distance:\t {compute.distance(cur, dest)}")
    input("Press Enter to quit run tests and back to main menu...")

def start():
	"""
		logs the user in, and runs the app
	"""
	userName = userLogin.login()

	runApp(userName)


def runApp(userName):
	"""
		runs the app
	"""
	# loop until user types q
	nrange = np.arange(100)
	xC=random.choice(nrange)
	yC=random.choice(nrange)
	current=(xC,yC)
	xD=random.choice(nrange)
	yD=random.choice(nrange)
	dest=(xD,yD)
	distance=0
	userQuit = False
	while (not userQuit):
		# menu
		print("\n-- Welcome to the Gladys West Map App --")
		print("[c] Type c to set current position")
		print("[d] Type d to set destination position")
		print("[m] Type m to map – which tells the distance")
		print("[t] Type t to run module tests")
		print("[q] Type q to quit")
		print(f"Current GPS:\t{compute.gpsPrint(current[0], current[1])}")
		print(f"Dest GPS:\t{compute.gpsPrint(dest[0], dest[1])}")
		print(f"Distance:\t{compute.distance(current, dest)}")
		
		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		# quit
		if firstChar == 'q':
			userQuit = True

		# set current position function
		elif firstChar == 'c':
			print("Set current position")
			current = setPosition()

		# set destination position function
		elif firstChar == 'd':
			print("Set destination position")
			dest = setPosition()
		
		# calculate distance between current/destination position function
		elif firstChar == 'm':
			distance = getDistance(current, dest)

		# test function
		elif firstChar == 't':
			runTests(current, dest)

		# error input invalid choice
		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\nThank you for using the Gladys West Map App!\n")
