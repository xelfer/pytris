import sys, pygame, pprint
import game

# game timer update, ticks in seconds
def timer_update(g):
	tmptime = pygame.time.get_ticks()/g.speed
	if tmptime > g.timer:
		g.timer = tmptime
		drawGame(g)


		
# the main game loop
def gameLoop(g):
	if g.falling == False:
			addNewBlock(g)


# draws the game according to the array
def drawGame(g):

	x,y=0,0
	for row in g.gameboard:
		for cell in row:
			if cell == 1:
				# determine block position for a block
				# y is row, x is column
				block = pygame.image.load("block.png")
				blockrect = block.get_rect()
				blockrect.x = (x*blockrect.width)
				blockrect.y = (y*blockrect.height)
				g.screen.blit(block, blockrect)
				pygame.display.flip()

			x=x+1
		x=0
		y=y+1


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
		gameLoop(g)


if __name__ == "__main__":
    main()