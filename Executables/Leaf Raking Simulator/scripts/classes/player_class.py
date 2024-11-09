from scripts.settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y, game):
        super(Player, self).__init__()
        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game
        self.animSpeed = 5
        self.temp = 0
        self.temp2 = False
        self.anims = [["scripts/assets/sprites/player/1.png",14,17],["scripts/assets/sprites/player/2.png",15,18],["scripts/assets/sprites/player/3.png",14,17],["scripts/assets/sprites/player/4.png",15,18]]
        self.animNum = 0
        self.imageU = pg.image.load("scripts/assets/sprites/player/1.png").convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, (tile_size[0]*14,tile_size[1]*17))

        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rect = self.imageU.get_rect()
        self.rect.center = (self.x,self.y)
        self.rotRect = ""
        self.image = ""


        self.moveSpeed = 10
        self.velX = 0
        self.velY = 0
        self.turnDir = [0,0]
        self.absDir = 0
        self.lUp = True
        self.lLeft = False
        self.isMoving = False


    def update(self,dt):
        keyStates = pg.key.get_pressed()
        xDir = 0
        yDir = 0
        self.isMoving = False

        if keyStates[pg.K_UP] or keyStates[pg.K_w]:
            yDir -= 1
            self.isMoving = True

        if keyStates[pg.K_DOWN] or keyStates[pg.K_s]:
            yDir += 1
            self.isMoving = True

        if keyStates[pg.K_LEFT] or keyStates[pg.K_a]:
            xDir -= 1
            self.isMoving = True

        if keyStates[pg.K_RIGHT] or keyStates[pg.K_d]:
            xDir += 1
            self.isMoving = True

        if yDir == 0:
            if xDir == 1:
                self.absDir =90
                self.game.rake.x = self.x + self.game.rake.rakeNum[1]*1.3
                self.game.rake.y = self.y
            if xDir == -1:
                self.absDir =270
                self.game.rake.x = self.x - self.game.rake.rakeNum[1]*1.1
                self.game.rake.y = self.y
            if xDir == 0:
                pass
                #last spot

        if yDir == 1:
            if xDir == 1:
                self.absDir =135
                self.game.rake.x = self.x + self.game.rake.rakeNum[1]/1.05
                self.game.rake.y = self.y + self.game.rake.rakeNum[10]/1.1
            if xDir == -1:
                self.absDir =225
                self.game.rake.x = self.x - self.game.rake.rakeNum[1]
                self.game.rake.y = self.y + self.game.rake.rakeNum[10]/1.3
            if xDir == 0:
                self.absDir =180
                self.game.rake.y = self.y + self.game.rake.rakeNum[10]*1.2
                self.game.rake.x = self.x


        if yDir == -1:
            if xDir == 1:
                self.absDir =45
                self.game.rake.x = self.x + self.game.rake.rakeNum[1]/1.1
                self.game.rake.y = self.y - self.game.rake.rakeNum[10]*1.1
            if xDir == -1:
                self.absDir =315
                self.game.rake.x = self.x -self.game.rake.rakeNum[1]/1.1
                self.game.rake.y = self.y - self.game.rake.rakeNum[10]/1.1
            if xDir == 0:
                self.absDir =0
                self.game.rake.y = self.y - self.game.rake.rakeNum[10]*1.2
                self.game.rake.x = self.x

        #lol

        self.image = pg.transform.rotate(self.imageU,-self.absDir +180)
        self.game.rake.image = pg.transform.rotate(self.game.rake.imageU, -self.absDir)


        # print(self.game.rake.rect.centery,self.rect.centery)
        # print(self.image.get_width(), self.game.rake.image.get_width())


        if self.isMoving == True:
            self.temp +=1

            if self.temp>=self.animSpeed:
                self.animNum +=1
                if self.animNum >3:
                    self.animNum = 0
                self.imageU = pg.image.load(self.anims[self.animNum][0]).convert_alpha()
                self.imageU = pg.transform.scale(self.imageU, (tile_size[0]*self.anims[self.animNum][1],tile_size[1]*self.anims[self.animNum][2]))
                self.temp = 0

        if abs(xDir) and abs(yDir) == 1:
            xDir *= 0.707
            yDir *= 0.707

        self.move(xDir,yDir)

    def move(self, x, y):
        self.velX = x*self.moveSpeed
        self.velY = y*self.moveSpeed

        self.x += self.velX
        self.y += self.velY

        if self.x + self.rect.width/2>self.game.location[1][0]+self.game.location[1][1]:
            self.x = self.game.location[1][0]+self.game.location[1][1] - self.rect.width/2
        if self.x< self.game.location[1][1]:
            self.x = self.game.location[1][1]
        if self.y< self.game.location[1][3]:
            self.y = self.game.location[1][3]
        if self.y + self.rect.height/2> self.game.location[1][2]+self.game.location[1][3]:
            self.y = self.game.location[1][2]+self.game.location[1][3] - self.rect.height/2

        self.rect.left = self.x - int(self.image.get_width()) / 2
        self.rect.top = self.y - int(self.image.get_height()) / 2
        self.game.rake.rect.left = self.game.rake.x - int(self.game.rake.image.get_width()) / 2
        self.game.rake.rect.top = self.game.rake.y - int(self.game.rake.image.get_height()) / 2