import math
import random

from pygame.sprite import groupcollide
from scripts.settings import *
from scripts.classes.gui_class import GUI
from scripts.classes.player_class import Player
from scripts.classes.tile_class import Tile, TileMap
from scripts.classes.particle_class import Particle


class Game(object):

  def __init__(self):
    pg.init()
    pg.mixer.init()
    pg.joystick.init()
    self.window = pg.display.set_mode((WIDTH, HEIGHT))
    self.clock = pg.time.Clock()
    self.is_playing = True
    self.buttons = pg.sprite.Group()
    self.players = pg.sprite.Group()
    self.all_sprites = pg.sprite.Group()
    self.wall_sprites = pg.sprite.Group()
    self.goal_sprites = pg.sprite.Group()
    self.kill_sprites = pg.sprite.Group()
    self.particle_sprites = pg.sprite.Group()
    self.bean_sprites = pg.sprite.Group()
    self.surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

    #define start bg images
    self.startBG = pg.image.load("scripts/assets/startbg/bg.jpg")
    self.startBG = pg.transform.scale(self.startBG, (612*2,HEIGHT))  # delete if needed
    self.startBGT = self.startBG.copy()
    self.startBGMove = 0
    self.startPlayer =  pg.image.load("scripts/assets/player/midair.png")
    self.startPlayer = pg.transform.scale(self.startPlayer, [tileSize,tileSize])  # delete if needed
    self.startPlayer = pg.transform.rotate(self.startPlayer,270)
    self.startPlayerT=self.startPlayer.copy()
    self.startPlayerFall = pg.image.load("scripts/assets/player/death.png")
    self.startPlayerFall = pg.transform.scale(self.startPlayerFall, [tileSize,tileSize])  # delete if needed
    self.startPlayerFallT = self.startPlayerFall.copy()
    self.startLightning = pg.image.load("scripts/assets/startbg/lightning.png")
    self.startLightning = pg.transform.scale(self.startLightning,(44*2,6*tileSize)) # delete if needed
    self.startPlayerElectrocuted = pg.image.load("scripts/assets/player/electrocuted.png")
    self.startPlayerElectrocuted = pg.transform.scale(self.startPlayerElectrocuted,[tileSize,tileSize])
    self.startPlayerPos = [WIDTH/2,6*tileSize]
    self.startPlayerVel = [3,0]
    self.startPlayerRot = random.randint(0,360)
    self.startPlayerElectrocuted = pg.transform.rotate(self.startPlayerElectrocuted, self.startPlayerRot)
    self.startPlayerFalling = 0

    # define bg images
    self.topGUI = pg.image.load("scripts/assets/placeHolder.jpg")
    self.topGUI = pg.transform.scale(self.topGUI,(WIDTH,int(HEIGHT/10))) #delete if needed
    self.fartGUI = pg.image.load("scripts/assets/ui/fart.png")
    self.fartGUI = pg.transform.scale(self.fartGUI,(tileSize,tileSize)) #delete if needed
    self.skullGui = pg.image.load("scripts/assets/ui/skull.png")
    self.skullGui = pg.transform.scale(self.skullGui,(tileSize,tileSize)) #delete if needed
    self.bg = pg.image.load("scripts/assets/bg.jpg")
    self.bg = pg.transform.scale(self.bg,(WIDTH,HEIGHT))

    pg.display.set_caption("Farty Mc-Fly")
    image = pg.image.load("scripts/assets/logo.png")
    pg.display.set_icon(image)

    self.level = 1
    self.deaths = 0
    self.deathCircle = 2400
    self.particleTime=0
    self.won=False
    self.alive = True
    self.startScreen=True
    self.endScreen = False
    self.endReady = False

    #achievment vars
    self.beansCollected=0 #ready
    #deaths
    self.totalFarts = 0 #ready
    self.totalTime = 0 #ready
    self.closeCalls = 0 #ready


    self.map = TileMap(levels[self.level-1][0])
    playerx, playery = self.map.start_x, self.map.start_y

    self.player = Player(playerx, playery, self)
    self.players.add(self.player)
    self.all_sprites.add(self.players)

    self.defineTiles()

    pg.mixer.music.load("scripts/assets/sounds/Jazz.mp3")
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(-1)

  def endLevel(self):
    if len(levels)>self.level:
      self.level+=1
      self.alive=False
      self.won=True
    else:
      self.endScreen = True
      self.alive = False



  def restartLevel(self):
    self.alive = False
    self.deaths+=1
    self.won=False

  def killBean(self,bean):
    bean.kill()

  def defineTiles(self):
    for tile in self.map.tiles:
      if tile.type == "wall":
        self.wall_sprites.add(tile)
      elif tile.type == "goal":
        self.goal_sprites.add(tile)
      elif tile.type =="kill":
        self.kill_sprites.add(tile)
        self.wall_sprites.add(tile) # so player can bounce on kill objects still lol
      elif tile.type =="beans":
        self.bean_sprites.add(tile)

  def update(self):
    if not self.startScreen:
      try:
        self.totalTime += 1 / self.clock.get_fps()
      except:
        pass
      if self.alive:
        self.all_sprites.update()
        if self.deathCircle<2400:
          self.deathCircle+=10
      else:
        if self.deathCircle>1300:
          self.deathCircle-=10
          if random.randint(0,8)==0:
            if self.won:
              self.spawnParticle(random.choice(happyParticles), "start", random.randint(0, 1))
            else:
              self.spawnParticle(random.choice(sadParticles), "start", random.randint(0, 1))
        else:
          if self.endScreen:
            self.alive=True
            try:
              for tile in self.map.tiles:
                tile.kill()
              self.map.kill()
              self.player.kill()
              self.startPlayer = pg.transform.scale(self.startPlayer, [tileSize, tileSize])  # delete if needed
              self.startPlayer = pg.transform.rotate(self.startPlayer, 0)
              self.startPlayerPos = [WIDTH / 2, 6 * tileSize]
              self.startPlayerVel = [3, 0]
              self.startPlayerRot = random.randint(0, 360)
              self.startPlayerElectrocuted = pg.transform.rotate(self.startPlayerElectrocuted, self.startPlayerRot)
              self.startPlayerFalling = 0
              self.startScreen=True
            except:
              pass
          else:
            self.alive=True
            for tile in self.map.tiles:
              tile.kill()
            self.map = TileMap(levels[self.level-1][0])
            playerx, playery = self.map.start_x, self.map.start_y
            try:
              self.player.kill()
            except:
              pass
            self.player = Player(playerx, playery, self)
            self.players.add(self.player)
            self.all_sprites.add(self.players)
            self.defineTiles()
    else:
      self.particle_sprites.update()
      if not self.alive:
        if self.deathCircle > 1200:
          self.deathCircle -= 10
        else:
          self.alive=True
          self.startScreen=False
          if self.endScreen:
            self.level = 1
            self.deaths = 0
            self.particleTime = 0
            self.won = False
            self.alive = True
            self.startScreen = False
            self.endScreen = False
            self.endReady = False

            self.map = TileMap(levels[self.level - 1][0])
            playerx, playery = self.map.start_x, self.map.start_y

            self.player = Player(playerx, playery, self)
            self.players.add(self.player)
            self.all_sprites.add(self.players)
            self.defineTiles()
      if not self.endReady and self.endScreen:
        if self.deathCircle < 2400:
          self.deathCircle += 10
        else:
          self.endReady=True

    # self.mouseOverlap()
    # self.sillyEvent()

  def draw(self):
    self.window.fill(WHITE)
    self.surface.fill(TRANSPARENT)
    if self.startScreen:
      if random.randint(0,6)==0:
        self.spawnParticle(random.choice(happyParticles),"start",random.randint(0,1))

      self.startBGMove-=2
      self.window.blit(self.startBG,(self.startBGMove,0))
      self.window.blit(self.startBGT,(self.startBGMove+self.startBG.get_width(),0))
      if abs(self.startBGMove)>=self.startBG.get_width():
        self.startBGMove=0

      if self.startPlayerFalling==0:
        if random.randint(0,240)==1:
          self.startPlayerVel[0]*=-1
          self.spawnParticle("scripts/assets/particles/fart.png", "startFart", 0)
        self.startPlayerPos[0] += self.startPlayerVel[0]
        if self.startPlayerPos[0]+self.startPlayer.get_width()>WIDTH-5*tileSize:
          self.startPlayerVel[0] = - abs(self.startPlayerVel[0])
          self.spawnParticle("scripts/assets/particles/fart.png", "startFart", 0)
        if self.startPlayerPos[0]<5*tileSize:
          self.startPlayerVel[0] = abs(self.startPlayerVel[0])
          self.spawnParticle("scripts/assets/particles/fart.png", "startFart", 0)

        if self.startPlayerVel[0]<0:
          self.startPlayer = pg.transform.flip(self.startPlayerT, True, False)
        else:
          self.startPlayer = pg.transform.flip(self.startPlayerT, False, False)

        if pg.mouse.get_pressed()[0]:
          self.startPlayerFalling=1
          self.startPlayerDif = [WIDTH/2-self.startPlayerPos[0],HEIGHT-self.startPlayerPos[1]]

        self.window.blit(self.startPlayer, self.startPlayerPos)
      else:
        if self.startPlayerFalling<45:
          if self.startPlayerFalling<2:
            pg.mixer.Channel(0).play(pg.mixer.Sound('scripts/assets/sounds/lightning.mp3'))
          self.startPlayerVel= [0,0]
          self.window.blit(self.startPlayerElectrocuted, self.startPlayerPos)
          pg.draw.rect(self.surface,BLACK1,pg.Rect(0,0,WIDTH,HEIGHT))
          self.window.blit(self.startLightning, (self.startPlayerPos[0]-self.startPlayer.get_width(), 0))
          self.startPlayerPos[1]=int(5.5*tileSize)
        else:
          self.startPlayerDif[1] = (self.startPlayerFalling-45) * 0.2
          self.startPlayerDif[0] = self.startPlayerDif[0]
          if self.startPlayerPos[1]-self.startPlayer.get_height()*2>HEIGHT:
            self.alive=False
            self.startPlayerFalling=46
            self.startPlayerDif[0] = 0
          self.startPlayerPos[0] += self.startPlayerDif[0] / 120
          self.startPlayerPos[1] += (self.startPlayerFalling - 45) * 0.2
          self.startPlayerFall = pg.transform.rotate(self.startPlayerFallT,self.startPlayerRot)
          if self.startPlayerDif[0]>1:
            self.startPlayerRot-=2
          else:
            self.startPlayerRot += 2


          self.window.blit(self.startPlayerFall, self.startPlayerPos)

        self.startPlayerFalling+=1
      self.particle_sprites.draw(self.window)
      if self.endScreen:
        draw_text_center(self.window, "FARTY   MC-FLY", 60, WHITE, WIDTH / 2, 1 * tileSize,
                         "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        draw_text_center(self.window, "thank you for playing!", 35, WHITE, WIDTH / 2, int(2.5 * tileSize),
                         "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        # stats
        # draw_text(self.window, "you farted a total of  "+str(self.totalFarts)+"  times", 35, WHITE, tileSize/2, 10*tileSize,
        #                  "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        # draw_text(self.window, "you collected  " + str(self.beansCollected)+"  beans", 35, WHITE, tileSize/2, (10+1.5) * tileSize,
        #                "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        # draw_text(self.window, "you spent a total of  " + str(int(((self.totalTime)/60)*1000)/1000)+"  minutes", 35, WHITE, tileSize/2,
        #                (10 + 3) * tileSize,"scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        # draw_text(self.window, "you had a total of  " + str(self.closeCalls)+"  close calls", 35, WHITE, tileSize/2,
        #                (10 + 4.5) * tileSize, "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
      else:
        draw_text_center(self.window, "FARTY   MC-FLY", 60, WHITE, WIDTH/2, 1*tileSize,"scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
        draw_text_center(self.window, "click   anywhere   to   begin!", 35, WHITE, WIDTH/2, int(2.5*tileSize),"scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
      pg.draw.circle(self.surface, BLACK, self.startPlayerPos, self.deathCircle,math.ceil(WIDTH * 2))  # death circle
    else:
      self.window.blit(self.bg, (0, 0))
      self.map.draw_map(self.window)
      self.all_sprites.draw(self.window)
      self.drawCircle()

      self.window.blit(self.fartGUI, (15, 15))
      draw_text(self.window,str(self.player.farts),40,WHITE,25+self.fartGUI.get_width(),15)
      self.window.blit(self.skullGui, (WIDTH-15-self.skullGui.get_width(), 15))
      draw_text_right(self.window, str(self.deaths), 40, WHITE, WIDTH-self.skullGui.get_width()-25, 15)

      draw_text_center(self.window, "Level: "+str(self.level), 50, WHITE, WIDTH/2, 15)

      pg.draw.circle(self.surface, BLACK, self.player.rect.center, self.deathCircle,math.ceil(WIDTH * 2))  # death circle
    self.window.blit(self.surface,(0,0))

    pg.display.flip()

  def drawCircle(self):
    if self.player.mouseButtonDown:
      var1 = math.sqrt((self.player.dif[0]) ** 2 + (self.player.dif[1]) ** 2)
      if var1 >= 5 * tileSize:
        var1 = 5 * tileSize
      pg.draw.circle(self.surface, WHITE, (self.player.orgPos), var1, 2)  # get rid of width and change color
      circles = 0
      for i in range(0, int(var1)):
        if i % 20 == 0:
          circles += 1
      for i in range(0, circles):
        var = 10 * i / 10 + 2
        self.player.temp1 = 1
        if var > 20:
          var = 20
        if var1 >= 5 * tileSize:
          while math.sqrt((self.player.dif[0] * self.player.temp1) ** 2 + (self.player.dif[1] * self.player.temp1) ** 2) >= 5 * tileSize:
            self.player.temp1 *= 0.98
        pg.draw.circle(self.surface, WHITE, ((self.player.orgPos[0] - self.player.dif[0] / circles * i * self.player.temp1),
                                             (self.player.orgPos[1] - self.player.dif[1] / circles * i * self.player.temp1)), var)
        pg.draw.circle(self.surface, GREY1,((self.player.rect.center[0] + self.player.dif[0] / circles * abs(i-circles) * self.player.temp1*0.5),
                        (self.player.rect.center[1] + self.player.dif[1] / circles * abs(i-circles) * self.player.temp1*0.5)), var/2)

  def spawnParticle(self, type, location, amount, game=False, x=0, y=0 ,flipped=False,moveVec = []):
    if location == "start":
      x = random.randint(0, WIDTH)
      y = HEIGHT+tileSize
      particle = Particle(type, x, y, amount, game, 3, True)
    elif location == "startFart":
      if self.startPlayerVel[0] <0:
        flipped =True
      else:
        flipped=False
      particle = Particle(type, self.startPlayerPos[0], self.startPlayerPos[1]+self.startPlayer.get_height()/2, amount, game, 3, True,flipped)
    else:
      if amount > 0:
        particle = Particle(type, x, y, amount, self, 3,False,flipped)
      else:
        particle = Particle(type, x, y, amount, False, 3,False,flipped)
    self.particle_sprites.add(particle)
    self.all_sprites.add(particle)

  def play(self):
    while self.is_playing:
      self.clock.tick(FPS)
      self.get_game_events()
      self.update()
      self.draw()


  def mouseOverlap(self, source):
    for button in source:
      self.mouse_pos = pg.mouse.get_pos()
      self.mouse_bttns = pg.mouse.get_pressed()
      x = False
      y = False
      if self.mouse_pos[0] < button.xpos + button.width / 2 and self.mouse_pos[0] > button.xpos - button.width / 2:
        x = True
      if self.mouse_pos[1] < button.ypos + button.height / 2 and self.mouse_pos[1] > button.ypos - button.height / 2:
        y = True

      if x and y == True:
        print("mouse overlap")

  def get_game_events(self):
    events = pg.event.get()
    for event in events:
      if event.type == pg.QUIT:
        self.is_playing = False

  def end_screen(self):
    return "quit"