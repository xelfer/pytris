import sys, pygame, pprint
import game
import re

# game timer update, ticks in seconds
def timer_update(g):
	tmptime = pygame.time.get_ticks()/g.speed
	if tmptime > g.timer:
		g.timer = tmptime
		gameLoop(g)

# the main game loop
def gameLoop(g):
	if (g.gameover == False):
		if g.falling == False:
			addNewBlock(g)
			drawGame(g)

		else:
			moveFallingPieceDown(g)

def moveFallingPieceDown(g):
	g.gameboard.reverse()
	stopgame = False
	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
			if move: # check if we can move the block
				if (re.match(r'[a-z]', g.gameboard[y-1][x], flags=0)):
					stopgame = True
				elif y == 0:
					stopgame = True

	if (stopgame == False):
		for y in range(len(g.gameboard)):
			for x in range(len(g.gameboard[y])):
				move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
				if move:
					g.gameboard[y-1][x] = g.gameboard[y][x]
					g.gameboard[y][x] = '0'
		g.blockpos = [g.blockpos[0]+1, g.blockpos[1]]

	else:
		stop(g)

	g.gameboard.reverse()
	drawGame(g)


def moveFallingPieceLeft(g):
	cantmove = False
	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
			if move: # check if we can move the block
				if x == 0:
					cantmove = True
				elif (re.match(r'[a-z]', g.gameboard[y][x-1], flags=0)):
					cantmove = True

	if (cantmove == False):
		for y in range(len(g.gameboard)):
			for x in range(len(g.gameboard[y])):
				move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
				if move:
					g.gameboard[y][x-1] = g.gameboard[y][x]
					g.gameboard[y][x] = '0'
		g.blockpos = [g.blockpos[0], g.blockpos[1]-1]

	drawGame(g)

def moveFallingPieceRight(g):
	cantmove = False
	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
			if move:
				if x == 9:
					cantmove = True
				elif re.match(r'[a-z]', g.gameboard[y][x+1], flags=0):
					cantmove = True
	
	if (cantmove == False):
		for y in range(len(g.gameboard)):
			xx=g.boardwidth-1
			for x in range(0,g.boardwidth):
				move = re.match(r'[A-Z]', g.gameboard[y][xx], flags=0)
				if move:
					g.gameboard[y][xx+1] = g.gameboard[y][xx]
					g.gameboard[y][xx] = '0'
				xx=xx-1	
		g.blockpos = [g.blockpos[0], g.blockpos[1]+1]

	drawGame(g)

def stop(g):
	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			if (re.match(r'[A-Z]', g.gameboard[y][x], flags=0)):
				g.gameboard[y][x] = g.gameboard[y][x].lower()
	g.falling = False

def rotatePiece(g):

	# create a tmp board which just has the piece to rotate
	#tmpboard = [['0' for i in xrange(g.boardwidth)] for i in xrange(g.boardheight)]
	#for y in range(len(g.gameboard)):
	#		for x in range(len(g.gameboard[y])):
	#			if (re.match(r'[A-Z]', g.gameboard[y][x], flags=0)):
	#				tmpboard[y][x] = g.gameboard[y][x]


	y,x = g.blockpos
	# create a 4x4 with the piece to rotate
	block = g.getBlock(g.currentBlock)
	pprint.pprint(block)

	# rotate it
	print g.currentBlock
	if g.currentBlock == 'O': pass
	elif g.currentBlock == 'I':pass
	elif g.currentBlock == 'J':pass
	elif g.currentBlock == 'L':pass
	elif g.currentBlock == 'S':pass
	elif g.currentBlock == 'T':pass
	elif g.currentBlock == 'Z':pass

	# check if it clashes

	# if it doesn't, keep the new board

	# if it does, don't do anything, keep current board
	drawGame(g)
	


# draws the game according to the array
def drawGame(g):
	g.screen.fill(g.screen_colour)

	iblock = pygame.image.load("images/I.png")
	jblock = pygame.image.load("images/J.png")
	lblock = pygame.image.load("images/L.png")
	oblock = pygame.image.load("images/O.png")
	sblock = pygame.image.load("images/S.png")
	tblock = pygame.image.load("images/T.png")
	zblock = pygame.image.load("images/Z.png")
	iblockrect = iblock.get_rect()
	jblockrect = jblock.get_rect()
	lblockrect = lblock.get_rect()
	oblockrect = oblock.get_rect()
	sblockrect = sblock.get_rect()
	tblockrect = tblock.get_rect()
	zblockrect = zblock.get_rect()

	blockrect, block = 0, 0

	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			if g.gameboard[y][x] == 'I' or g.gameboard[y][x] == 'i':
				block = iblock
				blockrect = iblockrect				
			elif g.gameboard[y][x] == 'J' or g.gameboard[y][x] == 'j':
				block = jblock
				blockrect = jblockrect
			elif g.gameboard[y][x] == 'L' or g.gameboard[y][x] == 'l':
				block = lblock
				blockrect = lblockrect
			elif g.gameboard[y][x] == 'O' or g.gameboard[y][x] == 'o':
				block = oblock
				blockrect = oblockrect
			elif g.gameboard[y][x] == 'S' or g.gameboard[y][x] == 's':
				block = sblock
				blockrect = sblockrect
			elif g.gameboard[y][x] == 'T' or g.gameboard[y][x] == 't':
				block = tblock
				blockrect = tblockrect
			elif g.gameboard[y][x] == 'Z' or g.gameboard[y][x] == 'z':
				block = zblock
				blockrect = zblockrect

			if (block != 0):
				blockrect.x = (x*blockrect.width)
				blockrect.y = (y*blockrect.height)
				g.screen.blit(block, blockrect)
				block, blockrect = 0,0
	
	pygame.display.flip()


# adds a new block to the array
def addNewBlock(g):
	blocktoadd = g.getNewBlock()

	# check if the whole new block will fit before declaring game over
	for y in range(len(blocktoadd)):
		for x in range(len(blocktoadd[y])):
			if blocktoadd[y][x] != '0':
				if g.gameboard[y][x+3] != '0':
					g.gameover = True

	if (g.gameover == False):
		for y in range(len(blocktoadd)):
			for x in range(len(blocktoadd[y])):
				if blocktoadd[y][x] != '0':
					if g.gameboard[y][x+3] == '0':
						g.gameboard[y][x+3] = blocktoadd[y][x]
				
# main
def main():
	pygame.init()
	pygame.display.set_caption("pytris")
	g = game.Game()
	# set up game
	g.screen = pygame.display.set_mode(g.screen_size)
	g.screen.fill(g.screen_colour)

	
	# main game loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					moveFallingPieceLeft(g)
				if event.key == pygame.K_RIGHT:
					moveFallingPieceRight(g)
				if event.key == pygame.K_DOWN:
					moveFallingPieceDown(g)
				if event.key == pygame.K_UP:
					rotatePiece(g)

		timer_update(g)

if __name__ == "__main__":
    main()