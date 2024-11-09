from scripts.settings import *

class Trail(pg.sprite.Sprite):

    def __init__(self,x,y,color):
        super(Trail, self).__init__()
        self.image = pg.Surface(tile_size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
