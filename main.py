import pygame
from sys import exit
from grid import Grid

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

	def loop(self, grid, clockTick = None):
		while True:
			isMousePressed = pygame.mouse.get_pressed()
			isLeftMousePressed = isMousePressed[0]
			isRightMousePressed = isMousePressed[2]
			mousePos = pygame.mouse.get_pos()

			for event in pygame.event.get():
				isMouseMotionType = event.type == pygame.MOUSEMOTION

				if isLeftMousePressed or isLeftMousePressed and isMouseMotionType:
					grid.handleGridLeftClick(mousePos[0], mousePos[1])
				elif isRightMousePressed or isRightMousePressed and isMouseMotionType:
					grid.handleGridRightClick(mousePos[0], mousePos[1])
				elif event.type == pygame.QUIT:
					pygame.quit()
					exit()

			grid.drawCells(self.screen)

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
	game.loop(grid)

main()
