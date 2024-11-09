import os.path

import pygame as pg
import random
import math

TITLE = "SLIME GAME"
WIDTH = 1280
HEIGHT = 720
FPS = 60
tile_count = (64, 36)
# 8 to 56 x       8 to 35 y
tile_size = (WIDTH/tile_count[0], HEIGHT/tile_count[1])
tile_width = tile_size[0]
tile_height = tile_size[1]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 55, 55)
GREEN = (55, 255, 55)
BLUE = (5, 55, 255)
PINK = (255, 55, 255)
CYAN = (55, 255, 255)
YELLOW = (255, 255, 55)
playerColors = [RED, GREEN, BLUE, PINK, CYAN, YELLOW]

UICOLOR = (177,177,177)
UIRED = (208,75,75)

def draw_text(screen, text, size, color, x, y, font="scripts/assets/3x4PixelRedo (4).ttf"):
    font = pg.font.Font(font, size)
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.midtop = (x, y)
    screen.blit(text_img, rect)

def draw_text_left(screen, text, size, color, x, y, font="scripts/assets/3x4PixelRedo (4).ttf"):
    font = pg.font.Font(font, size)
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.topleft = (x, y)
    screen.blit(text_img, rect)