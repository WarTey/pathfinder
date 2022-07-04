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
		self.screen.fill('White')
		pygame.display.set_caption(windowTitle)
		self.clock = pygame.time.Clock()

	def drawGrid(self):
		for x in range(self.blockSize, self.screenWidth, self.blockSize):
			pygame.draw.line(self.screen, 'Black', (x, 0), (x, self.screenHeight), 1)
		for y in range(self.blockSize, self.screenHeight, self.blockSize):
			pygame.draw.line(self.screen, 'Black', (0, y), (self.screenWidth, y), 1)

	def loop(self, clockTick = None):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			self.drawGrid()

			pygame.display.update()
			if clockTick:
				self.clock.tick(clockTick)

game = Main(1000, 700, 50)
game.initPygame('Pathfinder')
game.loop()
