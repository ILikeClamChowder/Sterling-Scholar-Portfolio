import os.path

import pygame as pg
import random
import math
import time

TITLE = "Leaf Raking Simulator"
WIDTH = 1280
HEIGHT = 720
FPS = 60
tile_count = (64, 36)
tile_size = (4, 4)
tile_width = tile_size[0]
tile_height = tile_size[1]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (190,190,0)
GREY1 = (80, 80, 80)
GREY2 = (120, 120, 120)
GREY3 = (160, 160, 160)
GREY4 = (200, 200, 200)
GREY5 = (240, 240, 240)

# directory 0, dimensionx 1, dimensiony 2, name 3, price 4, owned? 5, effectiveness 6, strength 7, speed 8, equipped 9
roombaA = [["scripts/assets/sprites/roombas/none.png",28, 28,"None",0,True,0,0,0, False],
                        ["scripts/assets/sprites/roombas/0.png", 10, 10, "Poop Mo-beel", 65, False, 8, 1.5, 3, False],
                        ["scripts/assets/sprites/roombas/1.png", 10, 10, "Smile Bot", 470, False, 5, 5, 6, False],
                        ["scripts/assets/sprites/roombas/2.png", 14, 14, "Mr. Roomba", 3900, False, 6, 9, 8, False],
                        # ["scripts/assets/sprites/roombas/3.png", 24, 17, "Rake-mba", 100, False, 6, 15, 10, False],
                        ["scripts/assets/sprites/roombas/4.png", 28, 28, "Mammoth Roomba", 24000, False, 6, 40, 5, False],
                        ["scripts/assets/sprites/roombas/5.png", 24, 24, "Angry Bot", 138000, False, 6, 30, 12, False]]

# directory 0, offset x 1, dimensionx 2, dimensiony 3, name 4, price 5, owned? 6, effectiveness 7, strength 8, equipped 9, offset y 10
rakeA = [["scripts/assets/sprites/rakes/0.png", 35, 5 ,6, "A Metal Spoon?", 0, True, 1.2 , 2, False, 35],
              ["scripts/assets/sprites/rakes/1.png", 45, 9 ,10, "Sand Scooper", 95, False, 0.5, 5, False, 37],
              ["scripts/assets/sprites/rakes/2.png", 55, 23, 23, "Grandma's Rake", 700, False, 0.7, 12, False, 55],
              ["scripts/assets/sprites/rakes/3.png", 55, 35, 23, "Extended Rake", 4400, False, 1, 12, False, 55],
              ["scripts/assets/sprites/rakes/4.png", 63, 5, 42, "Knockback Stick", 23000, False, 4, 10, False, 75],
              ["scripts/assets/sprites/rakes/5.png", 80, 30, 10, "Magic Rake", 128000, False, 1, 20, False, 80],
              # ["scripts/assets/sprites/rakes/rake23Gold.png", 55, 23, 23, "Golden Rake", 4000, False, 10, 10, False, 55]
         ]


def draw_text(screen, text, color, x, y, font, baba = False): #optimize this

    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.topleft = (x, y)
    screen.blit(text_img, rect)
    if baba:
        return [rect.right,rect.left]

def draw_text_center(screen, text, color, x, y, font):
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.midtop = (x, y)
    screen.blit(text_img, rect)

def draw_screen(path, x, y, screen):
    test_img = pg.image.load(path).convert_alpha()
    test_img = pg.transform.scale(test_img, (WIDTH, HEIGHT))
    rect = test_img.get_rect()
    rect.x = x
    rect.y = y
    screen.blit(test_img, rect)