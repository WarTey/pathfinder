import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.cellSize = cellSize
		self.nbCol = int(screenWidth / cellSize)
		self.nbRow = int(screenHeight / cellSize)

		self.grid = [[Cell() for _ in range(self.nbCol)] for _ in range(self.nbRow)]
		self.grid[0][0].setStart()
		self.grid[self.nbRow - 1][self.nbCol - 1].setEnd()

	def getCell(self, x, y):
		return self.grid[int(y)][int(x)]

	def handleLeftClick(self, x, y):
		self.getCell(x / self.cellSize, y / self.cellSize).setWall()

	def handleRightClick(self, x, y):
		self.getCell(x / self.cellSize, y / self.cellSize).setFree()

	def draw(self, screen):
		for row, cells in enumerate(self.grid):
			for col, cell in enumerate(cells):
				rect = pygame.Rect(col * self.cellSize, row * self.cellSize, self.cellSize - 1, self.cellSize - 1)
				pygame.draw.rect(screen, cell.getColor(), rect)
