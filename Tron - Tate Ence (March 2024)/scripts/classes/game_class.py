from scripts.settings import *
from scripts.classes.player_class import Player
from scripts.classes.trail_class import Trail
from scripts.classes.powerUp_class import PowerUp

class Game(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.trails = pg.sprite.Group()

        self.coolDown = 0
        self.cursorPos = 0
        self.cursorActive = True
        self.page = 0
        self.pages = [["play","tutorial","about"],["p v p","p v e","e v e"],["Tron! Avoid~your enemy.~Use arrows/~WASD to move.~Have fun!"],["Hi! This is a~game created~by Tate Ence~in April of~2024. Enjoy!"],["Continue","Return"]]
        self.bg = pg.image.load("scripts/assets/sprites/bg.jpg")
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))

        self.gameType = 0
        self.score = [0,0]
        self.updateTime = 0
        self.startTime = 0
        self.startScreen = True
        self.endScreen = False
        self.endGameScreen = False
        self.dX = 0
        self.dY = 0
        self.temp1 = 0
        self.temp2 = 0
        self.is_playing = True
        self.both = False

        pg.mixer.init()
        pg.mixer.music.load("scripts/assets/sounds/start.mp3")
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)

        pg.display.set_caption("Tron - Tate Ence")
        icon = pg.image.load("scripts/assets/sprites/death2logo.png")
        pg.display.set_icon(icon)

        #POWERUPS: invincibility for period, jumping, speedup/speeddown, rewind, shoot projectile, detroy tail



    def endGame(self,x,y,player,both=False):
        self.dX = x
        self.dY = y
        if both:
            self.score[0] -= 1
            self.score[1] -= 1
            self.both = True
        else:
            self.score[player] -= 1
        self.score[0]+=1
        self.score[1]+=1
        self.endScreen = True

    def startGame(self, gameType):
        self.gameType = gameType
        self.bg = pg.image.load("scripts/assets/sprites/bg2.jpg")
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))

        try:
            self.player1.kill()
            self.player2.kill()
            self.powerUp.kill()
        except:
            pass
        for trail in self.trails:
            trail.kill()

        playerColor1 = random.choice(playerColors)
        playerColor2 = random.choice(playerColors)
        while playerColor2==playerColor1:
            playerColor2 = random.choice(playerColors)
        if self.gameType==0:
            self.player1 = Player(12, 18,playerColor1,self, "WASD",0, False)
            self.player2 = Player(64-12, 18, playerColor2, self, "ARROWS",1, False)
        if self.gameType==1:
            self.player1 = Player(12, 18,playerColor1,self, "WASD",0, False)
            self.player2 = Player(64-12, 18, playerColor2, self, "ARROWS",1, True)
        if self.gameType==2:
            self.player1 = Player(12, 18,playerColor1,self, "WASD",0, True)
            self.player2 = Player(64-12, 18, playerColor2, self, "ARROWS",1, True)
        self.players.add(self.player1)
        self.all_sprites.add(self.player1)
        self.players.add(self.player2)
        self.all_sprites.add(self.player2)
        self.powerUp = PowerUp(self)
        self.all_sprites.add(self.powerUp)

        pg.mixer.music.load("scripts/assets/sounds/gameplay.mp3")
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)

        self.score = [0, 0]
        self.updateTime = 0
        self.startTime = 0
        self.startScreen = True
        self.endScreen = False
        self.endGameScreen = False
        self.dX = 0
        self.dY = 0
        self.temp1 = 0
        self.temp2 = 0
        self.is_playing = True
        self.both = False

    def restart(self):
        if self.startScreen:
            pass
        else:
            try:
                self.player1.kill()
                self.player2.kill()
                self.powerUp.kill()
            except:
                pass
            playerColor1 = random.choice(playerColors)
            playerColor2 = random.choice(playerColors)
            while playerColor2 == playerColor1:
                playerColor2 = random.choice(playerColors)
                print("change color")
            if self.gameType == 0:
                self.player1 = Player(12, 18, playerColor1, self, "WASD", 0, False)
                self.player2 = Player(64 - 12, 18, playerColor2, self, "ARROWS", 1, False)
            if self.gameType == 1:
                self.player1 = Player(12, 18, playerColor1, self, "WASD", 0, False)
                self.player2 = Player(64 - 12, 18, playerColor2, self, "ARROWS", 1, True)
            if self.gameType == 2:
                self.player1 = Player(12, 18, playerColor1, self, "WASD", 0, True)
                self.player2 = Player(64 - 12, 18, playerColor2, self, "ARROWS", 1, True)
            self.players.add(self.player1)
            self.all_sprites.add(self.player1)
            self.players.add(self.player2)
            self.all_sprites.add(self.player2)
            self.powerUp = PowerUp(self)
            self.all_sprites.add(self.powerUp)
            self.updateTime = 0
            self.startTime = 0
            # self.startScreen = True
            self.endScreen = False
            self.temp1 = 0
            self.temp2=  0
            self.both = False
            for trail in self.trails:
                trail.kill()
            print("end?")

    def update(self):
        if self.startScreen:
            pass
            # self.startScreen=False
        elif self.endScreen or self.endGameScreen:
            pass
        else:
            if self.startTime <= 180:
                self.startTime+=1
            else:
                kill = False
                both = False
                self.updateTime+=1
                if self.updateTime>2:
                    self.updateTime = 0
                    self.all_sprites.update(self.clock.tick(FPS))
                    for player in self.players:
                        kill=False
                        if player.alive:
                            for tilea in self.trails:
                                for playera in self.players:
                                    if playera == self.powerUp.player:
                                        if self.powerUp.invincibleTime <= 0: #FIX THISSSSKOSDGUHSL:DGJKHSDL:GKUSDHJGL:KSDJGHL:SDKGJ
                                            if playera.rect.centerx == tilea.rect.centerx and playera.rect.centery == tilea.rect.centery:
                                                if kill:
                                                    both = True
                                                else:
                                                    kill = True
                                                    playerb = playera
                                    else:
                                        if playera.rect.centerx == tilea.rect.centerx and playera.rect.centery == tilea.rect.centery:
                                            if kill:
                                                both = True
                                            else:
                                                kill = True
                                                playerb = playera
                            if player.speed==1:
                                tile = player.playerTiles[len(player.playerTiles)-1]
                                trail = Trail(tile[0], tile[1], player.color)
                                self.trails.add(trail)
                            elif player.speed==2:
                                print("baba")
                                print(player.playerTiles[len(player.playerTiles) - 1],player.playerTiles[len(player.playerTiles) - 2])
                                tile = [player.playerTiles[len(player.playerTiles) - 1],player.playerTiles[len(player.playerTiles) - 2]]
                                trail = Trail(tile[0][0], tile[0][1], player.color)
                                self.trails.add(trail)
                                trail2 = Trail(tile[1][0], tile[1][1], player.color)
                                self.trails.add(trail2)

                    if kill == True:
                        if both:
                            playerb.killPlayer(True)
                        else:
                            playerb.killPlayer()

    def play(self):
        while self.is_playing:
            # tick clock
            self.clock.tick(FPS)
            self.get_game_events()
            self.update()
            self.draw()

    # def checkOverlap(self,obj1,obj2):
    #     if (obj1.rect.left) < (obj2.rect.right):
    #         if obj2.num == 1:
    #             if (obj1.rect.left+20) > (obj2.rect.right):
    #                 if (obj1.rect.top) < (obj2.rect.bottom):
    #                     if (obj1.rect.bottom) > (obj2.rect.top):
    #                         return True
    #     if (obj1.rect.right) > (obj2.rect.left):
    #         if obj2.num == 2:
    #             if (obj1.rect.right-20) < (obj2.rect.left):
    #                 if (obj1.rect.top) < (obj2.rect.bottom):
    #                     if (obj1.rect.bottom) > (obj2.rect.top):
    #                         return True
    #     else:
    #         return False

    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False

    def draw(self):
        self.window.fill(WHITE)
        self.window.blit(self.bg, (0, 0))

        if self.startScreen:
            self.bg = pg.image.load("scripts/assets/sprites/bg.jpg")
            self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))
            keyStates = pg.key.get_pressed()
            if self.coolDown>10:
                if keyStates[pg.K_UP] or keyStates[pg.K_w]:
                    if self.cursorPos > 0:
                        self.cursorPos -= 1
                        self.coolDown = 0
                elif keyStates[pg.K_DOWN] or keyStates[pg.K_s]:
                    if self.cursorPos < len(self.pages[self.page])-1:
                        self.cursorPos += 1
                        self.coolDown = 0
            self.coolDown+=1
            baseSpace= [20 * tile_size[0],10 * tile_size[1]]
            if self.page == 0:
                self.cursorActive = True
                ySpace = (28*tile_size[1])/len(self.pages[0])
                curYSpace = 0
                for thing in self.pages[0]:
                    draw_text_left(self.window, thing, 100, UIRED,baseSpace[0], baseSpace[1] + curYSpace)
                    curYSpace+=ySpace
                if self.coolDown > 15:
                    if keyStates[pg.K_RETURN]:
                        if self.cursorPos==0:
                            self.page = 1
                        elif self.cursorPos==1:
                            self.page = 2
                        elif self.cursorPos==2:
                            self.page = 3
                        self.coolDown = 0
            elif self.page == 1:
                self.cursorActive = True
                ySpace = (28 * tile_size[1]) / len(self.pages[1])
                curYSpace = 0
                for thing in self.pages[1]:
                    draw_text_left(self.window, thing, 100, UIRED, baseSpace[0], baseSpace[1] + curYSpace)
                    curYSpace += ySpace
                if self.coolDown > 15:
                    if keyStates[pg.K_ESCAPE]:
                        self.page = 0
                        self.coolDown = 0
                    if keyStates[pg.K_RETURN]:
                        if self.cursorPos==0:
                            self.startGame(0)
                            self.startScreen= False
                        elif self.cursorPos==1:
                            self.startGame(1)
                            self.startScreen = False
                        elif self.cursorPos==2:
                            self.startGame(2)
                            self.startScreen = False
                        self.coolDown = 0
            elif self.page == 2:
                self.cursorActive = False
                ySpace = (5 * tile_size[1])
                curYSpace = 0
                string = []
                for thing in self.pages[2]:
                    i = 0
                    prevI = -1
                    for let in thing:
                        if let == "~":
                            string.append(thing[prevI + 1:i])
                            prevI = i
                        if i >= len(thing) - 1:
                            string.append(thing[prevI + 1:])
                            break
                        i += 1
                    for string1 in string:
                        draw_text_left(self.window, string1, 100, UIRED, 10 * tile_size[0], baseSpace[1] + curYSpace)
                        curYSpace += ySpace
                if self.coolDown > 15:
                    if keyStates[pg.K_RETURN]:
                        self.page = 0
                        self.coolDown = 0
            elif self.page == 3:
                self.cursorActive = False
                ySpace = (5*tile_size[1])
                curYSpace = 0
                string = []
                for thing in self.pages[3]:
                    i = 0
                    prevI = -1
                    for let in thing:
                        if let=="~":
                            string.append(thing[prevI+1:i])
                            prevI=i
                        if i >= len(thing) - 1:
                            string.append(thing[prevI+1:])
                            break
                        i += 1
                    for string1 in string:
                        draw_text_left(self.window, string1, 100, UIRED, 10 * tile_size[0], baseSpace[1] + curYSpace)
                        curYSpace += ySpace
                if self.coolDown > 15:
                    if keyStates[pg.K_RETURN]:
                        self.page = 0
                        self.coolDown = 0
            if self.cursorActive:
                cursor = pg.Surface((tile_size[0]*4,tile_size[1]*4))
                cursor.fill(UICOLOR)
                rect = cursor.get_rect()
                rect.topleft = [baseSpace[0]-tile_size[0]*6,baseSpace[1]+self.cursorPos*ySpace]
                self.window.blit(cursor, rect.topleft)

        else:
            if not self.endGameScreen:
                self.all_sprites.draw(self.window)
                self.trails.draw(self.window)
            if self.startTime <= 180:
                if self.startTime <= 60:
                    num = pg.image.load("scripts/assets/sprites/3.png")
                elif self.startTime <= 120:
                    num = pg.image.load("scripts/assets/sprites/2.png")
                else:
                    num = pg.image.load("scripts/assets/sprites/1.png")
                num = pg.transform.scale(num, (7 * tile_size[0], 7 * tile_size[1]))
                self.window.blit(num, (WIDTH / 2 - num.get_width() / 2, HEIGHT / 2 - num.get_height() / 2))
            elif self.endScreen:
                self.temp1+=1
                self.temp2+=1
                if self.temp1>=12:
                    if self.both:
                        death = pg.image.load("scripts/assets/sprites/death.png")
                        death = pg.transform.scale(death, (7 * tile_size[0], 7 * tile_size[1]))
                        for player in self.players:
                            self.window.blit(death, (player.rect.centerx - death.get_width() / 2, player.rect.centery - death.get_height() / 2))

                    else:
                        death = pg.image.load("scripts/assets/sprites/death.png")
                        death = pg.transform.scale(death, (7 * tile_size[0], 7 * tile_size[1]))
                        self.window.blit(death, (self.dX- death.get_width() / 2, self.dY- death.get_height() / 2))
                    if self.temp1 >=24:
                        self.temp1 = 0
                draw_text(self.window, (str(self.score[0]) + "   " + str(self.score[1])), 100, UIRED, 32*tile_size[0] - tile_size[0]/2, 12*tile_size[1])
                if self.temp2 >=300:
                    self.cursorPos = 0
                    self.endScreen = False
                    self.endGameScreen = True
            elif self.endGameScreen:
                keyStates = pg.key.get_pressed()
                ySpace = (28 * tile_size[1]) / len(self.pages[4])
                baseSpace = [20 * tile_size[0], 10 * tile_size[1]]
                curYSpace = 0
                for thing in self.pages[4]:
                    draw_text_left(self.window, thing, 100, UIRED,baseSpace[0], baseSpace[1] + curYSpace)
                    curYSpace+=ySpace

                cursor = pg.Surface((tile_size[0] * 4, tile_size[1] * 4))
                cursor.fill(UICOLOR)
                rect = cursor.get_rect()
                rect.topleft = [baseSpace[0] - tile_size[0] * 6, baseSpace[1] + self.cursorPos * ySpace]
                self.window.blit(cursor, rect.topleft)

                if keyStates[pg.K_RETURN]:
                    if self.cursorPos == 0:
                        self.endGameScreen = False
                        self.restart()
                    else:
                        self.startScreen = True
                        self.endGameScreen = False
                        self.page = 0
                        self.coolDown = 0

                elif keyStates[pg.K_UP] or keyStates[pg.K_w]:
                    if self.cursorPos >0:
                        self.cursorPos = 0
                elif keyStates[pg.K_DOWN] or keyStates[pg.K_s]:
                    if self.cursorPos < 1:
                        self.cursorPos = 1
            else:
                if self.powerUp.owned:
                    if not self.powerUp.active:
                        image = pg.image.load(self.powerUp.powerUpNum[1])
                        image = pg.transform.scale(image, (6 * tile_size[0], 6 * tile_size[1]))
                        if self.powerUp.playerOwned == 0:
                            self.window.blit(image, (tile_size[0], 23 * tile_size[1]))
                        else:
                            self.window.blit(image, (tile_size[0]*57, 23 * tile_size[1]))
        pg.display.flip()


    def end_screen(self):
        print("end")
        return "quit"