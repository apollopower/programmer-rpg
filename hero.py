import pygame
from pygame.locals import *

HERO = pygame.image.load("resources/hero.png")

heroPos = [0,0]
heroSpeed = 300

xVel = 0
yVel = 0

# Keep track of hero inputs given:
heroUp = False
heroDown = False
heroLeft = False
heroRight = False