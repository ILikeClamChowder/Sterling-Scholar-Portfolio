from scripts.settings import *


class Player(pg.sprite.Sprite):

  def __init__(self, x, y, game):
    super(Player, self).__init__()
    self.image = pg.image.load("scripts/assets/player/idle1.png")
    self.image = pg.transform.scale(self.image,(tileSize,tileSize))
    self.imageT = self.image.copy()

    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    # print(self.rect.center)
    self.rotAmount = 0
    self.moveVec = [1, 1]
    self.speedx = 0
    self.speedy = 0
    self.gravity = 0.3
    self.moveDirY = 0
    self.gravTicks = 0
    self.groundedF = False
    self.groundedC = False
    self.game = game
    self.idleNum = 1
    self.idleActive = True
    self.temp3=0

    self.mouseButtonDown = False
    self.orgPos = [0, 0]
    self.curPos = [0, 0]
    self.dif = [0, 0]

    self.temp1 =1
    self.temp2 = 0
    self.farts = levels[self.game.level-1][1] # brother LMAOOOO
    self.dying=False

  def update(self):
    if self.moveVec[0] ==0 and self.moveVec[1]==0:
      self.idleActive=True
      self.rotAmount=0
    else:
      self.idleActive=False
    if self.idleActive:
      if self.temp3>35:
        self.temp3=0
        if self.idleNum==1:
          self.imageT = pg.image.load("scripts/assets/player/idle1.png")
          self.imageT = pg.transform.scale(self.imageT, (tileSize, tileSize))
          self.idleNum=2
        else:
          self.imageT = pg.image.load("scripts/assets/player/idle2.png")
          self.imageT = pg.transform.scale(self.imageT, (tileSize, tileSize))
          self.idleNum=1
      self.temp3+=1
    if self.dying:
      if self.moveVec[0]==0 and self.moveVec[1]==0:
        self.game.restartLevel()
    if self.farts <=0:
      self.dying=True
    self.move()
    # checks wall and death collisions
    self.gravityMove()
    self.check_coll("z")
    self.checkGoalCollision()
    self.checkMapBounds()

    if self.dying:
      self.imageT = pg.image.load("scripts/assets/player/death.png")
      self.imageT = pg.transform.scale(self.imageT, (tileSize, tileSize))

    self.image = pg.transform.rotate(self.imageT,self.rotAmount)

  def move(self):
    # keys = pg.key.get_pressed()
    mouse = pg.mouse.get_pos()
    mouseButtons = pg.mouse.get_pressed()


    if mouseButtons[0]:
      if not self.dying:
        if self.mouseButtonDown:
          self.imageT = pg.image.load("scripts/assets/player/midfart.png")
          self.imageT = pg.transform.scale(self.imageT, (tileSize, tileSize))
          self.curPos = mouse
          self.dif = [
              self.orgPos[0] - self.curPos[0], self.orgPos[1] - self.curPos[1]
          ]
        else:
          self.mouseButtonDown = True
          self.orgPos = mouse
        self.temp2=0
    else:

      if self.mouseButtonDown:
        if (self.gravity > 0 and self.groundedF) or (self.gravity < 0 and self.groundedC):
          pg.mixer.Channel(2).play(pg.mixer.Sound(random.choice(fartSounds)))
          self.mouseButtonDown = False
          if self.moveVec[0]>0:
            flipped=True
          else:
            flipped=False
          self.game.spawnParticle("scripts/assets/particles/fart.png", "", 0,False,self.rect.centerx,self.rect.centery,flipped,[-self.moveVec[0] * self.speedx,-self.moveVec[1] * self.speedy])
          self.temp2=0
          self.farts-=1
          self.game.totalFarts+=1
          self.imageT = pg.image.load("scripts/assets/player/midair.png")
          self.imageT = pg.transform.scale(self.imageT, (tileSize, tileSize))
          # set moveVecs and speed
          # set drag amount
          if self.dif[0]==0:
            self.dif[0] = 0.1
          if self.dif[1]==0:
            self.dif[1]=0.1
          self.moveVec = [
              self.dif[0] / abs(self.dif[0]), self.dif[1] / abs(self.dif[1])
          ]
          if abs(self.dif[0]) > abs(self.dif[1]):
            self.dif[1] *= 1/self.dif[0] *self.dif[1]/abs(self.dif[1])
            self.dif[0]=1 *self.dif[0]/abs(self.dif[0])
          else:
            self.dif[0] *= 1/self.dif[1] *self.dif[0]/abs(self.dif[0])
            self.dif[1]=1 *self.dif[1]/abs(self.dif[1])
          self.speedx = abs(self.dif[0]) *(abs(abs((self.curPos[0])-abs(self.orgPos[0]))*self.temp1))*0.1
          self.speedy = abs(self.dif[1]) *(abs(abs((self.curPos[1])-abs(self.orgPos[1]))*self.temp1))*0.1

        else:
          self.temp2+=1
          if self.temp2>=20:
            self.mouseButtonDown=False

    if abs(self.moveVec[0]) > 0:
      self.speedx *= 0.99  # slow down by drag amount
      if abs(self.speedx) < 0.1:
        self.moveVec[0] = 0
        self.speedx = 0
    if abs(self.moveVec[1]) > 0:
      self.speedy *= 0.99  # slow down by drag amount
      if abs(self.speedy) < 0.20:
        self.moveVec[1] = 0
        self.speedy = 0
    self.rotAmount+= self.speedx/5 +self.speedy/5

    self.rect.centerx += self.moveVec[0] * self.speedx
    self.checkKillCollision()
    self.check_coll("x")
    self.rect.centery += self.moveVec[1] * self.speedy
    self.checkKillCollision()
    self.check_coll("y")
    self.checkBeansCollision()

    # WASD movement
    # if dir == "x":
    #   if keys[pg.K_d]:
    #     self.moveVec[0] = 1
    #   elif keys[pg.K_a]:
    #     self.moveVec[0] = -1
    #   else:
    #     self.moveVec[0] = 0
    #   self.rect.centerx += self.moveVec[0] * self.speed
    # else:
    #   if keys[pg.K_w]:
    #     self.moveVec[1] = -2
    #   elif keys[pg.K_s]:
    #     self.moveVec[1] = 1
    #   # else:
    #   #   self.moveVec[1] = 0
    #   self.rect.centery += self.moveVec[1] * self.speed

  def gravityMove(self):
    if self.groundedC:
      if self.gravity > 0 or abs(self.moveVec[1])>0.2:
        self.gravTicks += 1
        self.moveDirY = self.gravTicks * self.gravity
        self.rect.centery += self.moveDirY
        self.moveVec[1]= -self.moveVec[1]
      else:
        self.gravTicks = 0
    elif self.groundedF:
      if self.gravity < 0 or abs(self.moveVec[1])>0.2:
        self.gravTicks += 1
        self.moveDirY = self.gravTicks * self.gravity
        self.rect.centery += self.moveDirY
        self.moveVec[1] = -self.moveVec[1]
      else:
        self.gravTicks = 0
    else:
      self.gravTicks += 1
      self.moveDirY = self.gravTicks * self.gravity
      self.rect.centery += self.moveDirY


  def check_coll(self, dir):
    hits = pg.sprite.spritecollide(self, self.game.wall_sprites, False)
    if hits:
      if dir == "x":
        pg.mixer.Channel(3).play(pg.mixer.Sound(random.choice(wallSounds)))
        if self.moveVec[0] > 0:
          self.rect.right = hits[0].rect.left
          self.moveVec[0] = -self.moveVec[0]
        elif self.moveVec[0] < 0:
          self.rect.left = hits[0].rect.right
          self.moveVec[0] = -self.moveVec[0]
      elif dir == "y":
        pg.mixer.Channel(3).play(pg.mixer.Sound(random.choice(wallSounds)))
        if self.moveVec[1] > 0:
          self.gravTicks = 0
          self.groundedF = True
          self.groundedC = False
          self.rect.bottom = hits[0].rect.top
          return
        elif self.moveVec[1] < 0:
          self.gravTicks = 0
          self.groundedC = True
          self.groundedF = False
          self.rect.top = hits[0].rect.bottom
          return
        else:
          self.groundedC = False
          self.groundedF = False
          return
      else:
        if self.gravity > 0:
          self.groundedF = True
          self.groundedC = False
          self.gravTicks = 0
          self.rect.bottom = hits[0].rect.top
        elif self.gravity < 0:
          self.rect.top = hits[0].rect.bottom
          self.groundedC = True
          self.groundedF = False
          self.gravTicks = 0
        else:
          self.groundedC = False
          self.groundedF = False
    else:
      if dir == "y":
        self.groundedC = False
        self.groundedF = False

  def checkGoalCollision(self):
    hits = pg.sprite.spritecollide(self, self.game.goal_sprites, False)
    if hits:
      if self.farts<=0:
        self.game.closeCalls+=1
      self.game.endLevel()
      self.moveVec = [0, 0]
      self.alive = True

  def checkKillCollision(self):
    hits = pg.sprite.spritecollide(self, self.game.kill_sprites, False)
    if hits:
      self.dying=True

  def checkBeansCollision(self):
    hits = pg.sprite.spritecollideany(self, self.game.bean_sprites)
    if hits!= None:
      pg.mixer.Channel(2).play(pg.mixer.Sound('scripts/assets/sounds/beans.mp3'))
      self.game.killBean(hits)
      hits.killed=True
      self.game.map.map_surface = pg.Surface((self.game.map.map_w, self.game.map.map_h))
      self.game.map.map_surface.set_colorkey((0, 0, 0))
      self.game.map.load_map()
      self.game.beansCollected+=1
      if self.farts<=0:
        self.game.closeCalls+=1
      self.farts+=1
      self.dying = False


  def checkMapBounds(self):
    if self.rect.left>WIDTH or self.rect.right<0 or self.rect.top>HEIGHT or self.rect.bottom<0:
      if self.farts<=0:
        self.game.closeCalls+=1
      self.game.endLevel()
      self.moveVec = [0,0]
      self.alive=True
