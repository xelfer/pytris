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
		self.gameboard[1][5] = 1
		self.gameboard[2][5] = 1
		self.gameboard[3][5] = 1
		self.gameboard[3][6] = 1

		self.gameboard[9][1] = 1
		self.gameboard[9][2] = 1
		self.gameboard[9][3] = 1
		self.gameboard[9][4] = 1

		self.gameboard[15][6] = 1
		self.gameboard[15][7] = 1
		self.gameboard[16][6] = 1
		self.gameboard[16][7] = 1

	def getNewBlock(self):
		self.falling = True
		return random.choice(self.blocks)
