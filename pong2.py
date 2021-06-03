#python3

'''
This is a classical Pong Game
Author: XxVinr_AlfakynxX
Version: 1.1: Updated to be OOP for better collision detection

'''

# imports and initiation
import pygame


# vars
''' Window '''
WIN_SIZE = WIDTH, HEIGHT  = 1260, 600
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Pong By XxVinr_AlfakynxX")


''' Colours '''
white = (255, 255, 255)
black = (0,0,0)
blue = (0, 231, 218)

''' Player Positions and Sizes '''
vel = 10 # player velocity
player_size = player_width, player_height = (8, 80)

''' Ball Stuff '''
ballPos = xB, yB = (int(WIDTH/3), int(HEIGHT/2)-int(player_height/2))
#ballVel = xVel, yVel = 5, 0


# classes
class Bar():
    def __init__(self, surface, colour, x, y, player_width, player_height):
        ''' initiation func '''
        self.surface = surface
        self.colour = colour
        self.x = x
        self.y = y
        self.player_width = player_width
        self.player_height = player_height
    
    def show(self):
        ''' draws the bar to the surface '''
        pygame.draw.rect(self.surface, self.colour, ((self.x, self.y), (self.player_width, self.player_height)))
    
    def move(self, option):
        ''' moves the bar '''
        keys = pygame.key.get_pressed()
        if option == "up/down":
            if keys[pygame.K_UP] and self.y > 0:
                self.y -= vel
            if keys[pygame.K_DOWN] and self.y+self.player_height < HEIGHT:
                self.y += vel
        elif option == "w/s":
            if keys[pygame.K_w] and self.y > 0:
                self.y -= vel
            if keys[pygame.K_s] and self.y+self.player_height < HEIGHT:
                self.y += vel



class Ball():
    def __init__(self, surface, colour, xB, yB, radius, xVel, yVel):
        self.surface = surface
        self.colour = colour
        self.xB = xB
        self.yB = yB
        self.radius = radius
        self.xVel = xVel
        self.yVel = yVel
        
    
    def show(self):
        pygame.draw.circle(self.surface, self.colour, (self.xB, self.yB), self.radius)
    
    def move(self):
        self.xB += self.xVel
        self.yB += self.yVel
    
    def simpleCollision(self):
        # collision detection
        ''' Collision with Walls'''
        if self.xB > WIDTH:
            self.xVel = int(self.xVel * (-1))
        if self.xB < 0:
            self.xVel = int(self.xVel * (-1))
        if self.yB > HEIGHT:
            self.yVel = int(self.yVel * (-1))
        if self.yB < 0:
            self.yVel = int(self.yVel * (-1))
        
        ''' Collision with Players '''




class MiddleLine(Bar):
    pass




# Calling Instances of Classes
''' players'''
player1 = Bar(win, white, WIDTH/5, HEIGHT/2 - 8, 8, 80)
player2 = Bar(win, white, (WIDTH/5)*4, HEIGHT/2 - 8, 8, 80)

''' ball '''
ball = Ball(win, white, xB, yB, 6, 5, 1)

''' middle line '''
middleLine = MiddleLine(win, blue, WIDTH/2-8, 0, 10, HEIGHT)


# mainloop
def main():
    running = True
    while running:
        pygame.init()
        clock = pygame.time.Clock()
        fps = 60
        
        # quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        
        
        win.fill(black)
        
        ''' Players '''
        player1.show()
        player1.move("w/s")
        
        player2.show()
        player2.move("up/down")
        
        ''' ball '''
        ball.show()
        ball.move()
        ball.simpleCollision()
        
        ''' middle line '''
        middleLine.show()
        
        pygame.display.update()
        clock.tick(fps)

        

main()
pygame.quit()