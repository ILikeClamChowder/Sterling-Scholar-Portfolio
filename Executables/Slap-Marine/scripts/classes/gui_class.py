from scripts.settings import *

class GUI(pg.sprite.Sprite):

    def __init__(self, type, x, y, sizeX, sizeY, form, totalSize=False, square = False):
        super(GUI, self).__init__()
        self.xpos = x
        self.ypos = y
        self.width = sizeX
        self.height = sizeY
        self.type = type
        self.imageT = ""
        self.square = square

        if form == "color":
            self.color = form
            self.t = (self.width,self.height)
            self.image = pg.Surface(self.t)
            self.image.fill(WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (self.xpos, self.ypos)
        else:
            self.color = form
            self.image = pg.image.load(self.color).convert_alpha()
            if totalSize == True:
                self.updateImageTS(self.color)
            elif totalSize == "baba":
                height = self.image.get_height()
                width = self.image.get_width()
                if width > height:
                    self.image = pg.transform.scale(self.image, (75, height/(width/75)))
                    self.imageT = pg.transform.scale(self.image, (75, height/(width/75)))
                else:
                    self.image = pg.transform.scale(self.image, (width/(height/75), 75))
                    self.imageT = pg.transform.scale(self.image, (width/(height/75), 75))
                self.ypos = self.ypos - 25
            else:
                self.image = pg.transform.scale(self.image, (tile_size[0]*self.width,tile_size[1]*self.height))
                self.imageT = pg.transform.scale(self.image, (tile_size[0]*self.width,tile_size[1]*self.height))
            self.rect = self.image.get_rect()
            self.rect.center = (self.xpos, self.ypos)

        pg.display.flip()

    def updateImageTS(self,image):
        self.image = pg.image.load(image).convert_alpha()
        if self.square:
            height = self.image.get_height()
            width = self.image.get_width()
            if width > height:
                self.image = pg.transform.scale(self.image, (self.width, height / (width / self.height)))
                self.imageT = pg.transform.scale(self.image, (self.width, height / (width / self.height)))
            else:
                self.image = pg.transform.scale(self.image, (width / (height / self.width), self.height))
                self.imageT = pg.transform.scale(self.image, (width / (height / self.width), self.height))
        else:
            self.image = pg.transform.scale(self.image, (self.width, self.height))
            self.imageT = pg.transform.scale(self.image, (self.width, self.height))





