import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.cellSize = cellSize
		self.grid = [[Cell() for _ in range(int(screenWidth / cellSize))] for _ in range(int(screenHeight / cellSize))]

	def handleGridLeftClick(self, x, y):
		cellSize = self.cellSize
		self.grid[int(y / cellSize)][int(x / cellSize)].setWall()

	def handleGridRightClick(self, x, y):
		cellSize = self.cellSize
		self.grid[int(y / cellSize)][int(x / cellSize)].setFree()

	def drawCells(self, screen):
		cellSize = self.cellSize
		cellWidth = cellSize - 1
		for row, cells in enumerate(self.grid):
			for col, cell in enumerate(cells):
				pygame.draw.rect(screen, cell.cellType.value, pygame.Rect(col * cellSize, row * cellSize, cellWidth, cellWidth))
