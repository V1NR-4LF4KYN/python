# import and init pygame
import pygame as pg;
from pygame.locals import *
pg.init()


# IMPORTANT VARS
ACTIVE: bool = True # game running or not
clock = pg.time.Clock() # for fps setting
win_width:int = 800
win_height:int = 450
FPS: int = 40
playerxPos = 0 #int(win_width/2 - 50)
playeryPos:int = int(win_height/2 - 50)
bulletxPos = playerxPos

# Colours
WHITE = (100,255,255)
RED = (255, 20, 20)




# Classes

class Bullet:
	def __init__(self):
		global bulletxPos
		self.xSize = 12
		self.ySize = 8
		self.xPos = bulletxPos
		self.yPos = playeryPos + 50 + self.ySize/2
		bulletxPos = self.xPos
		self.size = (self.xSize, self.ySize)
		self.vel = 60
		self.screen = screen
		pg.draw.rect(self.screen, RED, (self.xPos, self.yPos, self.xSize, self.ySize))

	def move(self):
		global bulletxPos
		bulletxPos += self.vel
		





class Player:
	def __init__(self):
		self.x = playerxPos
		self.y = int(win_height/2 - 50)
		self.pos = (self.x, self.y)
		self.vel = 10
		self.screen = screen
		self.shot = False
		self.bulletlst = []
		self.colour = (100,100,100) # grey
		pg.draw.rect(self.screen, self.colour, (self.x, self.y, 100, 100))

	def move(self):
		global playerxPos, bulletxPos
		keys = pg.key.get_pressed()
		if keys[pg.K_a] and playerxPos > 0:
			print("a pressed...")
			playerxPos -= self.vel
		if keys[pg.K_d] and playerxPos < win_width - 100:
			print("d pressed...")
			playerxPos +=  self.vel

		# shooting
		if keys[pg.K_SPACE] and not self.bulletlst:
			print("space pressed...")
			self.shot = True
			while self.shot:
				for i in range(3): # burst fire
					bullet = Bullet()
					self.bulletlst.append(bullet)
					bullet.move()

				# deleting bullets once they are out of screen
				if bulletxPos > win_width:
					for bullet in self.bulletlst:
						del bullet
					self.shot = False
					bulletxPos = playerxPos + 100
					print("hit the target!!!")
		#tst
		if keys[pg.K_q]:
			print(self.bulletlst)





while ACTIVE:
	# checking for user's actions
	for event in pg.event.get():
		if event.type == pg.QUIT:
			ACTIVE = False
			print("\nPygame Quitted...")


	



	# getting the display
	screen = pg.display.set_mode((win_width, win_height)) # set screen
	screen.fill(WHITE) # fill background


	# getting a player
	p1 = Player()
	p1.move()


	pg.display.update() # renew the screen 

	# setting refresh time (60fps)
	clock.tick(FPS)





# safe exit out of pygame
pg.quit()


