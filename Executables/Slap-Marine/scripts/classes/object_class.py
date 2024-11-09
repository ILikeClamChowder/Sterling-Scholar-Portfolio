from scripts.settings import *

class Object(pg.sprite.Sprite):

    def __init__(self, type, x, y,game):
        super(Object, self).__init__()
        self.game = game
        self.type = type
        self.speedY = 0
        self.speedX = 0
        self.speed = 0
        self.tolerance = 1 #smaller = more tolerance
        self.spinAmount=0
        self.absDir=0
        self.particleTime = 0
        self.changeX=0
        self.changeY=0

        # chests
        if type == "chest1":
            self.image = pg.image.load(objects[0][0][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speedY = -random.randint(1,2)
            self.speedX = random.randrange(-1,1)
            self.spinAmount = 2
        elif type == "chest2":
            self.image = pg.image.load(objects[0][1][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speedY = -random.randint(2,3)
            self.speedX = random.randrange(-1,1)
            self.spinAmount = 2
        elif type == "chest3":
            self.image = pg.image.load(objects[0][2][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speedY = -random.randint(2,3)
            self.speedX = random.randrange(-1,1)
            self.spinAmount = 2
        elif type == "chest4":
            self.image = pg.image.load(objects[0][3][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speedY = -random.randint(2,3)
            self.speedX = random.randrange(-1,1)
            self.spinAmount = 2

        # enemies
        elif type == "fish1":
            self.image = pg.image.load(objects[1][0][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 6
            self.tolerance =0.97
        elif type == "fish2":
            self.image = pg.image.load(objects[1][1][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 8
            self.tolerance = 0.94
        elif type == "fish3":
            self.image = pg.image.load(objects[1][2][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 7
            self.tolerance = 0.92
        elif type == "fish4":
            self.image = pg.image.load(objects[1][3][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 9
            self.tolerance = 0.88
        elif type == "fish5":
            self.image = pg.image.load(objects[1][4][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 11
            self.tolerance = 0.94
        elif type == "fish6":
            self.image = pg.image.load(objects[1][5][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 8
            self.tolerance = 0.89
        elif type == "fish7":
            self.image = pg.image.load(objects[1][6][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 9
            self.tolerance = 0.85
        elif type == "fish8":
            self.image = pg.image.load(objects[1][7][1])
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speed = 5
            self.tolerance = 0.80

        else:
            self.image = pg.image.load("scripts/assets/placeHolder.jpg")
            self.image = pg.transform.scale(self.image,(4*self.image.get_width(),4*self.image.get_height()))
            self.speedY = -random.randint(1, 2)

        self.imageT = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.xTop = x
        self.yLeft = y

        self.type = type
        self.temp = 0
        self.smash = False
        self.deathTime=0
        self.death=False
        self.deathImage = 0
        self.decomposing = False
        self.decomposeLevel = 255



    def update(self,dt):
        # if self.game!=False:
        #     if self.temp >= self.waitTime:
        #         if self.amount > 0:
        #             self.amount-=1
        #             if self.start:
        #                 self.game.spawnParticle(self.type,"start",self.amount)
        #             else:
        #                 pass
        #         self.temp = 0
        #     self.temp+=1
        # else:
        #     pass

        self.xCenter = self.xTop + self.rect.width / 2
        self.yCenter = self.yLeft + self.rect.height / 2

        # chests
        if self.type == "chest1":
            if self.particleTime>=40:
                self.game.spawnParticle("sparkle","",random.randint(2,5),False,self.rect.centerx,self.rect.centery)
                self.particleTime=0

                self.absDir += self.spinAmount
                self.image = pg.transform.rotate(self.imageT, self.absDir)
        elif self.type == "chest2":
            if self.particleTime>=40:
                self.game.spawnParticle("sparkle","",random.randint(3,5),False,self.rect.centerx,self.rect.centery)
                self.particleTime=0

                self.absDir += self.spinAmount
                self.image = pg.transform.rotate(self.imageT, self.absDir)
        elif self.type == "chest3":
            if self.particleTime>=40:
                self.game.spawnParticle("sparkle2","",random.randint(2,3),False,self.rect.centerx,self.rect.centery)
                self.particleTime=0

                self.absDir += self.spinAmount
                self.image = pg.transform.rotate(self.imageT, self.absDir)
        elif self.type == "chest4":
            if self.particleTime>=40:
                self.game.spawnParticle("sparkle2","",random.randint(4,6),False,self.rect.centerx,self.rect.centery)
                self.particleTime=0

                self.absDir += self.spinAmount
                self.image = pg.transform.rotate(self.imageT, self.absDir)

        # enemies
        elif self.type == "fish1" or self.type == "fish2" or self.type == "fish3" or self.type == "fish4" or self.type == "fish5" or self.type == "fish6" or self.type == "fish7" or self.type == "fish8":
            self.findPlayer()
            self.image = pg.transform.rotate(self.imageT, -self.absDir)
            self.speedX = self.xval*self.speed
            self.speedY = self.yval*self.speed
            if self.rect.left < self.game.player.x:
                if self.rect.right > self.game.player.x:
                    if self.rect.top < self.game.player.y:
                        if self.rect.bottom > self.game.player.y:
                            if not self.death:
                                self.game.spawnParticle("strength", "", random.randint(1, 3), False, self.rect.centerx,
                                                        self.rect.centery)
                                self.game.lives-=1
                                pg.mixer.Channel(5).play(pg.mixer.Sound('scripts/assets/sounds/hit1.mp3'))
                                self.kill()
        
        else:
            self.findPlayer()
            self.image = pg.transform.rotate(self.imageT, -self.absDir)
            self.speedX = self.xval*self.speed
            self.speedY = self.yval*self.speed


        if abs(self.changeX)>0:
            self.changeX=self.changeX*self.tolerance
            if abs(self.changeX)<0.01:
                self.changeX=0
        if abs(self.changeY)>0:
            self.changeY=self.changeY*self.tolerance
            if abs(self.changeY)<0.01:
                self.changeY=0

        if self.death != True:
            if (self.rect.bottom < 0 or self.rect.left > 320 * tile_size or self.rect.right < 0 or self.rect.top > 180 * tile_size):
                self.death=True
                self.image = pg.image.load("scripts/assets/particles/explosion1.png")
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()

        if self.death:
            self.speedX = 0
            self.changeX = 0
            self.speedY = 0
            self.changeY = 0
            if self.deathTime%5==0:
                if self.deathImage==0:
                    self.image = pg.image.load("scripts/assets/particles/explosion2.png")
                    self.deathImage=1
                else:
                    self.image = pg.image.load("scripts/assets/particles/explosion1.png")
                    self.deathImage=0
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()
            self.deathTime += 1
            if self.deathTime > 40:
                pg.mixer.Channel(0).play(pg.mixer.Sound('scripts/assets/sounds/death1.mp3'))
                self.kill()

        if self.decomposing:
            self.decomposeLevel-=5
            if self.decomposeLevel <0:
                self.kill()
            self.image.set_alpha(self.decomposeLevel)
            self.imageT = self.image.copy()


        self.xTop +=self.speedX +self.changeX
        self.yLeft +=self.speedY +self.changeY

        self.rect.centerx=self.xTop - self.image.get_width()/2 +self.rect.width/2
        self.rect.centery=self.yLeft - self.image.get_height()/2 +self.rect.height/2
        self.particleTime+=1


    def smashed(self,diry,dirx):
        if self.type=="chest1":
            if not self.decomposing:
                self.image = pg.image.load(objects[0][0][2])
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()
                self.game.spawnParticle("sparkle", "", random.randint(5, 8), False, self.rect.centerx, self.rect.centery)
                self.decomposing=True
                pg.mixer.Channel(1).play(pg.mixer.Sound('scripts/assets/sounds/chest1.mp3'))
                if len(self.game.powerUps) <4:
                    self.game.powerUps.append(random.choice(objects[0][0][3]))
            # add collect code
        elif self.type=="chest2":
            if not self.decomposing:
                self.image = pg.image.load(objects[0][1][2])
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()
                self.game.spawnParticle("sparkle", "", random.randint(5, 8), False, self.rect.centerx, self.rect.centery)
                self.decomposing=True
                pg.mixer.Channel(2).play(pg.mixer.Sound('scripts/assets/sounds/chest2.mp3'))
                if len(self.game.powerUps) < 4:
                    self.game.powerUps.append(random.choice(objects[0][1][3]))
        elif self.type == "chest3":
            if not self.decomposing:
                self.image = pg.image.load(objects[0][2][2])
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()
                self.game.spawnParticle("sparkle2", "", random.randint(3, 6), False, self.rect.centerx, self.rect.centery)
                self.decomposing = True
                pg.mixer.Channel(3).play(pg.mixer.Sound('scripts/assets/sounds/chest3.mp3'))
                if len(self.game.powerUps) < 4:
                    self.game.powerUps.append(random.choice(objects[0][2][3]))
        elif self.type == "chest4":
            if not self.decomposing:
                self.image = pg.image.load(objects[0][3][2])
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageT = self.image.copy()
                self.game.spawnParticle("sparkle2", "", random.randint(5, 8), False, self.rect.centerx, self.rect.centery)
                self.decomposing = True
                pg.mixer.Channel(4).play(pg.mixer.Sound('scripts/assets/sounds/chest4.mp3'))
                if len(self.game.powerUps) < 4:
                    self.game.powerUps.append(random.choice(objects[0][3][3]))
        else:
            self.smash = True
            self.changeX = 30*dirx
            self.changeY = 30*diry
            pg.mixer.Channel(5).play(pg.mixer.Sound('scripts/assets/sounds/slap.mp3'))
            self.game.spawnParticle("bubble", "", random.randint(1, 2), False, self.rect.centerx, self.rect.centery)

    def findPlayer(self):
        if self.game.player.xCenter - self.xCenter == 0:
            self.xval = 0.0001
        else:
            self.xval = self.game.player.xCenter - self.xCenter
        self.yval = (self.game.player.yCenter - self.yCenter)
        if self.yval == 0:
            self.yval = 0.0001
        if self.xval > 0:
            self.absDir = 180 + (365 / (math.pi * 2)) * math.atan(self.yval / self.xval)
        else:
            self.absDir = (365 / (math.pi * 2)) * math.atan(self.yval / self.xval)

        if abs(self.yval) > abs(self.xval):
            self.xval = abs(self.xval / self.yval) * self.xval / abs(self.xval)
            self.yval = 1 * self.yval / abs(self.yval)
        else:
            self.yval = abs(self.yval / self.xval) * self.yval / abs(self.yval)
            self.xval = 1 * self.xval / abs(self.xval)