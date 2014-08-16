import random

class Game:
	def __init__(self):
		self.boardwidth = 10
		self.boardheight = 20
		self.gameboard = [['0' for i in xrange(self.boardwidth)] for i in xrange(self.boardheight)]
		self.blocks = ['I', 'J', 'L', 'O', 'Z', 'T', 'S']
		self.falling = False
		self.screen_size = self.width, self.height = 500, 1000
		self.screen_colour = 0,0,0
		self.speed = 500
		self.timer = 0
		self.gameover = False

	def getNewBlock(self):
		self.falling = True
		self.piece = random.choice(self.blocks)
		if self.piece == 'I':
			return self.IBlock()
		elif self.piece == 'J':
			return self.JBlock()
		elif self.piece == 'L':
			return self.LBlock()
		elif self.piece == 'O':
			return self.OBlock()
		elif self.piece == 'S':
			return self.SBlock()
		elif self.piece == 'T':
			return self.TBlock()	
		elif self.piece == 'Z':
			return self.ZBlock()

	def IBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(4)]
		block[0][4] = 'I'
		block[1][4] = 'I'
		block[2][4] = 'I'
		block[3][4] = 'I'
		return block

	def JBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(3)]
		block[0][5] = 'J'
		block[1][5] = 'J'
		block[2][5] = 'J'
		block[2][4] = 'J'
		return block

	def LBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(3)]
		block[0][4] = 'L'
		block[1][4] = 'L'
		block[2][4] = 'L'
		block[2][5] = 'L'
		return block

	def OBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(2)]
		block[0][4] = 'O'
		block[0][5] = 'O'
		block[1][4] = 'O'
		block[1][5] = 'O'
		return block

	def ZBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(2)]
		block[0][3] = 'Z'
		block[0][4] = 'Z'
		block[1][4] = 'Z'
		block[1][5] = 'Z'
		return block

	def TBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(2)]
		block[0][4] = 'T'
		block[1][3] = 'T'
		block[1][4] = 'T'
		block[1][5] = 'T'
		return block

	def SBlock(self):
		block = [['0' for i in xrange(10)] for i in xrange(2)]
		block[0][5] = 'S'
		block[0][4] = 'S'
		block[1][4] = 'S'
		block[1][3] = 'S'
		return block

