from scripts.settings import *

class PowerUp(pg.sprite.Sprite):

    def __init__(self,game):
        super(PowerUp, self).__init__()
        # POWERUPS: invincibility for period, jumping, speedup/speeddown, rewind, shoot projectile, detroy tail, bomb
        # Name 0, Directory 1, Use amount 2
        self.powerUpA = [["bomb","scripts/assets/sprites/PU/bomb.png", 1],
                         ["invincibility","scripts/assets/sprites/PU/invincibility.png", 1],
                         ["jump","scripts/assets/sprites/PU/jump.png", 3],
                         ["rewind","scripts/assets/sprites/PU/rewind.png", 1],
                         # ["speed down", "scripts/assets/sprites/PU/speeddown.png", 1],
                         # ["speed up", "scripts/assets/sprites/PU/speedup.png", 1],
                         # ["rewind","scripts/assets/sprites/PU/your_mom.png", 1]
                         ]
        self.powerUpNum = random.choice(self.powerUpA)
        # self.powerUpNum = self.powerUpA[random.randint(0,3)]
        # self.powerUpNum = self.powerUpA[3]

        self.game = game
        self.image = pg.Surface(tile_size)
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.topleft = [random.randint(8,55)*tile_size[0],random.randint(8,34)*tile_size[1]]
        self.temp = 0
        self.temp2 = 0
        self.owned = False
        self.active = False
        self.temp3 = 0
        self.invincibleTime = 0
        self.player = ""
        self.temp4 = 0


        while True:
            num1 = 0
            for player in self.game.players:
                if self.rect.topleft == player.rect.topleft:
                    self.rect.topleft = [random.randint(8, 56) * tile_size[0], random.randint(8, 35) * tile_size[1]]
                else:
                    num1+=1
                    self.temp2+=1
            if num1>=2:
                break

    def update(self, dt):
        self.temp+=1
        if self.temp >= 3:
            self.temp=0
            self.image.fill(random.choice(playerColors))
        if self.invincibleTime > 0:
            self.invincibleTime -=1
            self.player.color = WHITE
            if self.invincibleTime <=0:
                self.player.image.fill(self.playerColor)
                self.player.color = self.playerColor

        for player in self.game.players:
            if player.rect.topleft == self.rect.topleft:
                self.owned = True
                self.playerOwned = player.num
        if self.owned:
            if self.active:
                if self.powerUpNum[0] == self.powerUpA[0][0]:
                    self.rect.center = self.player.rect.center
                    for trail in self.game.trails:
                        if abs(self.rect.centerx-trail.rect.centerx) < 125 and abs(self.rect.centery-trail.rect.centery) < 125:
                            self.game.trails.remove(trail)
                            trail.kill()
                            self.active = False
                            self.owned = False
                        pass
                elif self.powerUpNum[0] == self.powerUpA[3][0]:
                    temp = len(self.player.playerTiles)
                    if temp >= 40:
                        for trail in self.game.trails:
                            # for tile in self.player.playerTiles[-10:]:
                            for i in range(0,40):
                                if trail.rect.center == (self.player.playerTiles[temp-i-1][0],self.player.playerTiles[temp-i-1][1]):
                                    trail.kill()
                                    print("yaya")
                                    break
                        temp = self.player.playerTiles[len(self.player.playerTiles) - 40]
                        self.player.rect.centerx = temp[0]
                        self.player.rect.centery = temp[1]
                        del self.player.playerTiles[-40:]
                        self.player.aiMovement()
                    elif temp >= 20:
                        for trail in self.game.trails:
                            # for tile in self.player.playerTiles[-10:]:
                            for i in range(0,20):
                                if trail.rect.center == (self.player.playerTiles[temp-i-1][0],self.player.playerTiles[temp-i-1][1]):
                                    trail.kill()
                                    print("yaya")
                                    break
                        temp = self.player.playerTiles[len(self.player.playerTiles) - 20]
                        self.player.rect.centerx = temp[0]
                        self.player.rect.centery = temp[1]
                        del self.player.playerTiles[-20:]
                        self.player.aiMovement()
                    self.active = False
                    self.owned = False

                # elif self.powerUpNum[0] == self.powerUpA[4][0]:
                #     self.player.speed *= 1/2
                #
                #     self.owned = False
                #     self.active = False
                #
                # elif self.powerUpNum[0] == self.powerUpA[5][0]:
                #     pass
                #
                #     self.owned = False
                #     self.active = False




                #use more than once
                if self.invincibleTime <=0:
                    if self.powerUpNum[0] == self.powerUpA[1][0]:
                        self.invincibleTime = 60
                        self.temp4 += 1
                        self.active = False
                        if self.temp4 >= self.powerUpNum[2]:
                            self.owned = False
                            self.active = False
                            self.temp4 = 0

                    elif self.powerUpNum[0] == self.powerUpA[2][0]:
                        self.invincibleTime = 6
                        self.temp4+=1
                        self.active = False
                        if self.temp4>=self.powerUpNum[2]:
                            self.owned = False
                            self.active = False
                            self.temp4 = 0
                else:
                    # animation for owned but not use
                    pass





    def usePowerup(self,player,num):
        if self.owned:
            if self.playerOwned == num:
                self.active = True
                self.player = player
                self.playerColor = self.player.color
