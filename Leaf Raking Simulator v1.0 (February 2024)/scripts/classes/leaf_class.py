from scripts.settings import *


class Leaf(pg.sprite.Sprite):

    def __init__(self, game, x, y, price,image, sizex, sizey):
        super(Leaf, self).__init__()

        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game
        self.imageF = image
        self.image = pg.image.load(image).convert_alpha()
        self.image = pg.transform.scale(self.image, (tile_size[0]*sizex,tile_size[1]*sizey))
        self.image.set_colorkey((255,0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.moveSpeedY = 0
        self.moveSpeedX = 0
        self.pushing = False
        self.price = price
        self.alphaLvl = 0
        self.image.set_alpha(self.alphaLvl)
        self.pushedByRake = False
        self.pushedByRoomba = False


    def pushed(self,speedX,speedY):

        if  abs(self.moveSpeedX) < abs(speedX):
            if self.moveSpeedX*speedX >= 0:
                self.moveSpeedX = speedX *1.1 * self.game.rake.rakeNum[7]
        if abs(self.moveSpeedY) < abs(speedY):
            if self.moveSpeedY*speedY >= 0:
                self.moveSpeedY = speedY *1.1 * self.game.rake.rakeNum[7]
        self.pushedByRake = True

    def roombaPushed(self,speedX,speedY):
        if  abs(self.moveSpeedX) < abs(speedX):
            if self.moveSpeedX*speedX >= 0:
                self.moveSpeedX = speedX *1.1 * self.game.roomba.roombaNum[6]
        if abs(self.moveSpeedY) < abs(speedY):
            if self.moveSpeedY*speedY >= 0:
                self.moveSpeedY = speedY *1.1 * self.game.roomba.roombaNum[6]
        self.pushedByRoomba = True




    def update(self,dt):
        if self.rect.top >= self.game.location[1][2] + self.game.location[1][3] or self.rect.bottom <= self.game.location[1][3] or self.rect.left >= self.game.location[1][0] + self.game.location[1][1] or self.rect.right <= self.game.location[1][1]:
            # add to presents
            self.game.addCurrency(self.price)
            self.game.spawnLeaf(self.price,self.imageF,self.game.location[9][0],self.game.location[9][1])
            self.kill()

        if self.pushedByRake:
            self.moveSpeedX *= 1-1/self.game.rake.rakeNum[8]
            self.moveSpeedY *= 1-1/self.game.rake.rakeNum[8]
        elif self.pushedByRoomba:
            if self.game.roomba.roombaActive:
                self.moveSpeedX *= 1 - 1 / self.game.roomba.roombaNum[7]
                self.moveSpeedY *= 1 - 1 / self.game.roomba.roombaNum[7]
        if abs(self.moveSpeedX) < 0.001:
            self.moveSpeedX = 0
        if abs(self.moveSpeedY) < 0.001:
            self.moveSpeedY = 0
        self.move(self.moveSpeedX,self.moveSpeedY)

        if self.alphaLvl < 255:
            self.alphaLvl += 10
            self.image.set_alpha(self.alphaLvl)


        self.animate()


    def animate(self):
        self.image.set_colorkey((0, 0, 255, 0.0))




    def move(self, x, y):
        self.rect.centerx += x
        self.rect.centery += y