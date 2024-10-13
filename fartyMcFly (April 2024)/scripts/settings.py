import os.path

import pygame as pg
import random
import math
import time
import csv

levels = [['scripts/assets/maps/level1.csv',3],['scripts/assets/maps/level2.csv',4],["scripts/assets/maps/level3.csv",2],["scripts/assets/maps/level4.csv",4],["scripts/assets/maps/level5.csv",3]]

happyParticles = ["scripts/assets/particles/happy1.png","scripts/assets/particles/happy2.png","scripts/assets/particles/happy3.png","scripts/assets/particles/happy4.png"]
sadParticles = ["scripts/assets/particles/sad1.png","scripts/assets/particles/sad2.png","scripts/assets/particles/sad3.png","scripts/assets/particles/sad4.png"]
fartParticles = ["scripts/assets/particles/fart.png","scripts/assets/particles/fart1.png"]

fartSounds = ["scripts/assets/sounds/fart1.mp3","scripts/assets/sounds/fart2.mp3","scripts/assets/sounds/fart3.mp3","scripts/assets/sounds/fart4.mp3","scripts/assets/sounds/fart5.mp3","scripts/assets/sounds/fart6.mp3","scripts/assets/sounds/fart7.mp3"]
wallSounds = ["scripts/assets/sounds/wall1.mp3","scripts/assets/sounds/wall2.mp3","scripts/assets/sounds/wall3.mp3"]

WIDTH = 720
HEIGHT = 720
tileSize = 36  # 18*2
tilexy = [20, 20]
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLACK1 = (0,0,0,70)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DGREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (190, 190, 0)
TRANSPARENT = (0,0,0,0)
GREY1 = (80, 80, 80,100)
GREY2 = (120, 120, 120)
GREY3 = (160, 160, 160)
GREY4 = (200, 200, 200)
GREY5 = (240, 240, 240)


def draw_text(screen, text, size, color, x, y, font="scripts/assets/fonts/yoster-island/yoster.ttf"):
  # font2 = pg.font.match_font(font)
  font = pg.font.Font(font, size)
  text_img = font.render(text, False, color)
  rect = text_img.get_rect()
  rect.topleft = (x, y)
  screen.blit(text_img, rect)

def draw_text_right(screen, text, size, color, x, y, font="scripts/assets/fonts/yoster-island/yoster.ttf"):
  # font2 = pg.font.match_font(font)
  font = pg.font.Font(font, size)
  text_img = font.render(text, False, color)
  rect = text_img.get_rect()
  rect.topright = (x, y)
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