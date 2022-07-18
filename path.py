class Path:
	def __init__(self, grid):
		self.isProcessing = False
		self.initProcess(grid)

	def initProcess(self, grid):
		self.xStart = self.yStart = 0
		self.cell = grid.getCell(self.xStart, self.yStart)
		self.exploredCells = []

	def updateProcess(self, grid):
		self.isProcessing = not self.isProcessing
		if self.isProcessing:
			self.initProcess(grid)

	def getDistance(self, xFrom, yFrom, xTo, yTo):
		distance = 0

		#TODO: Inc distance with diag
		while xFrom != xTo or yFrom != yTo:
			if xFrom > xTo:
				xFrom -= 1
			elif xFrom < xTo:
				xFrom += 1

			if yFrom > yTo:
				yFrom -= 1
			elif yFrom < yTo:
				yFrom += 1

			distance += 1

		return distance

	def exploreCell(self, grid, x, y):
		if x >= grid.nbCol or x < 0 or y >= grid.nbRow or y < 0:
			return None

		cell = grid.getCell(x, y)
		cell.setExplored()
		if not cell.isExplored():
			return None

		distanceFromStart = self.getDistance(x, y, self.xStart, self.yStart) #TODO: DEF startx and starty
		distanceFromEnd = self.getDistance(x, y, 19, 13) #TODO: DEF endx and endy

		if distanceFromStart + distanceFromEnd >= cell.score and cell.score > 0:
			return None

		cell.startDistance = distanceFromStart
		cell.endDistance = distanceFromEnd
		cell.score = distanceFromStart + distanceFromEnd
		cell.parent = self.cell
		self.exploredCells.append(cell)

		return cell

	def getNextCell(self):
		return self.cell

	def process(self, grid):
		if self.cell.isEnd():
			self.updateProcess(grid)
			return

		# TODO: Reduce with for loop
		self.exploreCell(grid, self.xStart, self.yStart - 1)
		self.exploreCell(grid, self.xStart + 1, self.yStart)
		self.exploreCell(grid, self.xStart, self.yStart + 1)
		self.exploreCell(grid, self.xStart - 1, self.yStart)
		self.exploreCell(grid, self.xStart + 1, self.yStart + 1)
		self.exploreCell(grid, self.xStart - 1, self.yStart + 1)
		self.exploreCell(grid, self.xStart + 1, self.yStart - 1)
		self.exploreCell(grid, self.xStart - 1, self.yStart - 1)

		nextCell = self.getNextCell()
		if not nextCell.isPath():
			self.updateProcess(grid)
