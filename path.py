class Path:
	def __init__(self):
		self.isProcessing = False

	def updateProcess(self):
		self.isProcessing = not self.isProcessing

	def getDistance(self):
		pass

	def process(self, grid):
		pass
