import random

from scripts.settings import *
from scripts.classes.player_class import Player
from scripts.classes.gui_class import GUI
from scripts.classes.particle_class import Particle
from scripts.classes.object_class import Object
from scripts.classes.hand_class import Hand


class Game(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.main_sprites = pg.sprite.Group()
        self.object_sprites = pg.sprite.Group()
        self.particle_sprites = pg.sprite.Group()
        self.player_sprites = pg.sprite.Group()

        # loading bg assets
        self.bg = pg.image.load("scripts/assets/background/sky3.jpg").convert()
        self.bg = pg.transform.scale(self.bg, (1280*tile_size,148*tile_size))
        self.waves = pg.image.load("scripts/assets/background/waves2.png").convert_alpha()
        self.waves = pg.transform.scale(self.waves, (640 * tile_size, 20 * tile_size))
        self.water = pg.image.load("scripts/assets/background/water.png").convert_alpha()
        self.water = pg.transform.scale(self.water, (320 * tile_size, 360 * tile_size))
        self.playerImageBg = pg.image.load("scripts/assets/background/playerBg.png").convert_alpha()
        self.playerImageBg = pg.transform.scale(self.playerImageBg, (32 * tile_size, 16 * tile_size))
        self.playerImageBgRect = self.playerImageBg.get_rect()
        self.playerImageBgT = self.playerImageBg.copy()
        self.bgMove1 = tile_size*random.randint(0,int(self.bg.get_width()/4))
        self.bgMove2 = 0
        self.bgMove3 = 0
        self.bgMove31 = 0
        self.bgMove3F = True
        self.bgMove3R = 0
        self.bgParticleSpawned = False

        # loading ui assets
        self.topGUI = pg.image.load("scripts/assets/ui/topgui3.png").convert_alpha()
        self.topGUI = pg.transform.scale(self.topGUI, (self.topGUI.get_width() * tile_size, self.topGUI.get_height() * tile_size))
        self.oxygenTank = pg.image.load("scripts/assets/ui/oxygentank.png").convert_alpha()
        self.oxygenTank = pg.transform.scale(self.oxygenTank,(self.oxygenTank.get_width() * (tile_size-1), self.oxygenTank.get_height() * (tile_size-1)))
        self.oxygenTank = pg.transform.rotate(self.oxygenTank,45)
        self.oxygenTankEmpty = pg.image.load("scripts/assets/ui/oxygentankempty.png").convert_alpha()
        self.oxygenTankEmpty = pg.image.load("scripts/assets/ui/oxygentankempty.png").convert_alpha()
        self.oxygenTankEmpty = pg.transform.scale(self.oxygenTankEmpty, (self.oxygenTankEmpty.get_width() * (tile_size-1), self.oxygenTankEmpty.get_height() * (tile_size-1)))
        self.oxygenTankEmpty = pg.transform.rotate(self.oxygenTankEmpty, 45)

        # powerups assets
        self.tempPowerUp = pg.image.load("scripts/assets/powerups/strength1.jpg").convert()
        self.tempPowerUp = pg.transform.scale(self.tempPowerUp,(self.tempPowerUp.get_width() * tile_size, self.tempPowerUp.get_height() * tile_size))
        self.explodePowerUp = pg.image.load("scripts/assets/powerups/explode.png").convert_alpha()
        self.explodePowerUp = pg.transform.scale(self.explodePowerUp, (
        self.explodePowerUp.get_width() * tile_size, self.explodePowerUp.get_height() * tile_size))
        self.heal1PowerUp = pg.image.load("scripts/assets/powerups/heal1.png").convert_alpha()
        self.heal1PowerUp = pg.transform.scale(self.heal1PowerUp, (
        self.heal1PowerUp.get_width() * tile_size, self.heal1PowerUp.get_height() * tile_size))
        self.heal2PowerUp = pg.image.load("scripts/assets/powerups/heal2.png").convert_alpha()
        self.heal2PowerUp = pg.transform.scale(self.heal2PowerUp, (
            self.heal2PowerUp.get_width() * tile_size, self.heal2PowerUp.get_height() * tile_size))
        self.heal3PowerUp = pg.image.load("scripts/assets/powerups/heal3.png").convert_alpha()
        self.heal3PowerUp = pg.transform.scale(self.heal3PowerUp, (
            self.heal3PowerUp.get_width() * tile_size, self.heal3PowerUp.get_height() * tile_size))
        self.speed1PowerUp = pg.image.load("scripts/assets/powerups/speed1.png").convert_alpha()
        self.speed1PowerUp = pg.transform.scale(self.speed1PowerUp, (
            self.speed1PowerUp.get_width() * tile_size, self.speed1PowerUp.get_height() * tile_size))
        self.speed2PowerUp = pg.image.load("scripts/assets/powerups/speed2.png").convert_alpha()
        self.speed2PowerUp = pg.transform.scale(self.speed2PowerUp, (
            self.speed2PowerUp.get_width() * tile_size, self.speed2PowerUp.get_height() * tile_size))
        self.speed3PowerUp = pg.image.load("scripts/assets/powerups/speed3.png").convert_alpha()
        self.speed3PowerUp = pg.transform.scale(self.speed3PowerUp, (
            self.speed3PowerUp.get_width() * tile_size, self.speed3PowerUp.get_height() * tile_size))
        self.strength1PowerUp = pg.image.load("scripts/assets/powerups/strength1.png").convert_alpha()
        self.strength1PowerUp = pg.transform.scale(self.strength1PowerUp, (
            self.strength1PowerUp.get_width() * tile_size, self.strength1PowerUp.get_height() * tile_size))
        self.strength2PowerUp = pg.image.load("scripts/assets/powerups/strength2.png").convert_alpha()
        self.strength2PowerUp = pg.transform.scale(self.strength2PowerUp, (
            self.strength2PowerUp.get_width() * tile_size, self.strength2PowerUp.get_height() * tile_size))
        self.strength3PowerUp = pg.image.load("scripts/assets/powerups/strength3.png").convert_alpha()
        self.strength3PowerUp = pg.transform.scale(self.strength3PowerUp, (
            self.strength3PowerUp.get_width() * tile_size, self.strength3PowerUp.get_height() * tile_size))


        self.is_playing = True

        self.startscreenOpen = True
        self.startScreenAnim = False
        self.startScreenBg()


        self.curWaterColor = (81, 160, 200)
        self.gameSpeed = 100
        self.depth = 0

        # real level is what level is being called from settings, display level is what level the game displays
        self.realLevel = 30
        self.displayLevel = 1
        self.displayScore = 0
        self.realScore = 0
        self.highScore = 0

        self.waveCoolDown = 180 # 3 second wave cool down
        self.temp2 = 0
        self.waveSpawned = 0
        self.mainObjectNum = 0
        self.mainObjectsFinished = False
        self.lives = 4
        self.powerUps = []

        self.startTime = 0

        # get player data
        fileRead = open("scripts/playerData.txt", "r")
        for line in fileRead.readlines():
            print(line)
            try:
                self.highScore = int(line)
            except:
                pass
        fileRead.close()

        pg.mixer.init()
        pg.mixer.music.load("scripts/assets/sounds/Fluffing-a-Duck.mp3")
        pg.mixer.music.set_volume(0.4)
        pg.mixer.music.play(-1)
        pg.display.set_caption("Slap-Marine")
        image = pg.image.load("scripts/assets/playerIcon.png").convert_alpha()
        pg.display.set_icon(image)


    def prepGame(self):
        self.bg = pg.Surface((WIDTH, HEIGHT))
        self.bg.fill(self.curWaterColor)
        self.bg2 = pg.Surface((WIDTH, HEIGHT))
        self.bg2.fill((self.curWaterColor[0] - 6, self.curWaterColor[1] - 6, self.curWaterColor[2] - 6))
        self.player = Player(WIDTH / 2, HEIGHT / 2, self)
        self.player_sprites.add(self.player)
        self.hand = Hand(self)
        self.player_sprites.add(self.hand)


        self.gameBgMove1 = 0

    def endGame(self):
        for object in self.object_sprites:
            object.kill()
        for thing in self.main_sprites:
            thing.kill()
        for thing in self.player_sprites:
            thing.kill()
        for thing in self.particle_sprites:
            thing.kill()
        for thing in self.all_sprites:
            thing.kill()
        # loading bg assets
        self.bg = pg.image.load("scripts/assets/background/sky3.jpg").convert()
        self.bg = pg.transform.scale(self.bg, (1280 * tile_size, 148 * tile_size))
        self.waves = pg.image.load("scripts/assets/background/waves2.png").convert_alpha()
        self.waves = pg.transform.scale(self.waves, (640 * tile_size, 20 * tile_size))
        self.water = pg.image.load("scripts/assets/background/water.png").convert_alpha()
        self.water = pg.transform.scale(self.water, (320 * tile_size, 360 * tile_size))
        self.playerImageBg = pg.image.load("scripts/assets/background/playerBg.png").convert_alpha()
        self.playerImageBg = pg.transform.scale(self.playerImageBg, (32 * tile_size, 16 * tile_size))
        self.playerImageBgRect = self.playerImageBg.get_rect()
        self.playerImageBgT = self.playerImageBg.copy()
        self.bgMove1 = tile_size * random.randint(0, int(self.bg.get_width() / 4))
        self.bgMove2 = 0
        self.bgMove3 = 0
        self.bgMove31 = 0
        self.bgMove3F = True
        self.bgMove3R = 0
        self.bgParticleSpawned = False

        # loading ui assets
        self.topGUI = pg.image.load("scripts/assets/ui/topgui3.png").convert_alpha()
        self.topGUI = pg.transform.scale(self.topGUI, (
        self.topGUI.get_width() * tile_size, self.topGUI.get_height() * tile_size))
        self.oxygenTank = pg.image.load("scripts/assets/ui/oxygentank.png").convert_alpha()
        self.oxygenTank = pg.transform.scale(self.oxygenTank, (
        self.oxygenTank.get_width() * (tile_size - 1), self.oxygenTank.get_height() * (tile_size - 1)))
        self.oxygenTank = pg.transform.rotate(self.oxygenTank, 45)
        self.oxygenTankEmpty = pg.image.load("scripts/assets/ui/oxygentankempty.png").convert_alpha()
        self.oxygenTankEmpty = pg.image.load("scripts/assets/ui/oxygentankempty.png").convert_alpha()
        self.oxygenTankEmpty = pg.transform.scale(self.oxygenTankEmpty, (
        self.oxygenTankEmpty.get_width() * (tile_size - 1), self.oxygenTankEmpty.get_height() * (tile_size - 1)))
        self.oxygenTankEmpty = pg.transform.rotate(self.oxygenTankEmpty, 45)

        self.startscreenOpen = True
        self.startScreenAnim = False
        self.startScreenBg()

        self.curWaterColor = (81, 160, 200)
        self.gameSpeed = 100
        self.depth = 0

        # real level is what level is being called from settings, display level is what level the game displays
        self.realLevel = 0
        self.displayLevel = 1
        self.displayScore = 0
        self.realScore = 0
        self.highScore = 0

        self.waveCoolDown = 180  # 3 second wave cool down
        self.temp2 = 0
        self.waveSpawned = 0
        self.mainObjectNum = 0
        self.mainObjectsFinished = False
        self.lives = 4
        self.powerUps = []
        self.startTime = 0

        # get player data
        fileRead = open("scripts/playerData.txt", "r")
        for line in fileRead.readlines():
            print(line)
            try:
                self.highScore = int(line)
            except:
                pass
        fileRead.close()

    def spawnParticle(self, type,location,amount,game = False,x=0,y=0):
        if location=="start":
            x = WIDTH / 2 - self.playerImageBg.get_width() / 2 + int(self.bgMove3)
            y = 155 * tile_size + self.bgMove31
            particle = Particle(type,x,y,amount,game,3,True)
            self.all_sprites.add(particle)
        else:
            if amount>0:
                particle = Particle(type, x, y, amount, self, 3)
            else:
                particle = Particle(type, x, y, amount, False, 3)
            self.particle_sprites.add(particle)




    def spawnObject(self):
        if random.randint(levelInfo[self.realLevel][3][0],levelInfo[self.realLevel][3][1])==levelInfo[self.realLevel][3][1]:
            if len(levelInfo[self.realLevel][0]) == 0:
                self.mainObjectsFinished = True
            if self.mainObjectsFinished:
                object = Object(random.choice(levelInfo[self.realLevel][1])[0], 4*random.randint(0,tile_count[0]), HEIGHT, self)
                self.main_sprites.add(object)
                self.object_sprites.add(object)
            else:
                object = Object(levelInfo[self.realLevel][0][self.mainObjectNum][0], 4*random.randint(0,tile_count[0]), HEIGHT, self)
                self.mainObjectNum += 1
                self.main_sprites.add(object)
                self.object_sprites.add(object)
                if self.mainObjectNum >= len(levelInfo[self.realLevel][0]):
                    self.mainObjectsFinished = True

            self.waveSpawned +=1
            if self.waveSpawned>=levelInfo[self.realLevel][2]:
                # move to next level if wave num spawned
                self.realLevel +=1
                self.displayLevel+=1
                self.realScore+=self.realLevel*200
                self.mainObjectsFinished = False
                self.mainObjectNum = 0
                self.waveSpawned = 0
                self.temp2 = 1

                if self.realLevel >= len(levelInfo):
                    self.realLevel=len(levelInfo)-1
                
                self.saveData()
    def update(self):
        pg.display.set_caption(str(self.clock.get_fps()))

        self.displayScore+=(self.realScore-self.displayScore)/20
        if self.startscreenOpen:
            self.particle_sprites.update(self.clock.tick(FPS))
            self.all_sprites.update(self.clock.tick(FPS))
        else:
            self.particle_sprites.update(self.clock.tick(FPS))
            self.main_sprites.update(self.clock.tick(FPS))
            self.player_sprites.update(self.clock.tick(FPS))
            if self.temp2 >0:
                self.temp2+=1
                self.gameBgMove1 -= tile_size
                self.depth += tile_size
                if self.temp2 >= self.waveCoolDown:
                    self.temp2 = 0
            else:
                self.spawnObject()
        if self.lives <=0:
            self.player.alive = False

        # self.mouseOverlap()
        # self.sillyEvent()



    def draw(self):
        if self.startscreenOpen:
            self.startScreenBg()
            self.all_sprites.draw(self.window)
        else:

            self.window.fill(WHITE)
            # pg.draw.rect(self.window)
            self.window.blit(self.bg, (0, self.gameBgMove1))
            self.window.blit(self.bg2, (0, self.gameBgMove1+HEIGHT))
            self.main_sprites.draw(self.window)
            self.player_sprites.draw(self.window)
            self.particle_sprites.draw(self.window)

            self.window.blit(self.topGUI, (0, 0))

            lives = 0
            xVal=5*tile_size
            for i in range(0,self.lives):
                self.window.blit(self.oxygenTank, (xVal, tile_size*2))
                xVal+=15*tile_size
                lives+=1
            for i in range(lives,4):
                self.window.blit(self.oxygenTankEmpty, (xVal, tile_size*2))
                xVal+=15*tile_size

            xVal = 198 * tile_size
            for powerup in self.powerUps:
                if powerup=="speed1":
                    self.window.blit(self.speed1PowerUp, (xVal, tile_size * 3))
                elif powerup=="speed2":
                    self.window.blit(self.speed2PowerUp, (xVal, tile_size * 3))
                elif powerup=="speed3":
                    self.window.blit(self.speed3PowerUp, (xVal, tile_size * 3))
                elif powerup=="heal1":
                    self.window.blit(self.heal1PowerUp, (xVal, tile_size * 3))
                elif powerup=="heal2":
                    self.window.blit(self.heal2PowerUp, (xVal, tile_size * 3))
                elif powerup=="heal3":
                    self.window.blit(self.heal3PowerUp, (xVal, tile_size * 3))
                elif powerup=="strength1":
                    self.window.blit(self.strength1PowerUp, (xVal, tile_size * 3))
                elif powerup=="strength2":
                    self.window.blit(self.strength2PowerUp, (xVal, tile_size * 3))
                elif powerup=="strength3":
                    self.window.blit(self.strength3PowerUp, (xVal, tile_size * 3))
                elif powerup=="large1":
                    self.window.blit(self.tempPowerUp, (xVal, tile_size * 3))
                elif powerup=="large2":
                    self.window.blit(self.tempPowerUp, (xVal, tile_size * 3))
                elif powerup=="large3":
                    self.window.blit(self.tempPowerUp, (xVal, tile_size * 3))
                elif powerup=="explode":
                    self.window.blit(self.explodePowerUp, (xVal, tile_size * 3))
                xVal += 30 * tile_size
            # for i in range(lives, 5):
            #     self.window.blit(self.oxygenTankEmpty, (xVal, tile_size * 2))
            #     xVal += 15 * tile_size


            draw_text_center(self.window, "Score:",45,WHITE,125*tile_size,tile_size*2)
            draw_text_center(self.window, str(int(self.displayScore)), 45, WHITE,125*tile_size, 12*tile_size)
            print(self.realScore)

            # print(self.depth)

            if self.gameBgMove1 <=-HEIGHT:
                self.curWaterColor = [self.curWaterColor[0]-6,self.curWaterColor[1]-6,self.curWaterColor[2]-6]
                if self.curWaterColor[0]<1:
                    self.curWaterColor[0]=1
                if self.curWaterColor[1]<1:
                    self.curWaterColor[1]=1
                if self.curWaterColor[2]<1:
                    self.curWaterColor[2]=1
                self.bg.fill(self.curWaterColor)
                
                nextWaterColor1 = self.curWaterColor[0] - 6
                if nextWaterColor1 < 1:
                    nextWaterColor1 = 1
                nextWaterColor2 = self.curWaterColor[1] - 6
                if nextWaterColor2 < 1:
                    nextWaterColor2 = 1
                nextWaterColor3 = self.curWaterColor[2] - 6
                if nextWaterColor3 < 1:
                    nextWaterColor3 = 1
                self.bg2.fill((nextWaterColor1, nextWaterColor2, nextWaterColor3))
                self.gameBgMove1 = 0


            self.startTime += 1
            if self.startTime < 60:
                draw_text_center(self.window,"Welcome to Slap-Marine!",35,WHITE,WIDTH/2,tile_size*30)
            elif self.startTime < 240:
                draw_text_center(self.window,"Throughout this game, you will attempt to make",35,WHITE,WIDTH/2,tile_size*30)
                draw_text_center(self.window, "your way to the bottom of the ocean!", 35,WHITE, WIDTH / 2, tile_size * 40)
            elif self.startTime < 420:
                draw_text_center(self.window,"Watch out for the fish though,",35,WHITE,WIDTH/2,tile_size*30)
                draw_text_center(self.window, "the deeper you go the stronger they become!", 35,WHITE, WIDTH / 2, tile_size * 40)
            elif self.startTime < 600:
                draw_text_center(self.window,"Inside of these chests you will find valuable powerups!",35,WHITE,WIDTH/2,tile_size*30)
                draw_text_center(self.window, "Press 'enter' or 'space' to activate these powerups!", 35,WHITE, WIDTH / 2, tile_size * 40)
            elif self.startTime < 800:
                draw_text_center(self.window,"Good Luck!",40,WHITE,WIDTH/2,tile_size*30)



        pg.display.flip()

    def guiText(self):
        button_transparency = 100
        for button in self.buttons:
            if button.type == "topGUI":
                button.image = pg.image.load("scripts/assets/topbg.png").convert_alpha()
                thing = draw_text(self.window, self.curcurTip, 30, BLACK,self.tipPos,5, "scripts/assets/fonts/yoster-island/yoster.ttf", True)
                speed = int((thing[0]-thing[1])/300)
                if speed < 2:
                    speed = 2
                if speed >4:
                    speed = 4
                self.tipPos -= speed
                if thing[0] < 0:
                    self.tipPos = 1280
                    self.curcurTip = random.choice(self.tips[0])

    def play(self):
        while self.is_playing:
            # tick clock
            self.clock.tick(FPS)


            self.get_game_events()
            self.update()
            self.draw()

    def mouseOverlap(self, source, shopButton = False, buttonCategory = ""):
        for button in source:
            self.mouse_pos = pg.mouse.get_pos()
            self.mouse_bttns = pg.mouse.get_pressed()
            x = False
            y = False
            if self.mouse_pos[0] < button.xpos + button.width/2 and self.mouse_pos[0] > button.xpos-button.width/2:
                x=True
            if self.mouse_pos[1] < button.ypos + button.height/2 and self.mouse_pos[1] > button.ypos-button.height/2:
                y=True

            if x and y == True:
                pass

    def saveData(self):
        fileWrite = open("scripts/playerData.txt", "w+")
        print("save data?")
        for line in fileWrite.readlines():
            try:
                self.highScore = int(line)
            except:
                pass
        if self.highScore<self.realScore:
            fileWrite.write(str(self.realScore))
            self.highScore = self.realScore
        else:
            print(self.displayLevel,self.highScore)
        fileWrite.close() # hopefully this works



    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.startscreenOpen:
                    self.startScreenAnim = True

    def startScreenBg(self):
        try:
            self.window.fill(BLACK)
            self.window.blit(self.bg, (-self.bgMove1, 0))
            if self.bgMove1 >=self.bg.get_width()-WIDTH:
                self.window.blit(self.bg, (-self.bgMove1+self.bg.get_width(), 0))
            # dark = pg.Surface((80*tile_size, 50*tile_size))
            # dark.fill(BLACK)
            # dark.set_alpha(150)
            # self.window.blit(dark, (0,60*tile_size))
            self.window.blit(self.waves, (-self.bgMove2,135*tile_size))
            if self.bgMove2 >=self.waves.get_width()-WIDTH:
                self.window.blit(self.waves, (-self.bgMove2+self.waves.get_width(), 135*tile_size))
            self.window.blit(self.water, (0,0))
            if self.startScreenAnim:
                self.playerImageBg = pg.transform.rotate(self.playerImageBgT, self.bgMove3R)
                self.window.blit(self.playerImageBg, (WIDTH / 2 - self.playerImageBg.get_width() / 2 + int(self.bgMove3), 150 * tile_size + self.bgMove31))
                if self.bgParticleSpawned==False:
                    self.spawnParticle("bubble","start", random.randint(4, 7), self)
                    self.bgParticleSpawned = True
                self.bgMove3R-=2
                self.bgMove31+=3
                if self.bgMove3R <= -180:
                    self.startScreenAnim = False
                    self.startscreenOpen = False
                    self.prepGame()
            else:
                self.window.blit(self.playerImageBg, (WIDTH/2 -self.playerImageBg.get_width()/2 +int(self.bgMove3),150*tile_size +self.bgMove31))
                if self.bgMove3 <= 10:
                    if self.bgMove3F:
                        self.bgMove3 += 0.5
                else:
                    self.bgMove3F = False
                if self.bgMove3 >= -10:
                    if self.bgMove3F == False:
                        self.bgMove3 -= 0.5
                else:
                    self.bgMove3F = True

                if random.randint(0, 10) == 3:
                    self.spawnParticle("bubble", "start", 1)
                    self.bgMove31 += random.randint(-1, 1)
                    if self.bgMove31 > 5:
                        self.bgMove31 = 5
                    elif self.bgMove31 < -5:
                        self.bgMove31 = -5


            draw_text_center(self.window, "SLAP-MARINE", 60, WHITE, WIDTH/2, HEIGHT / 3,
                             "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
            draw_text_center(self.window, "click anywhere to start!", 30, WHITE, WIDTH / 2, HEIGHT / 2.44,
                             "scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf")
            draw_text_center(self.window, "high score:"+str(self.highScore), 30, RED, WIDTH / 2, HEIGHT / 2.18)


            self.bgMove1 += 1
            self.bgMove2 += 2
            if self.bgMove1 >= self.bg.get_width():
                self.bgMove1 = 0
            if self.bgMove2 >= self.waves.get_width():
                self.bgMove2 = 0


            # image = pg.Surface((WIDTH,HEIGHT), pg.SRCALPHA)
            # image.fill((0,0,0,30))
            # self.window.blit(image, (0, 0))
        except Exception as e:
            pass

    def end_screen(self):

        return "quit"