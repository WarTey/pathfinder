import pygame
from sys import exit
from grid import Grid

class Main:
	def __init__(self, screenWidth, screenHeight):
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight

	def initPygame(self, windowTitle):
		pygame.init()
		self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
		self.screen.fill('Black')
		pygame.display.set_caption(windowTitle)
		self.clock = pygame.time.Clock()

	def loop(self, grid, clockTick = None):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
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

	game = Main(SCREEN_WIDTH, SCREEN_HEIGHT)
	game.initPygame(WINDOW_TITLE)
	grid = Grid(SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE)
	game.loop(grid)

main()
