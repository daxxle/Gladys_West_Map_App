import io
import random
import numpy as np 
import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin

def setCurrentPos():
	print("Set current position")
	mapCheck=False
	while (not mapCheck):
		xC = int(input("Current position x:"))
		yC = int(input("Current position y:"))
		mapCheck=compute.gpsCheck(xC, yC)
	return (xC,yC)
	
def setDestPos():
	print("Set destination position")
	mapCheck=False
	while (not mapCheck):
		xD = int(input("Destination position x:"))
		yD = int(input("Destination position y:"))
		mapCheck=compute.gpsCheck(xD, yD)
	return (xD,yD)

def getDistance(cur, dest):
	dist=compute.distance(cur,dest)
	#print("Distance:", dist)
	return dist

def runTests(cur, dest):

	print("Hello!")
	print("Running a few tests")
	print(f"Current GPS:\t {compute.gpsPrint(cur[0], cur[1])}")
	print(f"Current GPS Average:\t {compute.gpsAverage(cur[0], cur[1])}")
	print(f"Dest GPS:\t {compute.gpsPrint(dest[0], dest[1])}")
	print(f"Dest GPS Average:\t {compute.gpsAverage(dest[0], dest[1])}")
	print(f"Distance:\t {compute.distance(cur, dest)}")
	input("Press Enter to quit run tests ...")

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules

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
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("\n-- Welcome to the Gladys West Map App --")
		print("[c] Type c to set current position")
		print("[d] Type d to set destination position")
		print("[m] Type m to map – which tells the distance")
		print("[t] Type t to run module tests")
		print("[q] Type q to quit")
		print(f"Current GPS:\t {compute.gpsPrint(current[0], current[1])}")
		print(f"Destination GPS: {compute.gpsPrint(dest[0], dest[1])}")
		print(f"Distance:\t {compute.distance(current, dest)}")
		
		# get first character of input
		userInput = input("Enter a command:")
		lowerInput = userInput.lower()
		firstChar = lowerInput[0:1]

		# menu choices, use a switch-like if-elif control structure

		"""
			here students need to change and add to this code to
			handle their menu options
		"""
		# quit
		if firstChar == 'q':
			userQuit = True

		elif firstChar == 'c':
			current = setCurrentPos()

		elif firstChar == 'd':
			dest = setDestPos()
		
		elif firstChar == 'm':
			distance = getDistance(current, dest)

		elif firstChar == 't':
			runTests(current, dest)

		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\nThank you for using the Gladys West Map App!\n")
