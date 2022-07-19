class Path:
	def __init__(self, grid):
		self.isProcessing = False
		self.initProcess(grid)

	def initProcess(self, grid):
		self.cell = grid.getCell(0, 0)
		self.exploredCells = []

	def updateProcess(self, grid):
		self.isProcessing = not self.isProcessing
		if self.isProcessing:
			self.initProcess(grid)

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
		cell.setExplored()
		if not (cell.isExplored() or cell.isEnd()):
			return

		distanceFromStart = self.getDistance(x, y, 0, 0) #TODO: DEF startx and starty
		distanceFromEnd = self.getDistance(x, y, 19, 13) #TODO: DEF endx and endy

		if distanceFromStart + distanceFromEnd >= cell.score and cell.score > 0:
			return

		cell.startDistance = distanceFromStart
		cell.endDistance = distanceFromEnd
		cell.score = distanceFromStart + distanceFromEnd
		cell.parent = self.cell

		if not cell in self.exploredCells:
			self.exploredCells.append(cell)

	def getNextCell(self):
		self.exploredCells.sort(key = lambda cell: (cell.score, cell.endDistance))
		self.cell = self.exploredCells[0] if len(self.exploredCells) > 0 else None

		if not self.cell:
			return self.cell

		self.cell.setPath()
		self.exploredCells.remove(self.cell)
		return self.cell

	def process(self, grid):
		if self.cell.isEnd():
			self.updateProcess(grid)
			return

		for x in range(-1, 2):
			for y in range(-1, 2):
				if x != 0 or y != 0:
					self.exploreCell(grid, self.cell.x + x, self.cell.y + y)

		nextCell = self.getNextCell()
		if not nextCell or not nextCell.isPath():
			self.updateProcess(grid)
