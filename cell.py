from enum import Enum

class CellType(Enum):
	Free = 'White'
	Wall = 'Grey'
	Explored = 'Yellow'
	Path = 'Blue'
	Start = 'Green'
	End = 'Red'

class Cell:
	def __init__(self, x, y):
		self.type = CellType.Free
		self.startDistance = 0
		self.endDistance = 0
		self.score = 0
		self.parent = None
		self.x = x
		self.y = y

	def getColor(self):
		return self.type.value

	def isValid(self, type):
		return self.type == type

	def setType(self, type):
		if ((type == CellType.Free and self.isValid(CellType.Wall)) or
			(type == CellType.Wall and self.isValid(CellType.Free)) or
			(type == CellType.Explored and self.isValid(CellType.Free)) or
			(type == CellType.Path and self.isValid(CellType.Explored)) or
			(type == CellType.Start and self.isValid(CellType.Free)) or
			(type == CellType.End and self.isValid(CellType.Free))):
			self.type = type

	def setFree(self):
		self.setType(CellType.Free)

	def setWall(self):
		self.setType(CellType.Wall)

	def setStart(self):
		self.setType(CellType.Start)

	def setExplored(self):
		self.setType(CellType.Explored)

	def setPath(self):
		self.setType(CellType.Path)

	def setEnd(self):
		self.setType(CellType.End)

	def isExplored(self):
		return self.isValid(CellType.Explored)

	def isPath(self):
		return self.isValid(CellType.Path)

	def isEnd(self):
		return self.isValid(CellType.End)
