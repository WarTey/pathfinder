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

	def getColor(self):
		return self.cellType.value

	def isValid(self, cellType):
		return self.cellType == cellType

	def setType(self, cellType):
		if ((cellType == CellType.Free and self.isValid(CellType.Wall)) or
			(cellType == CellType.Wall and self.isValid(CellType.Free)) or
			(cellType == CellType.Start and self.isValid(CellType.Free)) or
			(cellType == CellType.End and self.isValid(CellType.Free))):
			self.cellType = cellType

	def setFree(self):
		self.setType(CellType.Free)

	def setWall(self):
		self.setType(CellType.Wall)

	def setStart(self):
		self.setType(CellType.Start)

	def setEnd(self):
		self.setType(CellType.End)
