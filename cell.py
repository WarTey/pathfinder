from enum import Enum

class CellType(Enum):
	Free = 'White'
	Wall = 'Grey'
	Explored = 'Yellow'
	Path = 'Blue'

class Cell:
	def __init__(self):
		self.cellType = CellType.Free
		self.cellValue = 0
		self.cellParent = None
