from scripts.settings import *

class Particle(pg.sprite.Sprite):

    def __init__(self, type, x, y, amount, game = False, waitTime = 10, start=False, flipped = False,moveVec=[]):
        super(Particle, self).__init__()
        self.game = game
        self.start = start
        self.speedX = 0
        self.speedY = 0
        if game!=False:
            self.type = type
            self.amount = amount
            self.waitTime = waitTime


        self.image = pg.image.load(type)
        if type == "scripts/assets/particles/fart.png" and self.start:
            if flipped:
                self.speedX = random.randint(1,3)
            else:
                self.speedX = -random.randint(1,3)
                self.image = pg.transform.flip(self.image,True,False)
            self.decayTime = 150
        elif self.start:
            self.speedY = -random.randint(1,4)
            self.decayTime = 255
        elif type == "scripts/assets/particles/fart.png":
            if flipped:
                self.speedX = random.randint(1, 3)
            else:
                self.speedX = -random.randint(1, 3)
                self.image = pg.transform.flip(self.image, True, False)
            self.decayTime = 60
            self.moveVec = moveVec


        self.image = pg.transform.scale(self.image,(self.image.get_width() * 2, self.image.get_height() * 2))
        self.imageT = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.startX = x
        self.startY = y

        self.type = type
        self.temp = 0






    def update(self):
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

        if self.start:
            self.decayTime-=1
            if self.decayTime<=0:
                self.kill()


        self.rect.centery+=self.speedY
        self.rect.centerx+=self.speedX
        if self.type=="scripts/assets/particles/fart.png":
            self.image.set_alpha(self.decayTime*2)
        else:
            self.image.set_alpha(self.decayTime)

        if self.start:
            if self.rect.top <= 0:
                self.kill()
        else:
            if self.rect.top < 0 or self.rect.left >WIDTH or self.rect.right<0 or self.rect.bottom>HEIGHT:
                self.kill()