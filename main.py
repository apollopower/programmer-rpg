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
pygame.display.set_icon(pygame.image.load("resources/hero.png"))


# Game loop:
while True:
    DISPLAYSURF.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                heroRight = True
                heroDirection = RIGHT
            if event.key == K_a:
                heroLeft = True
                heroDirection = LEFT
            if event.key == K_w:
                heroUp = True
                heroDirection = UP
            if event.key == K_s:
                heroDown = True
                heroDirection = DOWN
            if event.key == K_j:
                fireballs.append([heroPos[0] * TILESIZE, heroPos[1] * TILESIZE, heroDirection])
        if event.type == KEYUP:
            if event.key == K_d:
                heroRight = False
            if event.key == K_a:
                heroLeft = False
            if event.key == K_w:
                heroUp = False
            if event.key == K_s:
                heroDown = False
    # End of event checker

    # Determine Hero Velocity
    xVel = yVel = 0
    if (heroUp and not heroDown): yVel -= heroSpeed
    if (heroDown and not heroUp): yVel += heroSpeed
    if (heroLeft and not heroRight): xVel -= heroSpeed
    if (heroRight and not heroLeft): xVel += heroSpeed
    
    # Update Hero Position, and position for attack:
    heroPos[0] += xVel / 60
    heroPos[1] += yVel / 60


    # Loading tilemap
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # Draw the resource at the position in tilemap:
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column * TILESIZE, row * TILESIZE))

    # Updating fireball positions
    # for f in range(len(fireballs)):
        # fireballs[f][0] += 6

    for fireball in fireballs:
        updateFireball(fireball)
    
    # Load Player 
    DISPLAYSURF.blit(HERO, (heroPos[0] * TILESIZE, heroPos[1] * TILESIZE))

    for fireball in fireballs:
        DISPLAYSURF.blit(attacksMap[FIREBALL], pygame.Rect(fireball[0], fireball[1], 0, 0))
    
    # Update Display:
    pygame.display.update()