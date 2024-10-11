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
        self.imageU = pg.image.load("scripts/assets/player.png").convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, (tile_size*self.imageU.get_width(),tile_size*self.imageU.get_height()))

        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.rect = self.imageU.get_rect()
        self.rect.center = (self.x,self.y)
        self.rotRect = ""
        self.image = self.imageU.copy()


        self.moveSpeed = 10
        self.velX = 0
        self.velY = 0
        self.xval = 0
        self.yval = 0
        self.turnDir = [0,0]
        self.absDir = 90
        self.isMoving = False
        self.speedPowerupActive = False
        self.speedPowerupTime = 0
        self.powerupCoolDown = 0

        self.alive = True
        self.deathTime = 0
        self.deathImage = 0


    def update(self,dt):
        keyStates = pg.key.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        mouse_bttns = pg.mouse.get_pressed()
        xDir = 0
        yDir = 0
        self.isMoving = False
        self.xCenter = self.x+self.rect.width/2
        self.yCenter = self.y + self.rect.height / 2

        if self.alive:
            # check powerups
            if self.speedPowerupActive:
                self.speedPowerupTime-=1
                if self.speedPowerupTime %20 == 0:
                    # speed particle add
                    self.game.spawnParticle("speed", "", random.randint(1, 3), False, self.rect.centerx, self.rect.centery)
                if self.speedPowerupTime == 0:
                    self.moveSpeed = 10
                    self.speedPowerupActive = False


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

            if mouse_pos[0]-self.xCenter==0:
                self.xval = 0.0001
            else:
                self.xval = mouse_pos[0]-self.xCenter
            self.yval = (mouse_pos[1]-self.yCenter)
            if self.yval == 0:
                self.yval = 0.0001
            if self.xval>0:
                self.absDir =  (365/(math.pi*2))*math.atan(self.yval/self.xval)
            else:
                self.absDir = 180+ (365 / (math.pi * 2)) * math.atan(self.yval/ self.xval)

            self.image = pg.transform.rotate(self.imageU,-self.absDir )

            if self.isMoving == True:
                #spawn particles
                pass

            if abs(xDir) and abs(yDir) == 1:
                xDir *= 0.707
                yDir *= 0.707

            if self.powerupCoolDown>0:
                self.powerupCoolDown-=1

            if keyStates[pg.K_SPACE] or keyStates[pg.K_RETURN]:
                if self.powerupCoolDown<=0:
                    try:
                        self.usePowerup(self.game.powerUps[0])
                        self.game.powerUps.pop(0)
                    except:
                        pass

            self.move(xDir,yDir)
        else:
            if self.deathTime % 5 == 0:
                if self.deathImage == 0:
                    self.image = pg.image.load("scripts/assets/particles/explosion2.png")
                    self.deathImage = 1
                else:
                    self.image = pg.image.load("scripts/assets/particles/explosion1.png")
                    self.deathImage = 0
                self.image = pg.transform.scale(self.image, (4 * self.image.get_width(), 4 * self.image.get_height()))
                self.imageU = self.image.copy()
            self.deathTime += 1
            if self.deathTime > 40:
                self.game.endGame()
                pg.mixer.Channel(0).play(pg.mixer.Sound('scripts/assets/sounds/death1.mp3'))
                self.kill()

    def usePowerup(self,powerup):
        if powerup == "heal1":
            self.game.lives+=1
            if self.game.lives>4:
                self.game.lives = 4
        elif powerup == "heal2":
            self.game.lives+=2
            if self.game.lives>4:
                self.game.lives = 4
        elif powerup == "heal3":
            self.game.lives=4

        elif powerup == "large1":
            self.game.hand.largeTime = 240
            self.game.hand.large = 1
        elif powerup == "large2":
            self.game.hand.largeTime = 300
            self.game.hand.large = 2
        elif powerup == "large3":
            self.game.hand.largeTime = 360
            self.game.hand.large = 3

        elif powerup == "speed1":
            self.moveSpeed=14
            self.speedPowerupActive = True
            self.speedPowerupTime=240
        elif powerup == "speed2":
            self.moveSpeed=18
            self.speedPowerupActive = True
            self.speedPowerupTime = 300
        elif powerup == "speed3":
            self.moveSpeed=24
            self.speedPowerupActive = True
            self.speedPowerupTime = 300

        elif powerup == "strength1":
            self.game.hand.strengthTime = 240
            self.game.hand.strength = 1
        elif powerup == "strength2":
            self.game.hand.strengthTime = 300
            self.game.hand.strength = 2
        elif powerup == "strength3":
            self.game.hand.strengthTime = 360
            self.game.hand.strength = 3

        elif powerup == "explode":
            for object in self.game.object_sprites:
                if object.type == "chest1" or object.type == "chest2" or object.type == "chest3" or object.type == "chest4":
                    pass
                else:
                    object.death = True

        self.powerupCoolDown = 60




    def move(self, x, y):
        self.velX = x*self.moveSpeed
        self.velY = y*self.moveSpeed

        self.x += self.velX
        self.y += self.velY

        self.rect.left = self.x - int(self.image.get_width()) / 2
        self.rect.top = self.y - int(self.image.get_height()) / 2

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.x = self.rect.left+int(self.image.get_width()) / 2
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = self.rect.left + int(self.image.get_width()) / 2
        if self.rect.top < 0:
            self.rect.top = 0
            self.y = self.rect.top + int(self.image.get_height()) / 2
        if self.rect.bottom>HEIGHT:
            self.rect.bottom=HEIGHT
            self.y = self.rect.top + int(self.image.get_height()) / 2

