import random

class Game:
	def __init__(self):
		self.boardwidth = 10
		self.boardheight = 20
		self.gameboard = [['0' for i in xrange(self.boardwidth)] for i in xrange(self.boardheight)]
		self.blocks = ['I', 'J', 'L', 'O', 'Z', 'T', 'S']
		self.blockpos = [0,0]
		self.blockrotate = 0
		self.falling = False
		self.screen_size = self.width, self.height = 500, 1000
		self.screen_colour = 0,0,0
		self.speed = 1000
		self.timer = 0
		self.gameover = False

	def getNewBlock(self):
		self.falling = True
		self.currentBlock = random.choice(self.blocks)
		return self.getBlock(self.currentBlock)

	def getBlock(self, block):
		if block == 'I':
			return self.IBlock()
		elif block == 'J':
			return self.JBlock()
		elif block == 'L':
			return self.LBlock()
		elif block == 'O':
			return self.OBlock()
		elif block == 'S':
			return self.SBlock()
		elif block == 'T':
			return self.TBlock()	
		elif block == 'Z':
			return self.ZBlock()

	def IBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][2] = 'I'
		block[1][2] = 'I'
		block[2][2] = 'I'
		block[3][2] = 'I'
		self.blockpos = [1,4]
		return block

	def JBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][2] = 'J'
		block[1][2] = 'J'
		block[2][2] = 'J'
		block[2][1] = 'J'
		self.blockpos = [1,5]

		return block

	def LBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][1] = 'L'
		block[1][1] = 'L'
		block[2][1] = 'L'
		block[2][2] = 'L'
		self.blockpos = [1,4]
		return block

	def OBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][1] = 'O'
		block[0][2] = 'O'
		block[1][1] = 'O'
		block[1][2] = 'O'
		self.blockpos = [0,5]
		return block

	def ZBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][1] = 'Z'
		block[0][2] = 'Z'
		block[1][2] = 'Z'
		block[1][3] = 'Z'
		self.blockpos = [0,4]
		return block

	def TBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][1] = 'T'
		block[1][0] = 'T'
		block[1][1] = 'T'
		block[1][2] = 'T'
		self.blockpos = [1,4]
		return block

	def SBlock(self):
		block = [['0' for i in xrange(4)] for i in xrange(4)]
		block[0][3] = 'S'
		block[0][2] = 'S'
		block[1][2] = 'S'
		block[1][1] = 'S'
		self.blockpos = [0,4]
		return block

