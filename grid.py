from types import CellType
import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.cellSize = cellSize
		maxCol = int(screenWidth / cellSize)
		maxRow = int(screenHeight / cellSize)
		grid = [[Cell() for _ in range(maxCol)] for _ in range(maxRow)]
		grid[0][0].setStart()
		grid[maxRow - 1][maxCol - 1].setEnd()
		self.grid = grid

	def getCell(self, x, y):
		return self.grid[int(y)][int(x)]

	def handleGridLeftClick(self, x, y):
		cellSize = self.cellSize
		self.getCell(x / cellSize, y / cellSize).setWall()

	def handleGridRightClick(self, x, y):
		cellSize = self.cellSize
		self.getCell(x / cellSize, y / cellSize).setFree()

	def drawCells(self, screen):
		cellSize = self.cellSize
		cellWidth = cellSize - 1
		for row, cells in enumerate(self.grid):
			for col, cell in enumerate(cells):
				pygame.draw.rect(screen, cell.getCellColor(), pygame.Rect(col * cellSize, row * cellSize, cellWidth, cellWidth))
