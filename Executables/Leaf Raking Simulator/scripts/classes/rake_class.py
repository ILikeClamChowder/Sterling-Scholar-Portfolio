from scripts.settings import *

class Rake(pg.sprite.Sprite):

    def __init__(self, num, game):
        super(Rake, self).__init__()

        self.rakeNum = rakeA[num]
        self.rakeNum[9] = True
        self.game = game

        self.imageU = pg.image.load(self.rakeNum[0]).convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, (tile_size[0]*self.rakeNum[2],tile_size[1]*self.rakeNum[3]))
        self.rect = self.imageU.get_rect()
        self.x = self.game.player.rect.centerx
        self.y = self.game.player.rect.top
        self.rect.center = (self.x,self.y)
        self.image = ""

    def loadNewRake(self, newRakeNum):
        self.rakeNum[6] = True
        self.rakeNum[9] = False
        self.game.rake = Rake(newRakeNum, self.game)
        self.game.all_sprites.add(self.game.rake)
        self.kill()