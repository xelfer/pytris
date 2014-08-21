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
	drawGame(g)
	if (g.gameover == False):
		if g.falling == False:
			addNewBlock(g)
			drawGame(g)
		else:
			moveFallingPieceDown(g)
		lineCheck(g)

def lineCheck(g):
	for y in range(len(g.gameboard)):
		fullline = True
		for x in range(len(g.gameboard[y])):
			if (g.gameboard[y][x] == '0'):
				fullline = False
		if (fullline): #remove line y
			# make that matched row 'none'
			for x in range(len(g.gameboard[y])):
				g.gameboard[y][x] = None
			# swap it 
			g.gameboard.reverse()
			g.gameboard = removeBlankRows(g.gameboard)
			g.gameboard.append(['0' for i in xrange(g.boardwidth)])
			g.gameboard.reverse()

def removeBlankRows(grid):
    return [list(row) for row in grid if any(row)]

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

def rotateArray(block):
	return zip(*block[::-1])

def rotatePiece(g):
	# create a 4x4 with the piece to rotate
	block = g.block

	print g.currentBlock
	if g.currentBlock == 'O': 
		pass
	else:
		block = rotateArray(block)
		# check if the block clashes with anything
		rotate = True
		yy,xx = g.blockpos # offset
		# fix bounds
		if xx > (g.boardwidth-4):
			xx = g.boardwidth-4
		elif xx < 0:
			xx = 0
		if yy > (g.boardheight-4):
			yy = g.boardheight-4

		for y in range(len(block)):
			for x in range(len(block[y])):
				
				if (x+xx < g.boardwidth-1) and (y+yy < g.boardheight-1):
					if (re.match(r'[a-z]', g.gameboard[y+yy][x+xx], flags=0)):
						rotate = False

		if (rotate):
			# clear the old one
			for y in range(len(g.gameboard)):
				for x in range(len(g.gameboard[y])):
					move = re.match(r'[A-Z]', g.gameboard[y][x], flags=0)
					if(move):
						g.gameboard[y][x] = '0'
			# add the new one
			for y in range(len(block)):
				for x in range(len(block[y])):
					g.gameboard[y+yy][x+xx] = block[y][x]
			g.block = list(block)
			pprint.pprint(g.block)
		
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
	g.getNewBlock()
	blocktoadd = g.block
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

	drawGame(g)

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