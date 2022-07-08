from enum import Enum

class CellType(Enum):
	Free = 'White'
	Wall = 'Grey'
	Explored = 'Yellow'
	Path = 'Blue'
	Start = 'Green'
	End = 'Red'

class Cell:
	def __init__(self):
		self.cellType = CellType.Free
		self.cellValue = 0
		self.cellParent = None

	def getCellColor(self):
		return self.cellType.value

	def isCellValid(self, cellType):
		return self.cellType == cellType

	def setCellType(self, cellType):
		freeType = CellType.Free
		wallType = CellType.Wall

		if ((cellType == freeType and self.isCellValid(wallType)) or
			(cellType == wallType and self.isCellValid(freeType)) or
			(cellType == CellType.Start and self.isCellValid(freeType)) or
			(cellType == CellType.End and self.isCellValid(freeType))):
			self.cellType = cellType

	def setFree(self):
		self.setCellType(CellType.Free)

	def setWall(self):
		self.setCellType(CellType.Wall)

	def setStart(self):
		self.setCellType(CellType.Start)

	def setEnd(self):
		self.setCellType(CellType.End)
