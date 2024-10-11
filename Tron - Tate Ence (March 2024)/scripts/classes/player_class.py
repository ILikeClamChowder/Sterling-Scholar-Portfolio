from scripts.settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y,color,game,input,num,ai):
        super(Player, self).__init__()
        self.image = pg.Surface(tile_size)
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x*tile_size[0],y*tile_size[1])
        self.game = game
        self.speed = 1
        self.playerTiles = []
        self.input = input
        self.num = num
        self.ai = ai
        self.lastMovements = []
        self.aiDying = False
        self.prevDirs = [False, False, False, False]
        if self.input == "WASD":
            self.lastPressed = [1, 0]
        else:
            self.lastPressed = [-1, 0]
        self.alive = True
        self.temp = 0

    def update(self,dt):
        self.temp+=1
        # if self.temp <= self.speed:
        self.playerTiles.append([self.rect.centerx, self.rect.centery])
        if (self.rect.right >= 57*tile_size[0]) or (self.rect.left <= 7*tile_size[0]) or (self.rect.bottom >= 36*tile_size[1]) or (self.rect.top <= 7*tile_size[1]):
            self.killPlayer()
        if self.alive:
            if self.ai:
                    self.aiMovement()

            else:
                keyStates = pg.key.get_pressed()
                if self.input == "WASD":
                    self.up = keyStates[pg.K_w]
                    self.down = keyStates[pg.K_s]
                    self.left = keyStates[pg.K_a]
                    self.right = keyStates[pg.K_d]
                else:
                    self.up = keyStates[pg.K_UP]
                    self.down = keyStates[pg.K_DOWN]
                    self.left = keyStates[pg.K_LEFT]
                    self.right = keyStates[pg.K_RIGHT]

                if self.up or self.down:
                    if self.down:
                        if self.lastPressed[1]==-1:
                            self.game.powerUp.usePowerup(self,self.num)
                    else:
                        if self.lastPressed[1]==1:
                            self.game.powerUp.usePowerup(self,self.num)
                if self.left or self.right:
                    if self.right:
                        if self.lastPressed[0]==-1:
                            self.game.powerUp.usePowerup(self,self.num)
                    else:
                        if self.lastPressed[0]==1:
                            self.game.powerUp.usePowerup(self,self.num)
                if (self.lastPressed[0]!=0) and (self.up or self.down):
                    if self.down:
                        self.lastPressed = [0,1]
                    else:
                        self.lastPressed = [0,-1]
                elif (self.lastPressed[1]!=0) and (self.left or self.right):
                    if self.right:
                        self.lastPressed = [1, 0]
                    else:
                        self.lastPressed = [-1, 0]

            self.move(self.lastPressed[0], self.lastPressed[1])

        # if keyStates[pg.K_UP] or keyStates[pg.K_w]:
        #     self.lastPressed[1] = -1
        # if keyStates[pg.K_DOWN] or keyStates[pg.K_s]:
        #     self.lastPressed[1] = 1
        # if keyStates[pg.K_LEFT] or keyStates[pg.K_a]:
        #     self.lastPressed[0] = -1
        # if keyStates[pg.K_RIGHT] or keyStates[pg.K_d]:
        #     self.lastPressed[0] = 1


    def aiMovement(self):
        # add last movements to list "lastMovements" then see if the movements are the same or soemthing idk
        prevPressed = [0,0]
        prevPressed[0] = self.lastPressed[0]
        prevPressed[1] = self.lastPressed[1]


        right = False
        left = False
        top = False
        bottom = False
        if self.rect.right >= 56 * tile_size[0]:
            right = True
        elif self.rect.left <= 8 * tile_size[0]:
            left = True
        if self.rect.top <= 8 * tile_size[1]:
            top = True
        elif self.rect.bottom >= 35 * tile_size[1]:
            bottom = True
        for trail in self.game.trails:
            if trail.rect.centery == self.rect.centery:
                if self.rect.right == trail.rect.left:
                    right = True
                elif self.rect.left == trail.rect.right:
                    left = True
            if trail.rect.centerx == self.rect.centerx:
                if self.rect.top == trail.rect.bottom:
                    top = True
                elif self.rect.bottom == trail.rect.top:
                    bottom = True

        i = 0
        unneeded1top = False
        unneeded1bottom = False
        unneeded1all = False
        unneeded2top = False
        unneeded2bottom = False
        unneeded2all = False
        while True:
            i += 1
            if top or bottom:
                if top and bottom:
                    self.lastPressed[1] = 0
                elif bottom:
                    unneeded1bottom = True
                elif top:
                    unneeded1top = True
            else:
                unneeded1all = True

            if left or right:
                if left and right:
                    self.lastPressed[0] = 0
                elif left:
                    unneeded2top = True
                elif right:
                    unneeded2bottom = True
            else:
                unneeded2all = True


            if unneeded1all:
                if unneeded2bottom:
                    self.lastPressed[0] = random.randint(-1, 0)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(-1, 1)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2top:
                    self.lastPressed[0] = random.randint(0, 1)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(-1, 1)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2all:
                    self.lastPressed[1] = random.randint(-1, 1)
                    if self.lastPressed[1] == 0:
                        self.lastPressed[0] = random.randint(-1, 1)
                    else:
                        self.lastPressed[0] = 0
                if not unneeded2bottom and not unneeded2top and not unneeded2all:
                    self.lastPressed[1] = random.randint(-1,1)
            if unneeded1bottom:
                if unneeded2bottom:
                    self.lastPressed[0] = random.randint(-1, 0)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(-1, 0)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2top:
                    self.lastPressed[0] = random.randint(0, 1)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(-1, 0)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2all:
                    self.lastPressed[1] = random.randint(-1, 0)
                    if self.lastPressed[1] == 0:
                        self.lastPressed[0] = random.randint(-1, 1)
                    else:
                        self.lastPressed[0] = 0
                if not unneeded2bottom and not unneeded2top and not unneeded2all:
                    self.lastPressed[1] = -1
            if unneeded1top:
                if unneeded2bottom:
                    self.lastPressed[0] = random.randint(-1, 0)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(0, 1)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2top:
                    self.lastPressed[0] = random.randint(0, 1)
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = random.randint(0, 1)
                    else:
                        self.lastPressed[1] = 0
                if unneeded2all:
                    self.lastPressed[1] = random.randint(0, 1)
                    if self.lastPressed[1] == 0:
                        self.lastPressed[0] = random.randint(-1, 1)
                    else:
                        self.lastPressed[0] = 0
                if not unneeded2bottom and not unneeded2top and not unneeded2all:
                    self.lastPressed[1] = 1
            if not unneeded1bottom and not unneeded1top and not unneeded1all:
                if unneeded2bottom:
                    self.lastPressed[0] = -1
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = 0
                    else:
                        self.lastPressed[1] = 0
                if unneeded2top:
                    self.lastPressed[0] = 1
                    if self.lastPressed[0] == 0:
                        self.lastPressed[1] = 0
                    else:
                        self.lastPressed[1] = 0
                if unneeded2all:
                    self.lastPressed[1] = 0
                    if self.lastPressed[1] == 0:
                        self.lastPressed[0] = random.randint(-1, 1)
                    else:
                        self.lastPressed[0] = 0
                if not unneeded2bottom and not unneeded2top and not unneeded2all:
                    self.lastPressed[1] = 0



            # if not self.aiDying:
            #     if prevPressed != self.lastPressed:
            #         self.lastMovements.append([self.lastPressed[0], self.lastPressed[1]])
            #         if len(self.lastMovements) > 4:
            #             self.lastMovements.pop(0)
            #             if self.lastMovements[0][0] == self.lastMovements[1][0] == self.lastMovements[2][0] == self.lastMovements[3][0]:
            #                 print("ai will die and is making a circle??",self.lastMovements)
            #                 print(self.rect.centerx, self.rect.centery)
            #                 self.aiDying = True
            #                 # bad code :(

            if random.randint(0,10) != 1:
                if [top,bottom,left,right] == self.prevDirs:
                    self.lastPressed[0] = prevPressed[0]
                    self.lastPressed[1] = prevPressed[1]

            if random.randint(0,15) == 1:
                self.game.powerUp.usePowerup(self,self.num)

            if self.lastPressed != [0, 0]:
                # if self.aiDying:
                #     self.lastMovements[3] = [self.lastPressed[0], self.lastPressed[1]]
                #     if self.lastMovements[0][0] == self.lastMovements[1][0] == self.lastMovements[2][0] == self.lastMovements[3][0]:
                #         self.aiDying = True
                #         self.lastPressed = [0, 0]
                #     else:
                #         self.aiDying=False
                #         print("escaped")
                #     if i > 10:
                #         # print(unneeded1top,unneeded1bottom,unneeded1all,unneeded2top,unneeded2bottom,unneeded2all)
                #         break
                self.prevDirs = [top, bottom, left, right]
                break
            else:
                if i > 10:
                    #print(unneeded1top,unneeded1bottom,unneeded1all,unneeded2top,unneeded2bottom,unneeded2all)
                    self.prevDirs = [top, bottom, left, right]
                    break


    def killPlayer(self,both=False):
        self.alive = False
        if both:
            self.game.endGame(self.rect.centerx,self.rect.centery,self.num,True)
        else:
            self.game.endGame(self.rect.centerx,self.rect.centery,self.num)

    def move(self, x, y):
        self.rect.centerx += x * tile_size[0]
        self.rect.centery += y *tile_size[1]

