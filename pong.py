#python3

'''
This is a classical Pong Game

Author: XxVinr_AlfakynxX
Version: 1.0: First Version. No OOP and no collision with bars
Version: 1.1: Updated to be OOP for better collision detection. Still no collision with bars
Version: 1.2:   <----  TODO  ----> Updated to have working collisions

'''

# imports and initiation
import pygame
from time import sleep


# vars
''' Window '''
WIN_SIZE = WIDTH, HEIGHT  = 1260, 600
win = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption("Pong By XxVinr_AlfakynxX")


''' Colours '''
white = (255, 255, 255)
black = (0,0,0)
blue = (0, 231, 218)
red = (255, 0, 0)

''' Player Positions and Sizes '''
vel = 10 # player velocity
player_size = player_width, player_height = (8, 80)

''' Ball Stuff '''
ballPos = xB, yB = (int(WIDTH/3), int(HEIGHT/2)-int(player_height/2))
#ballVel = xVel, yVel = 5, 0


# classes
class Bar():
    def __init__(self, playername, surface, colour, x, y, player_width, player_height):
        ''' initiation func '''
        self.playername = playername
        self.surface = surface
        self.colour = colour
        self.x = x
        self.y = y
        self.player_width = player_width
        self.player_height = player_height
        self.score = 0
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
    
    def hitboxRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.player_width, self.player_height)
        
    def show(self):
        ''' draws the bar to the surface '''
        pygame.draw.rect(self.surface, self.colour, self.rect)
    
    def getScore(self):
        print("Score of {0}: {1}".format(self.playername, self.score))
    
    def scoreMax(self):
        if self.score >= 7:
            running = False
            print("Game Over!")
            pygame.quit()
    
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
        self.rect = pygame.Rect(self.xB, self.yB, self.radius*2, self.radius*2)
        self.turn = True
    
    def hitboxBall(self):
        self.rect = pygame.Rect(self.xB, self.yB, self.radius*2+15, self.radius*2+15)
    
    def show(self):
        pygame.draw.ellipse(self.surface, self.colour, (self.rect))
    
    def move(self):
        self.xB += self.xVel
        self.yB += self.yVel
        
    
    def reset(self):
        self.xB, self.yB = (int(WIDTH/3), int(HEIGHT/2)-int(player_height/2))
        self.xVel = 12
        self.yVel = 5
        
    def simpleCollision(self, bar1, bar2):
        ''' Collision with Walls && SCORING + RESETTING'''
        if self.xB + self.radius >= WIDTH:
            bar2.score +=1
            sleep(.200)
            self.reset()
            bar1.getScore()
            bar2.getScore()
            bar1.scoreMax()
            bar2.scoreMax()
            
        if self.xB <= 0:
            bar1.score +=1
            sleep(.200)
            self.reset()
            bar1.getScore()
            bar2.getScore()
            bar1.scoreMax()
            bar2.scoreMax()
            
        if self.yB + self.radius >= HEIGHT:
            self.yVel = int(self.yVel * (-1))
        if self.yB <= 0:
            self.yVel = int(self.yVel * (-1))
        
        ''' Collision with Players '''
        if self.turn == True:        
            if self.rect.colliderect(bar1.rect) or self.rect.colliderect(bar2.rect):
                self.xVel *= -1
                self.turn = False
        elif self.turn == False:
            if self.rect.colliderect(middleLine.rect):
                self.turn = True
    


class MiddleLine(Bar):
    pass




# Calling Instances of Classes
''' players'''
player1 = Bar("player1", win, white, WIDTH/5, HEIGHT/2 - 8, 8, 80)
player2 = Bar("player2", win, white, (WIDTH/5)*4, HEIGHT/2 - 8, 8, 80)

''' ball '''
ball = Ball(win, white, xB, yB, 6, 12, 5)

''' middle line '''
middleLine = MiddleLine("noplayer", win, blue, WIDTH/2-8, 0, 10, HEIGHT)


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
        player1.hitboxRect()
        player1.show()
        player1.move("w/s")

        
        player2.hitboxRect()
        player2.show()
        player2.move("up/down")
        
        ''' ball '''
        ball.hitboxBall()
        ball.show()
        ball.move()
        ball.simpleCollision(player1, player2)
        
        
        ''' middle line '''
        middleLine.hitboxRect()
        middleLine.show()
        
        
        pygame.display.update()
        clock.tick(fps)

        
        

main()
pygame.quit()