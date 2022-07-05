from enum import Enum

class CellType(Enum):
	Free = 1
	Wall = 2
	Explored = 3

class Cell:
	def __init__(self):
		self.cellType = CellType.Free
		self.cellValue = 0
		self.cellParent = None
