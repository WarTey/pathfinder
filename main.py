import pygame
from sys import exit
from grid import Grid
from path import Path

class Game:
	def __init__(self, screenWidth, screenHeight):
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def initPygame(self, windowTitle):
		pygame.init()
		screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
		screen.fill('Black')
		pygame.display.set_caption(windowTitle)

		self.screen = screen
		self.clock = pygame.time.Clock()

	def handleMouse(self, eventType, grid):
		isMouseMotionType = eventType == pygame.MOUSEMOTION
		isMousePressed = pygame.mouse.get_pressed()
		isLeftMousePressed = isMousePressed[0]
		isRightMousePressed = isMousePressed[2]
		mousePos = pygame.mouse.get_pos()

		if isLeftMousePressed or isLeftMousePressed and isMouseMotionType:
			grid.handleGridLeftClick(mousePos[0], mousePos[1])
		elif isRightMousePressed or isRightMousePressed and isMouseMotionType:
			grid.handleGridRightClick(mousePos[0], mousePos[1])

	def handleKeyboard(self, eventKey, path, isPathProcessing):
		if eventKey == pygame.K_RETURN:
			path.setProcess(not isPathProcessing)

	def loop(self, grid, path, clockTick = None):
		while True:
			for event in pygame.event.get():
				eventType = event.type
				isPathProcessing = path.isProcessing()

				if not isPathProcessing:
					self.handleMouse(eventType, grid)

				if eventType == pygame.KEYDOWN:
					self.handleKeyboard(event.key, path, isPathProcessing)
				elif eventType == pygame.QUIT:
					pygame.quit()
					exit()

			grid.drawCells(self.screen)
			if isPathProcessing:
				path.process(grid)

			pygame.display.update()
			if clockTick:
				self.clock.tick(clockTick)

def main():
	SCREEN_WIDTH = 1000
	SCREEN_HEIGHT = 700
	CELL_SIZE = 50
	WINDOW_TITLE = 'Pathfinder'

	game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
	game.initPygame(WINDOW_TITLE)
	grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
	path = Path()
	game.loop(grid, path)

main()
