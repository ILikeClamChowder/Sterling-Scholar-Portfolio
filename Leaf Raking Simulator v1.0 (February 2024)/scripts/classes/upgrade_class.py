from scripts.settings import *


class Upgrade(pg.sprite.Sprite):

    def __init__(self, x, y, img):
        super(Upgrade, self).__init__()

        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)

        self.image = pg.image.load(img).convert_alpha()
        self.image = pg.transform.scale(self.image, tile_size)
        self.image.set_colorkey((255,0,255,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.moveSpeedY = 0
        self.moveSpeedX = 0
        self.pushing = False
        self.alphaLvl = 0
        self.image.set_alpha(self.alphaLvl)






    def update(self,dt):
        pass


    def animate(self):
        pass
