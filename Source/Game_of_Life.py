import os
import time
import random
import shutil

def getGridSize():
	gridX, gridY = input("Input grid's size(4x4) Enter '0x0' for current terminal size: ").split('x')
	if gridX == '0' and gridY == '0':
		gridX , gridY = shutil.get_terminal_size()[0], shutil.get_terminal_size()[1]-5
	return gridX, gridY
	#check user input
	#add size warning

def getGridMethod():
	print("#Completely dead with\n    1- random number and location of alive cells\n    2- max number and random location of alive cells")
	print("    3- set number and random location of alive cells\n    4- random number of alive cells at a set distance")
	print("    5- set number and set location of alive cells")
	print("#Completely alive with\n    5- random number and location of dead cells\n    6- max number and random location of alive cells")
	print("    7- set number and random location of dead cells\n    8-  random number of dead cells at a set distance")
	print("    9- set number and set location of dead cells")
	print("\n10- Completely random with adjustable bias")
		
	gridCreationMethod = int(input("Choose your grid creation method: "))
	return gridCreationMethod
	#check user input

def progressBar(x, y, interval):
	if x%interval == 0:	
		os.system("cls")
		print("finding {} random points".format(y))
		print("{}%".format(int((x*100)/y)))

def getRandomLocations(numberOfLocations):
	randomLocations = []
	while len(randomLocations) < numberOfLocations:
				randomPoint = [0 , 0]
				randomPoint[0] = random.randint(0,gridY-1)
				randomPoint[1] = random.randint(0,gridX-1)
				if randomPoint not in randomLocations:	
					randomLocations.append(randomPoint)
					progressBar(len(randomLocations), numberOfLocations, 5000)
	return randomLocations

def alterGrid(grid, locationsToBeAltered, alterTo):
	for i in range(len(locationsToBeAltered)):
				grid[locationsToBeAltered[i][0]][locationsToBeAltered[i][1]] = alterTo

def createGrid(gridX, gridY, gridCreationMethod):
	grid = []

	#Completely dead
	
	if gridCreationMethod < 6:
		#2d Array creation
		for y in range(gridY):
			new = []
			for x in range(gridX):
				new.append(0)
			grid.append(new)
		#Alterations for given methods
		if gridCreationMethod == 1:
			numberOfAliveCells = random.randint(0,gridX*gridY)
			randomLocations = getRandomLocations(numberOfAliveCells).copy()
			alterGrid(grid, randomLocations, 1)
			return grid

		elif gridCreationMethod == 2:
			os.system("cls")
			maxNumberOfAliveCells = int(input("Enter the maximum number of alive cells: "))
			numberOfAliveCells = random.randint(0,maxNumberOfAliveCells)
			randomLocations = getRandomLocations(maxNumberOfAliveCells).copy()
			alterGrid(grid, randomLocations, 1)
			return grid

		elif gridCreationMethod == 3:
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			numberOfAliveCells = int(input("Enter the number of alive cells: "))
			randomLocations = getRandomLocations(numberOfAliveCells).copy()
			alterGrid(grid, randomLocations, 1)
			return grid

		elif gridCreationMethod == 4:
			pass

		

	#Completely alive
	elif gridCreationMethod != 10:
		pass
	#Random
	else:
		pass

def displayGrid(grid):
	for y in range(len(grid)):
		print("")
		for x in range(len(grid[0])):
			if grid[y][x] == 1:
				print("#", end = '')
			else:
				print(" ", end = '')
	print("")


if __name__ == "__main__":
	gridX , gridY = getGridSize()
	gridX, gridY = int(gridX), int(gridY)
	gridCreationMethod = getGridMethod()
	grid = createGrid(gridX, gridY, gridCreationMethod).copy()
	os.system("cls")
	displayGrid(grid)

