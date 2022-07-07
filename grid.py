import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.cellSize = cellSize
		self.grid = [[Cell() for _ in range(int(screenWidth / cellSize))] for _ in range(int(screenHeight / cellSize))]

	def drawCells(self, screen):
		for row, cells in enumerate(self.grid):
			for col, _ in enumerate(cells):
				pygame.draw.rect(screen, 'White', pygame.Rect(col * self.cellSize, row * self.cellSize, self.cellSize - 1, self.cellSize - 1))
