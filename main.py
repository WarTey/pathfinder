import pygame
from sys import exit

class Main:
	def __init__(self, screenWidth, screenHeight, blockSize):
		self.screenWidth = screenWidth
		self.screenHeight = screenHeight
		self.blockSize = blockSize

	def initPygame(self, windowTitle):
		pygame.init()
		self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
		pygame.display.set_caption(windowTitle)
		self.clock = pygame.time.Clock()

	def loop(self, clockTick):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			pygame.display.update()
			self.clock.tick(clockTick)

	def drawGrid(self):
		pass

game = Main(1000, 700, 20)
game.initPygame('Pathfinder')
game.loop(60)