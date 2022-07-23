import pygame
from cell import Cell

class Grid:
	def __init__(self, screenWidth, screenHeight, cellSize, startX, startY, endX, endY):
		self.cellSize = cellSize
		self.nbCol = int(screenWidth / cellSize)
		self.nbRow = int(screenHeight / cellSize)

		self.grid = [[Cell(x, y) for x in range(self.nbCol)] for y in range(self.nbRow)]
		self.grid[startX][startY].setStart()
		self.grid[endX][endY].setEnd()

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

		mousePos = pygame.mouse.get_pos()
		cell = self.getCell(mousePos[0] / self.cellSize, mousePos[1] / self.cellSize)
		font = pygame.font.SysFont('Arial', 12, bold = True)
		text = font.render('Score: ' + str(cell.score) + ', Start: ' + str(cell.startDistance) + ', End: ' + str(cell.endDistance), True, 'Red', 'Black')
		screen.blit(text, ((mousePos[0], mousePos[1] - text.get_height())))
