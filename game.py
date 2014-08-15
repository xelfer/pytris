import random

class Game:
	def __init__(self):
		self.gameboard = [[0 for i in xrange(10)] for i in xrange(20)]
		self.blocks = ['I', 'J', 'L', 'O', 'Z', 'T', 'S']
		self.falling = False
		self.screen_size = self.width, self.height = 500, 1000
		self.screen_colour = 0,0,0
		self.speed = 1000
		self.timer = 0
		# temporary
		self.gameboard[1][4] = 1
		self.gameboard[2][4] = 1
		self.gameboard[3][4] = 1
		self.gameboard[0][4] = 1

	def getNewBlock(self):
		self.falling = True
		return random.choice(self.blocks)

	def iBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(4)]
		block[0][5] = 'I'
		block[1][5] = 'I'
		block[2][5] = 'I'
		block[3][5] = 'I'
		return block

	def jBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(3)]
		block[0][5] = 'J'
		block[1][5] = 'J'
		block[2][5] = 'J'
		block[2][4] = 'J'
		return block

	def lBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(3)]
		block[0][5] = 'L'
		block[1][5] = 'L'
		block[2][5] = 'L'
		block[2][6] = 'L'
		return block

	def oBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(2)]
		block[0][4] = 'O'
		block[1][5] = 'O'
		block[0][4] = 'O'
		block[1][5] = 'O'
		return block

	def zBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(2)]
		block[0][4] = 'Z'
		block[0][5] = 'Z'
		block[1][5] = 'Z'
		block[1][6] = 'Z'
		return block

	def tBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(2)]
		block[0][5] = 'T'
		block[1][4] = 'T'
		block[1][5] = 'T'
		block[1][6] = 'T'
		return block

	def sBlock(self):
		block = [[0 for i in xrange(10)] for i in xrange(2)]
		block[0][5] = 'S'
		block[0][6] = 'S'
		block[1][5] = 'S'
		block[1][4] = 'S'
		return block

