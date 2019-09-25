import os
import time
import random
import shutil

def getGridSize():
	gridX, gridY = input("Input grid's size(4x4) Enter '0x0' for current terminal size: ").split('x')
	if gridX == '0' and gridY == '0':
		gridX , gridY = shutil.get_terminal_size()[0], shutil.get_terminal_size()[1]-5
	return gridX, gridY
	#add checks for user input
	#add size warning

def getGridMethod():
	print("#Completely dead with\n    1- random number and location of alive cells\n    2- max number and random location of alive cells")
	print("    3- set number and random location of alive cells\n    4- random number of alive cells at a set distance")
	print("    5- max number of alive cells at a set distance\n    6- set number of alive cells at a set distance")
	print("    7- set number and set location of alive cells")
	print("#Completely alive with\n    8- random number and location of dead cells\n    9- max number and random location of alive cells")
	print("    10- set number and random location of dead cells\n    11- random number of dead cells at a set distance")
	print("    12- max number of dead cells at a set distance\n    13- set number of dead cells at a set distance")
	print("    14- set number and set location of dead cells")
	print("\n15- Completely random with adjustable bias\n")
		
	gridCreationMethod = int(input("Choose your grid creation method: "))
	return gridCreationMethod
	#add checks for user input

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
	
def	getRandomLocationsAtDistance(numberOfLocations, seperationDistance, gridX, gridY, type):
	tryCount = 0
	offset = 0
	randomLocations = []
	if type == 1:
		randomPoint = [0 , 0]
		randomPoint[0] = random.randint(0,gridY-1)
		randomPoint[1] = random.randint(0,gridX-1)
		randomLocations.append(randomPoint)
		while len(randomLocations) < numberOfLocations:
			randomPoint = [0 , 0]
			randomPoint[0] = random.randint(randomLocations[len(randomLocations)-1-offset][0] - seperationDistance,randomLocations[len(randomLocations)-1-offset][0] + seperationDistance)
			randomPoint[1] = random.randint(randomLocations[len(randomLocations)-1-offset][1] - seperationDistance,randomLocations[len(randomLocations)-1-offset][1] + seperationDistance)
			if randomPoint[0] < 0:
				randomPoint[0] += gridY-1
			elif randomPoint[0] > gridY-1:
				randomPoint[0] -= gridY-1

			if randomPoint[1] < 0:
				randomPoint[1] += gridX-1
			elif randomPoint[1] > gridX-1:
				randomPoint[1] -= gridX-1

			if randomPoint not in randomLocations:
				randomLocations.append(randomPoint)
				progressBar(len(randomLocations), numberOfLocations, 5000)
				offset, tryCount = 0, 0
			elif tryCount > 4:
				offset += 1
				tryCount = 0
			else:
				tryCount += 1
		return randomLocations


def alterGrid(grid, locationsToBeAltered, alterTo):
	for i in range(len(locationsToBeAltered)):
				grid[locationsToBeAltered[i][0]][locationsToBeAltered[i][1]] = alterTo


def setGridDead(grid, gridY, gridX):
	grid.clear()
	for y in range(gridY):
		new = []
		for x in range(gridX):
			new.append(0)
		grid.append(new)

def setGridAlive(grid, gridY, gridX):
	grid.clear()
	for y in range(gridY):
		new = []
		for x in range(gridX):
			new.append(1)
		grid.append(new)

def createGrid(gridX, gridY, gridCreationMethod):
	grid = []

	#Completely dead
	
	if gridCreationMethod < 8:
		#2d Array creation
		for y in range(gridY):
			new = []
			for x in range(gridX):
				new.append(0)
			grid.append(new)
		#Alterations for given methods
		if gridCreationMethod == 1:
			generateAgain = 'y'
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfAliveCells = random.randint(0,gridX*gridY)
				randomLocations = getRandomLocations(numberOfAliveCells).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 2:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			maxNumberOfAliveCells = int(input("Enter the maximum number of alive cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfAliveCells = random.randint(0,maxNumberOfAliveCells)
				randomLocations = getRandomLocations(maxNumberOfAliveCells).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 3:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			numberOfAliveCells = int(input("Enter the number of alive cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				randomLocations = getRandomLocations(numberOfAliveCells).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 4:
			generateAgain = 'y'
			os.system("cls")
			seperationDistance = int(input("Enter the seperation distance: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfAliveCells = random.randint(0,gridX*gridY)
				randomLocations = getRandomLocationsAtDistance(numberOfAliveCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid
		
		elif gridCreationMethod == 5:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			maxNumberOfAliveCells = int(input("Enter the maximum number of alive cells: ")) #add checks for user input
			seperationDistance = int(input("Enter the seperation distance: "))
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfAliveCells = random.randint(0,maxNumberOfAliveCells)
				randomLocations = getRandomLocationsAtDistance(numberOfAliveCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 6:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			numberOfAliveCells = int(input("Enter the maximum number of alive cells: ")) #add checks for user input
			seperationDistance = int(input("Enter the seperation distance: "))
			while generateAgain != 'n' and generateAgain != 'N':
				randomLocations = getRandomLocationsAtDistance(numberOfAliveCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid
		#needs optimizing

		elif gridCreationMethod == 7:
			generateAgain = 'y'
			os.system("cls")
			cellLocations = []
			cellCoordinates = [0,0]
			print("Total number of cells {}".format(gridX*gridY))
			numberOfAliveCells = int(input("Enter the number of alive cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				for i in range(numberOfAliveCells):
					cellCoordinates = [0,0]
					cellCoordinates[0],cellCoordinates[1] = input("Enter cell coordinates as 'row,column': ").split(',')
					cellCoordinates[0],cellCoordinates[1] = int(cellCoordinates[0]), int(cellCoordinates[1])
					cellLocations.append(cellCoordinates)
				alterGrid(grid, cellLocations, 1)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridDead(grid, gridY, gridX)
			return grid
		#needs input checks and improvements

	#Completely alive
	elif gridCreationMethod != 15:
		#2d Array creation
		for y in range(gridY):
			new = []
			for x in range(gridX):
				new.append(1)
			grid.append(new)
		
		#Alterations for given methods
		if gridCreationMethod == 8:
			generateAgain = 'y'
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfDeadCells = random.randint(0,gridX*gridY)
				randomLocations = getRandomLocations(numberOfDeadCells).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 9:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			maxNumberOfDeadCells = int(input("Enter the maximum number of dead cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfDeadCells = random.randint(0,maxNumberOfDeadCells)
				randomLocations = getRandomLocations(maxNumberOfDeadCells).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 10:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			numberOfDeadCells = int(input("Enter the number of dead cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				randomLocations = getRandomLocations(numberOfDeadCells).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid

		elif gridCreationMethod == 11:
			generateAgain = 'y'
			os.system("cls")
			seperationDistance = int(input("Enter the seperation distance: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfDeadCells = random.randint(0,gridX*gridY)
				randomLocations = getRandomLocationsAtDistance(numberOfDeadCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid
		
		elif gridCreationMethod == 12:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			maxNumberOfDeadCells = int(input("Enter the maximum number of dead cells: ")) #add checks for user input
			seperationDistance = int(input("Enter the seperation distance: "))
			while generateAgain != 'n' and generateAgain != 'N':
				numberOfDeadCells = random.randint(0,maxNumberOfDeadCells)
				randomLocations = getRandomLocationsAtDistance(numberOfDeadCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid
		
		elif gridCreationMethod == 13:
			generateAgain = 'y'
			os.system("cls")
			print("Total number of cells {}".format(gridX*gridY))
			numberOfDeadCells = int(input("Enter the maximum number of dead cells: ")) #add checks for user input
			seperationDistance = int(input("Enter the seperation distance: "))
			while generateAgain != 'n' and generateAgain != 'N':
				randomLocations = getRandomLocationsAtDistance(numberOfDeadCells, seperationDistance, gridX, gridY, 1).copy()
				alterGrid(grid, randomLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid
		#needs optimizing

		elif gridCreationMethod == 14:
			generateAgain = 'y'
			os.system("cls")
			cellLocations = []
			cellCoordinates = [0,0]
			print("Total number of cells {}".format(gridX*gridY))
			numberOfDeadCells = int(input("Enter the number of dead cells: ")) #add checks for user input
			while generateAgain != 'n' and generateAgain != 'N':
				for i in range(numberOfDeadCells):
					cellCoordinates = [0,0]
					cellCoordinates[0],cellCoordinates[1] = input("Enter cell coordinates as 'row,column': ").split(',')
					cellCoordinates[0],cellCoordinates[1] = int(cellCoordinates[0]), int(cellCoordinates[1])
					cellLocations.append(cellCoordinates)
				alterGrid(grid, cellLocations, 0)
				displayGrid(grid)
				print("Generate again(y/n)? ", end = '')
				generateAgain = input("('d' for choosing a different method or size)  ")
				if generateAgain == 'd' and 'D':
					return [[-1], [-1]]
				elif generateAgain == 'y' and 'Y':
					setGridAlive(grid, gridY, gridX)
			return grid
		#needs input checks and improvements

	#Random with bias
	else:
		generateAgain = 'y'
		os.system("cls")
		print("Total number of cells {}".format(gridX*gridY))
		biastowardsAlive = int(input("Enter bias towards being alive: %")) #add checks for user input
		while generateAgain != 'n' and generateAgain != 'N':
			for y in range(gridY):
				new = []
				for x in range(gridX):
				
					if random.randint(0, 100) < (50*biastowardsAlive/100)+50:
						new.append(1)
					else:
						new.append(0)
				progressBar((y+1)*(x+1), gridY*gridX, 5)
				grid.append(new)
			displayGrid(grid)
			print("Generate again(y/n)? ", end = '')
			generateAgain = input("('d' for choosing a different method or size)  ")
			if generateAgain == 'd' and 'D':
				return [[-1], [-1]]
			elif generateAgain == 'y' and 'Y':
				grid.clear()
		return grid
		
		

def displayGrid(grid):
	os.system("cls")
	for y in range(len(grid)):
		print("")
		for x in range(len(grid[0])):
			if grid[y][x] == 1:
				print("#", end = '')
			else:
				print(" ", end = '')
	print("")


if __name__ == "__main__":
	generateAgain = 'y'
	while generateAgain != 'n' and generateAgain != 'N':
		os.system("cls")
		gridX , gridY = getGridSize()
		gridX, gridY = int(gridX), int(gridY)
		gridCreationMethod = getGridMethod()
		grid = createGrid(gridX, gridY, gridCreationMethod).copy()
		if grid[0][0] == -1:
			generateAgain = 'y'
		else:
			generateAgain = 'n'



