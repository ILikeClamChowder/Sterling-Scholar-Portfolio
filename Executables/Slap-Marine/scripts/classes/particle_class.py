from scripts.settings import *

class Particle(pg.sprite.Sprite):

    def __init__(self, type, x, y, amount, game = False, waitTime = 10, start=False):
        super(Particle, self).__init__()
        self.game = game
        self.start = start
        self.speedX = 0
        self.speedY = 0
        if game!=False:
            self.type = type
            self.amount = amount
            self.waitTime = waitTime

        if type == "bubble":
            self.image = pg.image.load("scripts/assets/particles/bubble.png")
            self.speedY = -random.randint(3,6)
            x += random.randint(-4,4)*tile_size
        elif type == "sparkle":
            self.image = pg.image.load("scripts/assets/particles/sparkle.png").convert_alpha()
            while self.speedX==0 and self.speedY ==0:
                self.speedY = random.randint(-1,1)
                self.speedX = random.randint(-1,1)
                self.decayTime = 255
        elif type == "sparkle2":
            self.image = pg.image.load("scripts/assets/particles/sparkle2.png").convert_alpha()
            while self.speedX==0 and self.speedY ==0:
                self.speedY = random.randint(-1,1)
                self.speedX = random.randint(-1,1)
                self.decayTime = 255
        elif type == "strength":
            self.image = pg.image.load("scripts/assets/particles/strength.png").convert_alpha()
            while self.speedX==0 and self.speedY ==0:
                self.speedY = random.randint(-1,1)
                self.speedX = random.randint(-1,1)
                self.decayTime = 255
        elif type == "speed":
            self.image = pg.image.load("scripts/assets/particles/speed.png").convert_alpha()
            while self.speedX==0 and self.speedY ==0:
                self.speedY = random.randint(-1,1)
                self.speedX = random.randint(-1,1)
                self.decayTime = 255
        elif type == "large":
            self.image = pg.image.load("scripts/assets/particles/sparkle2.png").convert_alpha()
            while self.speedX==0 and self.speedY ==0:
                self.speedY = random.randint(-1,1)
                self.speedX = random.randint(-1,1)
                self.decayTime = 255
        else:
            self.image = pg.image.load("scripts/assets/placeHolder.jpg")

        self.image = pg.transform.scale(self.image,(self.image.get_width() * tile_size, self.image.get_height() * tile_size))
        self.imageT = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.startX = x
        self.startY = y

        self.type = type
        self.temp = 0






    def update(self,dt):
        if self.game!=False:
            if self.temp >= self.waitTime:
                if self.amount > 0:
                    self.amount-=1
                    if self.start:
                        self.game.spawnParticle(self.type,"start",self.amount)
                    else:
                        self.game.spawnParticle(self.type, "", 0, False, self.startX,self.startY)
                self.temp = 0
            self.temp+=1
        else:
            pass

        if self.type == "bubble":
            pass
        elif self.type == "sparkle" or self.type=="sparkle2" or self.type=="strength" or self.type == "speed":
            self.decayTime-=4
            if self.decayTime<=0:
                self.kill()
            self.image.set_alpha(self.decayTime)


        self.rect.centery+=self.speedY
        self.rect.centerx+=self.speedX

        if self.start:
            if self.rect.top <= 145*tile_size:
                self.kill()
        else:
            if self.rect.top < 0 or self.rect.left >320*tile_size or self.rect.right<0 or self.rect.bottom>180*tile_size:
                self.kill()