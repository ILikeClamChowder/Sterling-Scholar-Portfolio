from scripts.settings import *

class Hand(pg.sprite.Sprite):

    def __init__(self, game):
        super(Hand, self).__init__()
        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game

        self.open = pg.image.load("scripts/assets/hands/open.png").convert_alpha()
        self.open = pg.transform.scale(self.open, (tile_size*self.open.get_width(),tile_size*self.open.get_height()))
        self.closed = pg.image.load("scripts/assets/hands/closed.png").convert_alpha()
        self.closed = pg.transform.scale(self.closed,(tile_size * self.closed.get_width(), tile_size * self.closed.get_height()))

        #strength1
        self.open1 = pg.image.load("scripts/assets/hands/open.png").convert_alpha()
        self.open1 = pg.transform.scale(self.open1,(tile_size * self.open1.get_width(), tile_size * self.open1.get_height()))
        self.closed1 = pg.image.load("scripts/assets/hands/closed.png").convert_alpha()
        self.closed1 = pg.transform.scale(self.closed1,(tile_size * self.closed1.get_width(), tile_size * self.closed1.get_height()))

        # strength2
        self.open2 = pg.image.load("scripts/assets/hands/open.png").convert_alpha()
        self.open2 = pg.transform.scale(self.open2,(tile_size * self.open2.get_width(), tile_size * self.open2.get_height()))
        self.closed2 = pg.image.load("scripts/assets/hands/closed.png").convert_alpha()
        self.closed2 = pg.transform.scale(self.closed2,(tile_size * self.closed2.get_width(), tile_size * self.closed2.get_height()))

        # strength3
        self.open3 = pg.image.load("scripts/assets/hands/open.png").convert_alpha()
        self.open3 = pg.transform.scale(self.open3,(tile_size * self.open3.get_width(), tile_size * self.open3.get_height()))
        self.closed3 = pg.image.load("scripts/assets/hands/closed.png").convert_alpha()
        self.closed3 = pg.transform.scale(self.closed3,(tile_size * self.closed3.get_width(), tile_size * self.closed3.get_height()))



        self.imageU = self.open
        self.imageU.set_alpha(1)

        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rect = self.imageU.get_rect()
        self.rect.center = (self.x,self.y)
        self.image = self.imageU.copy()

        self.alphaLevel = 0
        self.absDir = 90
        self.smash = False
        self.smashTime = 0
        self.strength = 0
        self.strengthTime = 0
        self.large = 0
        self.largeTime = 0
        self.largeResized = False
        self.largeSizeAmount = 0



    def update(self,dt):
        if self.alphaLevel<200:
            self.alphaLevel+=5
            self.imageU.set_alpha(self.alphaLevel)

        if self.strength > 0:
            self.strengthTime-=1
            if self.strengthTime %20 ==0:
                # strength particle add
                self.game.spawnParticle("strength", "", random.randint(1, 3), False, self.rect.centerx,
                                        self.rect.centery)
            if self.strengthTime<=0:
                self.strength=0

        if self.large > 0:
            self.largeTime-=1
            if self.largeTime %20 ==0:
                # large particle add
                self.game.spawnParticle("speed", "", random.randint(1, 3), False, self.rect.centerx,
                                        self.rect.centery)
            if self.largeTime<=0:
                self.large=0
                self.imageU = pg.transform.scale(self.imageU,(self.imageU.get_width() /self.largeSizeAmount, self.imageU.get_height()/self.largeSizeAmount))
                self.image = pg.transform.scale(self.image,(self.image.get_width() /self.largeSizeAmount, self.image.get_height() /self.largeSizeAmount))

        mouse_pos = pg.mouse.get_pos()
        mouse_pressed = pg.mouse.get_pressed()



        # self.xCenter = self.x + self.rect.width / 2
        # self.yCenter = self.y + self.rect.height / 2
        self.xCenter = self.game.player.xCenter
        self.yCenter = self.game.player.yCenter

        if mouse_pos[0]-self.xCenter==0:
            xval = 0.0001
        else:
            xval = mouse_pos[0]-self.xCenter
        yval = (mouse_pos[1]-self.yCenter)
        if yval == 0:
            yval = 0.0001
        if xval>0:
            self.absDir = 90+ (365/(math.pi*2))*math.atan(yval/xval)
        else:
            self.absDir = 270+ (365 / (math.pi * 2)) * math.atan(yval/ xval)




        if abs(yval)>abs(xval):
            xval=abs(xval/yval) *xval/abs(xval)
            yval =1 *yval/abs(yval)
        else:
            yval = abs(yval/xval) *yval/abs(yval)
            xval = 1 *xval/abs(xval)


        if mouse_pressed[0]:
            if self.smash==False:
                self.smash=True
                self.imageU = self.closed
                self.largeResized = False
                for object in self.game.object_sprites:
                    if self.rect.left < object.rect.right:
                        if self.rect.right > object.rect.left:
                            if self.rect.top < object.rect.bottom:
                                if self.rect.bottom > object.rect.top:
                                    if self.strength==1:
                                        object.smashed(yval*1.45, xval*1.45)
                                    elif self.strength==2:
                                        object.smashed(yval*1.9, xval*1.9)
                                    elif self.strength==3:
                                        object.smashed(yval*3.5, xval*3.5)
                                    else:
                                        object.smashed(yval, xval)

            else:
                pass

        self.image = pg.transform.rotate(self.imageU,-self.absDir)

        self.move(xval * 35 * tile_size, yval * 35 * tile_size)
        self.handSmash()

        if self.largeResized == False and self.large>0:
            if self.large==1:
                self.largeSizeAmount=1.3
                self.imageU = pg.transform.scale(self.imageU,(self.imageU.get_width()*1.3,self.imageU.get_height()*1.3))
                self.image = pg.transform.scale(self.image,(self.image.get_width()*1.3,self.image.get_height()*1.3))
            elif self.large ==2:
                self.largeSizeAmount = 1.7
                self.imageU = pg.transform.scale(self.imageU,(self.imageU.get_width() * 1.7, self.imageU.get_height() * 1.7))
                self.image = pg.transform.scale(self.image,(self.image.get_width() * 1.7, self.image.get_height() * 1.7))
            elif self.large ==3:
                self.largeSizeAmount = 2.2
                self.imageU = pg.transform.scale(self.imageU,(self.imageU.get_width() * 2.2, self.imageU.get_height() * 2.2))
                self.image = pg.transform.scale(self.image,(self.image.get_width() * 2.2, self.image.get_height() * 2.2))
            self.largeResized = True


    def move(self, x, y):

        # self.x += self.velX
        # self.y += self.velY
        #
        # if self.rect.right > WIDTH:
        #     self.x-=self.velX
        # if self.rect.left < 0:
        #     self.x-=self.velX
        # if self.rect.top < 0:
        #     self.y-=self.velY
        # if self.rect.bottom>HEIGHT:
        #     self.y-=self.velY
        #  - int(self.image.get_width()) / 2  - int(self.image.get_height()) / 2
        self.rect.left = self.game.player.x- int(self.image.get_width()) / 2 +x
        self.rect.top = self.game.player.y - int(self.image.get_height()) / 2 +y

    def handSmash(self):
        if self.smash:
            self.smashTime+=1
            if self.smashTime >= 10:
                self.imageU = self.open
                self.largeResized = False
            if self.smashTime>=15:
                self.smash=False
                self.smashTime = 0