class Path:
	def __init__(self, grid, startX, startY, endX, endY):
		self.isProcessing = False
		self.startX, self.startY, self.endX, self.endY = startX, startY, endX, endY
		self.initProcess(grid)

	def initProcess(self, grid):
		self.cell = grid.getCell(self.startX, self.startY)
		self.exploredCells = []
		self.traveledCells = [self.cell]

	def updateProcess(self):
		self.isProcessing = not self.isProcessing

	def getDistance(self, xFrom, yFrom, xTo, yTo):
		distance = 0

		while xFrom != xTo or yFrom != yTo:
			distance += 14 if xFrom != xTo and yFrom != yTo else 10
			xFrom += int((xTo - xFrom) / (abs(xTo - xFrom) or 1))
			yFrom += int((yTo - yFrom) / (abs(yTo - yFrom) or 1))

		return distance

	def exploreCell(self, grid, x, y):
		if x >= grid.nbCol or x < 0 or y >= grid.nbRow or y < 0:
			return

		cell = grid.getCell(x, y)
		if not cell.isExplorable() or cell in self.traveledCells:
			return

		cell.setExplored()
		if not cell in self.exploredCells:
			self.exploredCells.append(cell)

		distanceFromStart = self.cell.startDistance + self.getDistance(self.cell.x, self.cell.y, x, y)
		distanceFromEnd = self.getDistance(x, y, self.endX, self.endY)

		isCellScoreInvalid = distanceFromStart + distanceFromEnd > cell.score
		isCellFarFromEnd = distanceFromStart + distanceFromEnd == cell.score and distanceFromEnd >= cell.endDistance

		if cell.score > 0 and (isCellScoreInvalid or isCellFarFromEnd):
			return

		cell.startDistance = distanceFromStart
		cell.endDistance = distanceFromEnd
		cell.score = distanceFromStart + distanceFromEnd
		cell.parent = self.cell

	def setNextCell(self):
		if not len(self.exploredCells):
			self.updateProcess()

		self.exploredCells.sort(key = lambda cell: (cell.score, cell.endDistance))
		self.cell = self.exploredCells[0]
		self.exploredCells.remove(self.cell)
		self.traveledCells.append(self.cell)

	def colorPath(self):
		while self.cell:
			self.cell.setPath()
			self.cell = self.cell.parent

	def process(self, grid):
		if not self.cell or self.cell.isEnd():
			self.colorPath()
			self.updateProcess()
			return

		for x in range(-1, 2):
			for y in range(-1, 2):
				if x != 0 or y != 0:
					self.exploreCell(grid, self.cell.x + x, self.cell.y + y)

		self.setNextCell()
