# python 3
# used game engine: pygame
# author james roper
# title own game

#imports

import pygame

pygame.init() # initializing pygame modules

#game vars

size = width, height = 320, 240
black = 0, 0, 0
ballPos = int(width/2), int(height/2)


# screen and ball

screen = pygame.display.set_mode(size) # creates a new Surface object

ball = pygame.draw.circle(screen, (255, 0, 255), ballPos, 20)
ballrect = ball.get_rect()


# game loop

while True:
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
