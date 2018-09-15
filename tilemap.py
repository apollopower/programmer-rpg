import pygame
from pygame.locals import *

# Constants for game map:
TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15

GRASS = 1

# Textures:
textures = {
    GRASS: pygame.image.load("resources/grass.png")
}

# Creating base map:
tilemap = [[GRASS for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]