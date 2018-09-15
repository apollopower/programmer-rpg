# Importing libraries:
import pygame, sys, random

from pygame.locals import *
from tilemap import *
from hero import *

# Initializing pygame:
pygame.init()

# Basic Constants:
BLACK = (0, 0, 0)

# Creating Game Window
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))
pygame.display.set_caption("Programmer RPG")

# pygame.key.set_repeat(10,10)

# Game loop:
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                heroRight = True
            if event.key == K_LEFT:
                heroLeft = True
            if event.key == K_UP:
                heroUp = True
            if event.key == K_DOWN:
                heroDown = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                heroRight = False
            if event.key == K_LEFT:
                heroLeft = False
            if event.key == K_UP:
                heroUp = False
            if event.key == K_DOWN:
                heroDown = False
    # End of event checker

    # Determine Player Velocity
    xVel = yVel = 0
    if (heroUp and not heroDown):
        print("lkjsdf")

    # Loading tilemap
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Draw the resource at the position in tilemap:
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))
    
    # Load Player 
    DISPLAYSURF.blit(HERO, (heroPos[0] * TILESIZE, heroPos[1] * TILESIZE))
    
    # Update Display:
    pygame.display.update()