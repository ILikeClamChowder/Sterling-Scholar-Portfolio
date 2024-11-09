from scripts.settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, start,intro):
        super(Player, self).__init__()
        if start:
            playerImg1 = pg.image.load("scripts/assets/sprites/player/1.png").convert_alpha()
            playerImg2 = pg.image.load("scripts/assets/sprites/player/2.png").convert_alpha()
            playerImg3 = pg.image.load("scripts/assets/sprites/player/3.png").convert_alpha()
        else:
            playerImg1 = pg.image.load("scripts/assets/sprites/apocPlayer/1.png").convert_alpha()
            playerImg2 = pg.image.load("scripts/assets/sprites/apocPlayer/2.png").convert_alpha()
            playerImg3 = pg.image.load("scripts/assets/sprites/apocPlayer/3.png").convert_alpha()
        self.playerImages = [playerImg1,playerImg2,playerImg3]
        self.playerImgNum = 0

        self.image = self.playerImages[self.playerImgNum]
        self.image = pg.transform.scale(self.image, [self.image.get_width()*tileDivide,self.image.get_height()*tileDivide])
        self.imageT = self.image.copy()

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.radius = 20
        self.dirX = 1
        self.speedIncY = 0
        self.gravity=0.4
        self.speedX = 5
        self.rotAmount =0
        self.rotating = False
        self.flipped = False
        self.animCount = 0
        self.playerActive=True
        self.intro = intro
        self.startTime = 0


        # starts vars
        self.start = start
        if self.start or self.intro:
            self.speedX=0
            self.rect.centery = HEIGHT/1.5
            self.playerActive=False
        elif not self.intro and not self.start:
            self.startTime=300
            self.speedX = 0
            self.rect.centery = HEIGHT / 1.5
            self.playerActive=False


    def update(self):
        if self.animCount>6:
            self.animate()
            self.animCount=0
        self.animCount+=1
        if self.start or self.intro or self.startTime>0:
            self.startMove()
            mouseKeys = pg.mouse.get_pressed()
        else:
            self.move()

        if self.startTime>0:
            self.startTime-=1
            if self.startTime %20>=12:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)

            if self.startTime<=0:
                self.intro = False
                self.speedX = 5
                self.playerActive = True
                self.startTime = 0

        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.top<0:
            self.rect.top=20*tileDivide



    def animate(self):
        self.playerImgNum+=1
        if self.playerImgNum>len(self.playerImages)-1:
            self.playerImgNum=0
        self.imageT = self.playerImages[self.playerImgNum]
        self.imageT = pg.transform.scale(self.imageT, [self.imageT.get_width()*tileDivide,self.imageT.get_height()*tileDivide])
        self.image = self.imageT
        self.flipped=False

    def startMove(self):
        if self.rect.centery>HEIGHT/1.5:
            self.dirX = 1
            self.speedIncY = -5
            if self.flipped:
                self.flipped = False
                self.imageT = pg.transform.flip(self.imageT, True, False)
                self.image = self.imageT
        elif not self.flipped:
            if self.dirX==-1:
                self.flipped = True
                self.imageT = pg.transform.flip(self.imageT, True, False)
                self.image = self.imageT

        self.speedIncY += self.gravity
        # rotating
        if self.speedIncY>=5:
            self.rotating=True
            if self.dirX==-1:
                self.rotAmount += 3
                if self.rotAmount >= 90:
                    self.rotAmount = 90
            else:
                self.rotAmount -= 3
                if self.rotAmount <= -90:
                    self.rotAmount <= -90
            self.image = pg.transform.rotate(self.imageT,self.rotAmount)
        elif self.rotating:
            self.rotating=False
            self.rotAmount=0
            self.image = pg.transform.rotate(self.imageT, self.rotAmount)


        self.rect.centerx += self.dirX * self.speedX
        self.rect.centery += self.speedIncY

    def move(self):



        self.speedIncY+=self.gravity
        # rotation
        if self.speedIncY>=5:
            self.rotating=True
            if self.dirX==-1:
                self.rotAmount += 3
                if self.rotAmount >= 90:
                    self.rotAmount = 90
            else:
                self.rotAmount -= 3
                if self.rotAmount <= -90:
                    self.rotAmount <= -90
            self.image = pg.transform.rotate(self.imageT,self.rotAmount)
        elif self.rotating:
            self.rotating=False
            self.rotAmount=0
            self.image = pg.transform.rotate(self.imageT, self.rotAmount)

        elif not self.flipped:
            if self.dirX == -1:
                self.flipped = True
                self.imageT = pg.transform.flip(self.imageT, True, False)
                self.image = self.imageT



        self.rect.centerx += self.dirX*self.speedX
        self.rect.centery += self.speedIncY


    def playerJump(self):
        pg.mixer.Channel(0).play(jumpSound)
        mousePos = pg.mouse.get_pos()
        if self.intro or self.startTime>0:
            self.intro = False
            self.speedX = 5
            self.playerActive=True
            self.startTime=0


        if self.playerActive:

            if mousePos[0] < WIDTH / 2:
                self.dirX = -1
                self.speedIncY = -6
                if not self.flipped:
                    self.flipped = True
                    self.imageT = pg.transform.flip(self.imageT, True, False)
                    self.image = self.imageT
            else:
                self.dirX = 1
                self.speedIncY = -6
                if self.flipped:
                    self.flipped = False
                    self.imageT = pg.transform.flip(self.imageT, True, False)
                    self.image = self.imageT