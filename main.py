from enum import Enum
import pygame
from sys import exit
from grid import Grid
from path import Path

class MouseType(Enum):
	Left = 0
	Right = 2

class Game:
	def __init__(self, screenWidth, screenHeight, windowTitle):
		pygame.init()
		self.screenWidth, self.screenHeight = screenWidth, screenHeight
		self.screen = pygame.display.set_mode((screenWidth, screenHeight))
		self.screen.fill('Black')
		pygame.display.set_caption(windowTitle)

	def isMouseButtonInAction(self, mouseButton, eventType):
		isMousePressed = pygame.mouse.get_pressed()
		isMouseButtonPressed = isMousePressed[mouseButton]

		return isMouseButtonPressed or isMouseButtonPressed and eventType == pygame.MOUSEMOTION

	def handleMouse(self, eventType, grid):
		mousePos = pygame.mouse.get_pos()

		if self.isMouseButtonInAction(MouseType.Left.value, eventType):
			grid.handleLeftClick(mousePos[0], mousePos[1])
		elif self.isMouseButtonInAction(MouseType.Right.value, eventType):
			grid.handleRightClick(mousePos[0], mousePos[1])

	def handleKeyboard(self, eventKey, path):
		if eventKey == pygame.K_RETURN:
			path.updateProcess()

	def loop(self, grid, path):
		while True:
			for event in pygame.event.get():
				if not path.isProcessing:
					self.handleMouse(event.type, grid)

				if event.type == pygame.KEYDOWN:
					self.handleKeyboard(event.key, path)
				elif event.type == pygame.QUIT:
					pygame.quit()
					exit()

			grid.draw(self.screen)
			if path.isProcessing:
				path.process(grid)

			pygame.display.update()

def main():
	SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 700
	CELL_SIZE = 50
	WINDOW_TITLE = 'Pathfinder'
	START_X, START_Y = 0, 0
	END_X, END_Y = 10, 10

	game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
	grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE, START_X, START_Y, END_X, END_Y)
	path = Path(grid, START_X, START_Y, END_X, END_Y)
	game.loop(grid, path)

main()
