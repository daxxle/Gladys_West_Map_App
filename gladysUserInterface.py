import io

import gladysCompute as compute
import gladysSatellite as satellite
import gladysUserLogin as userLogin


def setCurrentPos():
	print("Set current position")
	xC = input("Current position x:")
	yC = input("Current position y:")
	return (xC,yC)
	
def setDestPos():
	print("Set destination position")
	xD = input("Destination position x:")
	yD = input("Destination position y:")
	return (xD,yD)

def getDistance(cur, dest):
	dist=compute.distance(cur,dest)
	print("Distance between current and destination", dist)
	return dist

def runTests():
	print("running a few tests")

	average = compute.gpsAverage(4, 5)
	print("average = ", average)

	# delete the remaining code *in this function* and replace it with
	# your code. add more code to do what the assignment asks you to do.
	# add 3 more tests of different functions in different modules
	print("hello!")


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
	current=(0,0)
	dest=(0,0)
	distance=0
	userQuit = False
	while (not userQuit):
		# menu
		"""
			here student needs to print their own menu. or, to do better, 
			create a function to print your menu and simply call it here.
		"""
		print("-- Welcome to the Gladys West Map App --")
		print("[c] Type c to set current position")
		print("[d] Type d to set destination position")
		print("[m] Type m to map – which tells the distance")
		print("[t] Type t to run module tests (random choice [c,d,m])")
		print("[q] Type q to quit")
		print()

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
			runTests()

		else:
			print("ERROR: " + firstChar + " is not a valid command")

	print("\nThank you for using the Gladys West Map App!\n")
