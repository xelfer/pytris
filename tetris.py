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
			addNewBlock(g)
	drawGame(g)


# draws the game according to the array
def drawGame(g):
	block = pygame.image.load("I.png")
	blockrect = block.get_rect()

	for y in range(len(g.gameboard)):
		for x in range(len(g.gameboard[y])):
			if g.gameboard[y][x] == 1:
				# determine block position for a block
				# y is row, x is column
				blockrect.x = (x*blockrect.width)
				blockrect.y = (y*blockrect.height)
				g.screen.blit(block, blockrect)
				pygame.display.flip()


# adds a new block to the array
def addNewBlock(g):
	blocktoadd = g.getNewBlock()
	print "Adding %s block" % blocktoadd


# main
def main():
	pygame.init()
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