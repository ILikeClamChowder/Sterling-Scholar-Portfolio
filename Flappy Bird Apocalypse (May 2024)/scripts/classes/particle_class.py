from scripts.settings import *

class Particle(pg.sprite.Sprite):

    def __init__(self, type, x, y, amount, game = False, moveVec=[],decayTime=255):
        super(Particle, self).__init__()
        self.game = game
        self.moveVec = moveVec
        if game!=False:
            self.type = type
            self.amount = amount


        self.image = pg.image.load(type)
        self.image = pg.transform.scale(self.image,(self.image.get_width() * tileDivide, self.image.get_height() * tileDivide)).convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.startX = x
        self.startY = y

        self.type = type
        self.decayTime=decayTime






    def update(self):
        if self.game!=False:
            if self.amount > 0:
                self.amount-=1
                self.game.spawnParticle(self.type, 0, self.startX,self.startY,self.moveVec,self.decayTime)
        else:
            pass

        self.rect.centery+=self.moveVec[1]
        self.rect.centerx+=self.moveVec[0]
        self.image.set_alpha(self.decayTime)

        self.decayTime-=1
        if self.decayTime<=0:
            self.kill()

        if self.rect.top < 0 or self.rect.left >WIDTH or self.rect.right<0 or self.rect.bottom>HEIGHT:
            self.kill()