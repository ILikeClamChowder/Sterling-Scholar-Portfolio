import os.path

import pygame as pg
import random
import math
import time

TITLE = "Going Deeper"
WIDTH = 1280
HEIGHT = 720
FPS = 60
tile_count = (320, 180)
tile_size = 4

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

# chests, enemies
# name, location closed, location open, effects
# name, location
objects = [[["chest1","scripts/assets/chests/chest1/closed.png","scripts/assets/chests/chest1/open.png",["heal1","speed1","strength1"]],
            ["chest2","scripts/assets/chests/chest2/closed.png","scripts/assets/chests/chest2/open.png",["heal1","strength1","heal2","speed1","speed2"]],
            ["chest3","scripts/assets/chests/chest3/closed.png","scripts/assets/chests/chest3/open.png",["heal2","heal3","speed3","speed2","strength2","explode"]],
            ["chest4","scripts/assets/chests/chest4/closed.png","scripts/assets/chests/chest4/open.png",["heal3","speed3","strength3","explode"]],],

           [["fish1","scripts/assets/enemies/piranha.png"],["fish2","scripts/assets/enemies/fish2.png"],["fish3","scripts/assets/enemies/fish3.png"],["fish4","scripts/assets/enemies/fish4.png"],["fish5","scripts/assets/enemies/fish5.png"],["fish6","scripts/assets/enemies/fish6.png"],["fish7","scripts/assets/enemies/fish7.png"],["fish8","scripts/assets/enemies/fish8.png"],]]


# [[level main object 1],[level random object 1, ...], wave length, [0, spawn max]],...
levelInfo = [[[objects[0][0],objects[1][0]],[],2,[0,60]],
             [[objects[1][1]],[objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[0][0],objects[1][1]],4,[0,40]],
             [[objects[0][0]],[objects[1][0]],6,[0,40]], # fish 1 wave
             [[objects[1][1],objects[1][1],objects[1][1],objects[0][1]],[objects[1][1],objects[1][0],objects[1][0],objects[1][0],objects[0][0],objects[1][1]],6,[0,40]],
             [[objects[1][2],objects[1][1],objects[1][1],objects[0][1]],[objects[1][2],objects[1][1],objects[1][1],objects[1][0],objects[0][1],objects[0][0],objects[1][0]],7,[0,40]],
             [[objects[0][0],objects[0][0]],[objects[1][1]],7,[0,40]], # fish 2 wave
             [[],[objects[1][2],objects[1][1],objects[1][1],objects[1][0],objects[1][0],objects[0][0],objects[0][1]],15,[0,28]], #every 7 waves spawn mass amounts
             [[objects[1][2],objects[1][2],objects[1][1]],[objects[1][2],objects[1][1],objects[1][1],objects[1][0],objects[0][0],objects[1][0]],8,[0,30]],
             [[objects[0][1]],[objects[1][2]],6,[0,35]], # fish 3 wave
             [[objects[1][3],objects[1][2],objects[0][2]],[objects[1][2],objects[1][1],objects[1][1],objects[1][0],objects[0][0],objects[1][0]],10,[0,30]],
             [[objects[1][3],objects[1][3],objects[0][2]],[objects[1][2],objects[1][1],objects[1][1],objects[1][1],objects[1][1],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[0][0],objects[1][0]],12,[0,25]],
             [[objects[1][4],objects[1][3],objects[1][3],objects[0][1]],[objects[0][3],objects[0][1],objects[1][0],objects[1][1],objects[1][2],objects[1][3],objects[1][0],objects[1][1],objects[1][2],objects[1][2]],12,[0,25]],
             [[objects[1][4],objects[1][4],objects[1][4]],[objects[1][0],objects[1][1],objects[1][2],objects[1][3],objects[1][0],objects[1][1],objects[1][2],objects[1][2],objects[1][3]],14,[0,20]],
             [[objects[0][2]],[objects[1][0],objects[1][0],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[0][0]],30,[0,32]], #mass wave
             [[],[objects[1][0]],7,[0,30]], # filler wave
             [[objects[0][1],objects[0][1]],[objects[1][3]],7,[0,35]], # fish 4 wave
             [[objects[1][5]],[objects[0][0],objects[0][1],objects[0][2],objects[1][0],objects[1][0],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4]],15,[0,16]],
             [[objects[1][5],objects[1][5]],[objects[0][0],objects[0][1],objects[1][0],objects[1][0],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4]],15,[0,15]],
             [[objects[0][2],objects[0][2]],[objects[1][4]],7,[0,40]], # fish 5 wave
             [[],[objects[0][0],objects[0][1],objects[0][2],objects[1][5],objects[1][5],objects[1][4],objects[1][4],objects[1][4],objects[1][3],objects[1][4],objects[1][5],objects[1][5],objects[1][4],objects[1][4],objects[1][4],objects[1][3],objects[1][4]],17,[0,15]],
             [[objects[0][3]],[objects[1][0],objects[1][0],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5],objects[0][0]],30,[0,28]], #mass wave
             [[objects[1][6]],[objects[0][1],objects[0][2],objects[1][0],objects[1][4],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5]],16,[0,12]],
             [[objects[0][3]],[objects[1][5]],6,[0,30]], # fish 6 wave
             [[objects[1][6],objects[1][5],objects[1][5]],[objects[0][1],objects[0][2],objects[1][0],objects[1][4],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5]],17,[0,16]],
             [[objects[0][1]],[objects[0][1],objects[0][2],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][0]],30,[0,20]], # mass piranha
             [[objects[1][6],objects[1][6],objects[1][5]],[objects[0][1],objects[0][2],objects[1][0],objects[1][4],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5]],17,[0,12]],
             [[objects[0][3]],[objects[1][6]],6,[0,25]], # fish 7 wave
             [[],[objects[1][0],objects[1][6],objects[1][5],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5],objects[1][6]],30,[0,25]], #mass wave
             [[objects[1][7]],[objects[0][3],objects[0][2],objects[1][0],objects[1][4],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][5],objects[1][5],objects[1][6],objects[1][6]],17,[0,15]],
             [[],[objects[1][7]],5,[0,22]], # fish 8 wave
             [[objects[0][0],objects[0][1],objects[0][2],objects[0][3]],[],4,[0,22]], # prepare for infinite waves
             [[],[objects[0][3],objects[0][2],objects[0][1],objects[1][0],objects[1][0],objects[1][0],objects[1][0],objects[1][1],objects[1][1],objects[1][1],objects[1][1],objects[1][2],objects[1][2],objects[1][3],objects[1][3],objects[1][4],objects[1][4],objects[1][5],objects[1][5],objects[1][6],objects[1][6],objects[1][7],objects[1][7]],22,[0,24]], # infinite waves
            ]


def draw_text(screen, text, size, color, x, y, font="scripts/assets/fonts/yoster-island/yoster.ttf"):

    font = pg.font.Font(font, size)
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.topleft = (x, y)
    screen.blit(text_img, rect)

def draw_text_center(screen, text, size, color, x, y, font="scripts/assets/fonts/yoster-island/yoster.ttf"):

    font = pg.font.Font(font, size)
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

