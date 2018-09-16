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

# Keep track of hero direction
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

heroDirection = RIGHT

# Attack Constants:
FIREBALL = 0
fireballSpeed = 10

attacksMap = {
    FIREBALL: pygame.image.load("resources/fireball.png")
}

fireballs = []

def updateFireball(fireball):
    if fireball[2] == RIGHT:
        fireball[0] += fireballSpeed
    elif fireball[2] == LEFT:
        fireball[0] -= fireballSpeed
    elif fireball[2] == UP:
        fireball[1] -= fireballSpeed
    elif fireball[2] == DOWN:
        fireball[1] += fireballSpeed