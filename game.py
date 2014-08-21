import random
import pprint

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




	def resetBlock(self):
		self.block = [['0' for i in xrange(4)] for i in xrange(4)]
		for y in range(len(self.block)):
			for x in range(len(self.block[y])):
				self.block[y][x] = '0'

	def getNewBlock(self):
		self.falling = True
		self.currentBlock = random.choice(self.blocks)
		self.blockpos = [0,3]
		return self.getBlock(self.currentBlock)

	def getBlock(self, block):
		if block == 'I':
			self.IBlock()
		elif block == 'J':
			self.JBlock()
		elif block == 'L':
			self.LBlock()
		elif block == 'O':
			self.OBlock()
		elif block == 'S':
			self.SBlock()
		elif block == 'T':
			self.TBlock()	
		elif block == 'Z':
			self.ZBlock()

	def IBlock(self):
		self.resetBlock()
		self.block[0][2] = 'I'
		self.block[1][2] = 'I'
		self.block[2][2] = 'I'
		self.block[3][2] = 'I'

	def JBlock(self):
		self.resetBlock()
		self.block[0][2] = 'J'
		self.block[1][2] = 'J'
		self.block[2][2] = 'J'
		self.block[2][1] = 'J'

	def LBlock(self):
		self.resetBlock()
		self.block[0][1] = 'L'
		self.block[1][1] = 'L'
		self.block[2][1] = 'L'
		self.block[2][2] = 'L'

	def OBlock(self):
		self.resetBlock()
		self.block[0][1] = 'O'
		self.block[0][2] = 'O'
		self.block[1][1] = 'O'
		self.block[1][2] = 'O'

	def ZBlock(self):
		self.resetBlock()
		self.block[0][1] = 'Z'
		self.block[0][2] = 'Z'
		self.block[1][2] = 'Z'
		self.block[1][3] = 'Z'

	def TBlock(self):
		self.resetBlock()
		self.block[0][1] = 'T'
		self.block[1][0] = 'T'
		self.block[1][1] = 'T'
		self.block[1][2] = 'T'

	def SBlock(self):
		self.resetBlock()
		self.block[0][3] = 'S'
		self.block[0][2] = 'S'
		self.block[1][2] = 'S'
		self.block[1][1] = 'S'

