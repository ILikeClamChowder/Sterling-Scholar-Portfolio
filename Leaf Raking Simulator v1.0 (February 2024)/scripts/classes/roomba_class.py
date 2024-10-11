from scripts.settings import *


class Roomba(pg.sprite.Sprite):

    def __init__(self,num, game):
        super(Roomba, self).__init__()

        self.roombaNum = roombaA[num]
        self.roombaNum[9] = True
        self.roombaActive = ""
        self.game = game


        self.imageU = pg.image.load(self.roombaNum[0]).convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, (tile_size[0] * self.roombaNum[1] , tile_size[1] * self.roombaNum[2]))
        self.image = self.imageU
        self.rect = self.imageU.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.realCenter = [WIDTH / 2, HEIGHT / 2]
        self.direction = 0
        self.desination = [random.randint(-20,self.game.location[1][0]+20)+self.game.location[1][1],random.randint(-20,self.game.location[1][2]+20)+self.game.location[1][3]]
        self.speedXfr = 0
        self.speedYfr = 0

        if abs(self.desination[1] - self.realCenter[1]) > abs(self.desination[0] - self.realCenter[0]):
            if self.desination[1] > self.realCenter[1]:
                self.velY = 1
            else:
                self.velY = -1
            self.velX = (self.desination[0] - self.realCenter[0]) / abs(self.desination[1] - self.realCenter[1])
        else:
            if self.desination[0] > self.realCenter[0]:
                self.velX = 1
            else:
                self.velX = -1
            self.velY = (self.desination[1] - self.realCenter[1]) / abs(self.desination[0] - self.realCenter[0])

        if num == 0:
            self.roombaActive = False
            self.rect.center = (WIDTH*2, HEIGHT*2)
        else:
            self.roombaActive = True

        #self.slope = (self.desination[1] - self.realCenter[1]) / (self.desination[0] - self.realCenter[0])



    def update(self,dt):
        if self.roombaActive:
            if self.realCenter[0] > self.desination[0]-self.roombaNum[8]-5 and self.realCenter[0] < self.desination[0]+self.roombaNum[8]+5:
                # print("xpas",self.velX)
                # print(self.realCenter[1],self.desination[1]-self.roombaNum[8]-5,self.desination[1]+self.roombaNum[8]+5)
                if self.realCenter[1] > self.desination[1]-self.roombaNum[8]-5 and self.realCenter[1] < self.desination[1]+self.roombaNum[8]+5:
                    # print("change destination")
                    self.desination = [random.randint(0, self.game.location[1][0]) + self.game.location[1][1],random.randint(0, self.game.location[1][2]) + self.game.location[1][3]]
                    # find slope
                    if abs(self.desination[1] - self.realCenter[1]) > abs(self.desination[0] - self.realCenter[0]):
                        if self.desination[1] > self.realCenter[1]:
                            self.velY = 1
                        else:
                            self.velY = -1
                        self.velX = (self.desination[0] - self.realCenter[0]) / abs(self.desination[1] - self.realCenter[1])
                    else:
                        if self.desination[0] > self.realCenter[0]:
                            self.velX = 1
                        else:
                            self.velX = -1
                        self.velY = (self.desination[1] - self.realCenter[1]) / abs(self.desination[0] - self.realCenter[0])
            if self.velX > 0:
                angle = 90 - (365/(math.pi*2))*math.atan(self.velY/self.velX)
            else:
                angle = 270 - (365/(math.pi * 2))*math.atan(self.velY/self.velX)
            self.image = pg.transform.rotate(self.imageU, angle)


            self.move()

            # if random.randint(0,80) == 1:
            #     print("roomba change direction")
            #     self.direction = random.randint(0,360)
            #     self.image = pg.transform.rotate(self.imageU, self.direction)
            # elif self.rect.top >= self.game.location[1][2] or self.rect.bottom <= self.game.location[1][3] or self.rect.left >= self.game.location[1][0] or self.rect.right <= self.game.location[1][1]:
            #     print("roomba change direction")
            #     self.direction +=180
            #     self.image = pg.transform.rotate(self.imageU, self.direction)
            # self.move(self.direction)


    def move(self):
        # self.velX = math.sin(dir*(math.pi/180))*self.roombaNum[8]
        # self.velY = math.cos(dir*(math.pi/180))*self.roombaNum[8]
        self.speedXfr = self.velX * self.roombaNum[8]
        self.speedYfr = self.velY * self.roombaNum[8]
        self.realCenter[0] += self.speedXfr
        self.realCenter[1] += self.speedYfr
        self.rect.centerx = math.floor(self.realCenter[0])
        self.rect.centery = math.floor(self.realCenter[1])

    def loadNewRoomba(self, newRoombaNum):
        self.roombaNum[9] = False
        self.game.roomba = Roomba(newRoombaNum, self.game)
        print(newRoombaNum)
        self.game.all_sprites.add(self.game.roomba)
        self.kill()
