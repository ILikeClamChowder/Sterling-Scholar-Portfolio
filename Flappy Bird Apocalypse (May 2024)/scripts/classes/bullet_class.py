from scripts.settings import *

class Bullet(pg.sprite.Sprite):

    def __init__(self,type,x,y,speed,rot=0):
        super(Bullet, self).__init__()
        self.waitTime=120
        self.type=type
        self.speedDif = [0, 0]
        self.speed = speed
        self.rot=rot
        self.x = x
        self.y = y

        if self.type==0 or self.type==1:
            self.image = pg.image.load("scripts/assets/sprites/background/warning tube.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, rot)
            self.rect = self.image.get_rect()
            self.rect.topright = (x-25, y+25)
            # if rot==90:
            #     self.rect.bottomleft = (x,y)
        elif self.type==2:
            self.image = pg.image.load("scripts/assets/sprites/background/warning cheep.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, rot+90)
            self.rect = self.image.get_rect()
            self.rect.topright = (x-25, y+25)
            if rot==90:
                self.rect.topright = (x, y+25)
        elif self.type==3:
            self.image = pg.image.load("scripts/assets/sprites/background/warning bullet bill.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, rot-90)
            self.rect = self.image.get_rect()
            self.rect.topright = (x-25, y-25)
            if rot==90:
                self.rect.topright = (x, y+25)





    def prepReal(self):
        if self.type==0: # bottom pipe
            self.image = pg.image.load("scripts/assets/sprites/background/bottomtube.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.x, self.y)
            if self.rot==90:
                self.rect.bottomleft = (self.x,self.y)
        elif self.type==1: # top pipe
            self.image = pg.image.load("scripts/assets/sprites/background/toptube.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (self.x, self.y)
            if self.rot==90:
                self.rect.bottomright = (self.x,self.y)
        elif self.type==2: # cheep cheep
            self.image = pg.image.load("scripts/assets/sprites/background/cheeocgeeo.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (self.x, self.y)
            self.spawnTime=0
        elif self.type==3: # bullet bill
            self.image = pg.image.load("scripts/assets/sprites/background/bulletbill.png")
            self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide))
            self.image = pg.transform.rotate(self.image,self.rot)
            self.rect = self.image.get_rect()
            self.rect.bottomleft = (self.x, self.y)
            self.spawnTime = 0

    def update(self):
        if self.waitTime>0:
            self.waitTime-=1
            if self.waitTime<=0:
                self.prepReal()
        else:
            if self.type==2: # cheep cheep
                self.spawnTime+=1
                self.speedDif[1]+=(self.spawnTime)*0.0005

            self.rect.centerx += self.speed[0]+self.speedDif[0]
            self.rect.centery += self.speed[1]+self.speedDif[1]
