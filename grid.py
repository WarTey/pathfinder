import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize):
		self.cellSize = cellSize
		self.grid = [[Cell() for i in range(int(screenWidth / cellSize))] for j in range(int(screenHeight / cellSize))]

	def drawSeparators(self, screen, screenWidth, screenHeight):
		for x in range(self.cellSize, screenWidth, self.cellSize):
			pygame.draw.line(screen, 'Black', (x, 0), (x, screenHeight), 1)
		for y in range(self.cellSize, screenHeight, self.cellSize):
			pygame.draw.line(screen, 'Black', (0, y), (screenWidth, y), 1)

	def drawCells(self):
		pass
