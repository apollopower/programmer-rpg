import pygame
from pygame.locals import *
from tilemap import TILESIZE, MAPHEIGHT, MAPWIDTH
from camera import *


HERO = pygame.image.load("resources/hero.png")

heroPos = [(CAMERA_WIDTH / 2), (CAMERA_HEIGHT / 2)]
heroSpeed = 10

xVel = 0
yVel = 0

# Keep track of hero inputs given:
heroDirectionMap = {
    'up': False,
    'down': False,
    'left': False,
    'right': False,
}

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

def updateHero(heroDirectionMap, xVel, yVel, heroSpeed, heroPos):
    if (heroDirectionMap['up'] and not heroDirectionMap['down']):
        yVel -= heroSpeed
    if (heroDirectionMap['down'] and not heroDirectionMap['up']):
        yVel += heroSpeed
    if (heroDirectionMap['left'] and not heroDirectionMap['right']):
        xVel -= heroSpeed
    if (heroDirectionMap['right'] and not heroDirectionMap['left']):
        xVel += heroSpeed
    
    heroPos[0] += xVel / 60
    heroPos[1] += yVel / 60

    return heroPos

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