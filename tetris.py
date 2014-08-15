import sys, pygame, pprint
import game

# game timer update, ticks in seconds
def timer_update(g):
	tmptime = pygame.time.get_ticks()/g.speed
	if tmptime > g.timer:
		g.timer = tmptime
		gameLoop(g)


		
# the main game loop
def gameLoop(g):
	if g.falling == False:
			g.winstatus = addNewBlock(g)
			if (g.winstatus == 1):
				print "Game Over"
	drawGame(g)


# draws the game according to the array
def drawGame(g):
	iblock = pygame.image.load("I.png")
	jblock = pygame.image.load("J.png")
	lblock = pygame.image.load("L.png")
	oblock = pygame.image.load("O.png")
	sblock = pygame.image.load("S.png")
	tblock = pygame.image.load("T.png")
	zblock = pygame.image.load("Z.png")
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
			if g.gameboard[y][x] == ('I' or 'i'):
				block = iblock
				blockrect = iblockrect				
			elif g.gameboard[y][x] == ('J' or 'j'):
				block = jblock
				blockrect = jblockrect
			elif g.gameboard[y][x] == ('L' or 'l'):
				block = lblock
				blockrect = lblockrect
			elif g.gameboard[y][x] == ('O' or 'o'):
				block = oblock
				blockrect = oblockrect
			elif g.gameboard[y][x] == ('S' or 's'):
				block = sblock
				blockrect = sblockrect
			elif g.gameboard[y][x] == ('T' or 't'):
				block = tblock
				blockrect = tblockrect
			elif g.gameboard[y][x] == ('Z' or 'z'):
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
	pprint.pprint(blocktoadd)

	for y in range(len(blocktoadd)):
		for x in range(len(blocktoadd[y])):
			if blocktoadd[y][x] != 0:
				g.gameboard[y][x] = blocktoadd[y][x]
			elif blocktoadd[y][x] == 0:
				pass
			else: #block hit another, game over
				return 1
	return 0


# main
def main():
	pygame.init()
	pygame.display.set_caption("pytet")
	g = game.Game()
	# set up game
	g.screen = pygame.display.set_mode(g.screen_size)
	g.screen.fill(g.screen_colour)

	
	# main game loop
	while 1:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()

		timer_update(g)


if __name__ == "__main__":
    main()