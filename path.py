class Path:
	def __init__(self):
		self.pathProcessing = False

	def isProcessing(self):
		return self.pathProcessing

	def setProcess(self, isProcessing):
		self.pathProcessing = isProcessing

	def process(self, grid):
		pass
