import os.path

import pygame as pg
import random
import math
import asyncio

WIDTH = 576
HEIGHT = 1024
FPS = 60
realTile = [144,256]
tileDivide = WIDTH/realTile[0]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY1 = (80, 80, 80)
GREY2 = (120, 120, 120)
GREY3 = (160, 160, 160)
GREY4 = (200, 200, 200)
GREY5 = (240, 240, 240)
char1color = (255, 84, 72)
char2color = (255, 157, 72)
char1colorApoc = (215, 44, 32)
char1colorApoc2 = (215, 24, 12)
poop = (84,56,71)

# text, text color
introText = [["Captain, the detonation device is ready.","scripts/assets/sounds/clip1.ogg",char2color],
             ["I am preparing to seal it within this metal bo-","scripts/assets/sounds/clip2.ogg",char2color],
             ["... Uhhhhhmmmm","scripts/assets/sounds/clip3.ogg",char2color],
             [""],
             ["Lieutenant, did you put it in the box?","scripts/assets/sounds/clip4.ogg",char1color],
             [""],
             ["...","scripts/assets/sounds/clip5.ogg",char2color],
             [""],
             ["Lieutenant?","scripts/assets/sounds/clip6.ogg",char1color],
             [""],
             ["uhhhhh...","scripts/assets/sounds/clip7.ogg",char2color],
             [""],
             ["Lieutenant, did you just drop the","scripts/assets/sounds/clip8.ogg",char1color],
             ["detonation device out of the aircraft?!","scripts/assets/sounds/clip9.ogg",char1color],
             [""],
             ["wait okay okay everything should be okay sir,","scripts/assets/sounds/clip10.ogg",char2color],
             ["as long as the detonation device does not","scripts/assets/sounds/clip11.ogg",char2color],
             ["get pressed by anything,","scripts/assets/sounds/clip12.ogg",char2color],
             ["we should not have any issues.","scripts/assets/sounds/clip13.ogg",char2color]]

introText2 = [["Lieutenant, *cough* are you alive?!","scripts/assets/sounds/1clip1.ogg",char1colorApoc],
              [""],
              ["Lieutenant!!","scripts/assets/sounds/1clip2.ogg",char1colorApoc],
              ["No... No! This can't be happening","scripts/assets/sounds/1clip3.ogg",char1colorApoc],
              [""],
              ["I saw that bird,","scripts/assets/sounds/1clip4.ogg",char1colorApoc],
              ["*cough* it was that bird that did this!","scripts/assets/sounds/1clip6.ogg",char1colorApoc],
              [""],
              ["I will get my revenge, even if it kills me","scripts/assets/sounds/1clip5.ogg",char1colorApoc2]]

aboutText = [["Welcome to Flappy Bird: Apocalypse!","scripts/assets/sounds/thing.ogg",char2color],
             ["This game was created by Tate Ence,","scripts/assets/sounds/thing.ogg",char2color],
             ["and was submitted to the Bullet Hell Jam 5","scripts/assets/sounds/thing.ogg",char2color],
             [""],
             ["This game takes place in a war tarn land.","scripts/assets/sounds/thing.ogg",char2color],
             ["control Flappy Bird as you avoid the","scripts/assets/sounds/thing.ogg",char2color],
             ["consequences of setting off a nucleur bomb!","scripts/assets/sounds/thing.ogg",char2color],
             [""],
             ["The movement in this game is slightly","scripts/assets/sounds/thing.ogg",char2color],
             ["different than the original,","scripts/assets/sounds/thing.ogg",char2color],
             ["tap on each side of your screen to","scripts/assets/sounds/thing.ogg",char2color],
             ["change your direction!","scripts/assets/sounds/thing.ogg",char2color],
             [""],
             ["Thanks for playing! Have fun!","scripts/assets/sounds/thing.ogg",char2color]]


clickSounds = ["scripts/assets/sounds/to1.ogg","scripts/assets/sounds/to2.ogg","scripts/assets/sounds/to3.ogg","scripts/assets/sounds/to4.ogg","scripts/assets/sounds/to5.ogg","scripts/assets/sounds/to6.ogg","scripts/assets/sounds/to7.ogg"]

levelText = [["It is finally time to show this bird that you reap what you show",char1colorApoc2],
             [""],
             []]

# sounds
pg.mixer.init()
startHeli = pg.mixer.Sound('scripts/assets/sounds/helicpoter.ogg')
dingSound = pg.mixer.Sound('scripts/assets/sounds/ding.ogg')
deathSound = pg.mixer.Sound('scripts/assets/sounds/death.ogg')
jumpSound = pg.mixer.Sound('scripts/assets/sounds/jump.ogg')


# 1 x axis tube
# 2 x axis cheep
# 3 x axis bullet bill
# 4 y axis tube
# 5 y axis cheep
# 6 y axis bullet bill

#other, spawn time, spawn min, spawn amount
levelData = [[[1],1,120,1],
             [[3,4],90,40,2],
             [[2],90,30,2],
             [[1,2,6],90,40,4],
             [[1,2,3,4,5,6],100,50,91]]


def draw_text(screen, text, color, x, y, font):
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.topleft = (x, y)
    screen.blit(text_img, rect)

def draw_text_right(screen, text, color, x, y, font):
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.topright = (x, y)
    screen.blit(text_img, rect)

def draw_text_center(screen, text, color, x, y, font):
    text_img = font.render(text, False, color)
    rect = text_img.get_rect()
    rect.midtop = (x, y)
    screen.blit(text_img, rect)