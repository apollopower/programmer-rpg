import pygame
from pygame.locals import *
from tilemap import TILESIZE, MAPHEIGHT, MAPWIDTH

HERO = pygame.image.load("resources/hero.png")

heroPos = [(MAPWIDTH / 2), (MAPHEIGHT / 2)]
heroSpeed = 10

xVel = 0
yVel = 0

# Keep track of hero inputs given:
heroUp = False
heroDown = False
heroLeft = False
heroRight = False


# Attack Constants:
FIREBALL = 0

attacksMap = {
    FIREBALL: pygame.image.load("resources/fireball.png")
}

attackToggle = False
attackPos = [heroPos[0],heroPos[1]]


