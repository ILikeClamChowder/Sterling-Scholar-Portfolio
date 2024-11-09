from scripts.settings import *
from scripts.classes.controller_class import *
from scripts.classes.player_class import Player
from scripts.classes.bullet_class import Bullet
from scripts.classes.particle_class import Particle

class Game(object):
    def __init__(self):
        pg.init()
        pg.joystick.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.enemyBullets = pg.sprite.Group()
        self.playerBullets = pg.sprite.Group()
        self.particle_sprites = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.is_playing = True

        # create images
        self.bg1 = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/bg2.jpg"),(WIDTH,HEIGHT))
        self.bg1Copy = self.bg1.copy()
        self.bg2 = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/bg2.jpg"), (WIDTH, HEIGHT))
        self.bg2Copy = self.bg2.copy()
        self.titleImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/title.png"),(372,180))
        self.startImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/start.png"),(208,116))
        self.hoverStartImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/hoverstart.png"),(208, 116))
        self.startImgRect = self.startImg.get_rect()
        self.aboutImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/about.png"), (208, 116))
        self.hoverAboutImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/hoverabout.png"),(208,116))
        self.aboutImgRect = self.aboutImg.get_rect()
        self.buttonImage = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/button.png"),(11*tileDivide,10*tileDivide))
        self.buttonImageT = self.buttonImage.copy()
        self.heartImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/heart.png"),(14 * tileDivide, 14 * tileDivide))
        self.emptyHeartImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/emptyheart.png"),(14 * tileDivide, 14 * tileDivide))
        self.tutImg = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/tut.png"),(109 * tileDivide, 38 * tileDivide))
        self.topGui = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/topgui.png"),(144 * tileDivide, 20 * tileDivide))
        self.bottomGui = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/bottombg.jpg"),(168 * tileDivide, 36 * tileDivide))
        self.bottomGui2 = self.bottomGui.copy()
        self.badgeGui = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/badge.png"),(113*tileDivide,57*tileDivide))
        self.badge3 = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/gold.png"),(22*tileDivide,22*tileDivide))
        self.badge2 = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/silver.png"),(22 * tileDivide, 22 * tileDivide))
        self.badge1 = pg.transform.scale(pg.image.load("scripts/assets/sprites/background/bronze.png"),(22 * tileDivide, 22 * tileDivide))

        # create fonts
        self.font1 = pg.font.Font("scripts/assets/fonts/ONESIZE_.TTF", 20)
        self.font2 = pg.font.Font("scripts/assets/fonts/pixelNums.ttf",60)
        self.font3 = pg.font.Font("scripts/assets/fonts/ONESIZE_.TTF", 40)
        self.font4 = pg.font.Font("scripts/assets/fonts/pixelNums.ttf", 40)

        # create sounds
        pg.mixer.Channel(0).set_volume(0.3) # dialogue
        pg.mixer.Channel(1).set_volume(0.2)  # death
        pg.mixer.Channel(2).set_volume(0.2)  # ding sound
        pg.mixer.Channel(3).set_volume(0.2) # typewriter click
        pg.mixer.Channel(4).set_volume(0.2)  # typewriter click
        pg.mixer.Channel(5).set_volume(0.5)  # helicopter
        pg.mixer.music.load("scripts/assets/sounds/music.ogg")
        pg.mixer.music.set_volume(0.2)
        pg.mixer.music.play(-1)

        pg.display.set_icon(pg.image.load("scripts/assets/sprites/background/icon.png"))
        pg.display.set_caption("Flappy Bird: Apocalypse")

        # startScreen Vars
        self.aboutPage=False
        self.startSiren=False
        self.waitTime = 0
        self.gameBgMove1 = 0
        self.gameBgMove2=0
        self.deathCircle = 2400
        self.startScreenActive = True #CHANGE THIS TO STOP START SCREEN
        self.hoverStart = [False, False]
        self.startScreenTime = 0
        self.buttonBounce = False
        self.bounceTime = 0
        self.textNum=0
        self.letterNum=0
        self.textWaitTime=0
        self.circle1 = False
        self.circle2 = False
        self.scuffed=False
        self.clickingTime = 0
        self.curText = introText
        self.endStart=False

        # game vars
        self.deathCooldown=0
        self.playerHealth = 3
        self.startingGame=True
        self.playerClicking=False
        self.curLevel=0
        self.score=0
        self.trophiesAwarded = [False,False,False]
        self.highScore = 0


        # add classes
        if self.startScreenActive:
            self.player = Player(True,False)
        else:
            self.player = Player(False,True)
        self.player.add(self.players)



    def update(self):
        if not self.player.intro:
            if random.randint(0,120)==1:
                self.createBullet(random.randint(0,5))

        for bullet in self.enemyBullets:
            if bullet.rect.top > HEIGHT -self.bottomGui.get_height()- 5 or bullet.rect.right < -5 or bullet.rect.bottom < -5 or bullet.rect.left > WIDTH + 5:
                self.score+=1
                pg.mixer.Channel(2).play(dingSound)
                self.spawnParticle("scripts/assets/sprites/background/point.png", 0,int(random.randint(int(tileDivide * 20), int(WIDTH - tileDivide * 20))), int(HEIGHT - 40),[random.randint(-1, 1), random.randint(-5, -1)], 80)
                bullet.kill()

        if not self.trophiesAwarded[0] and self.score>20:
            self.spawnParticle("scripts/assets/sprites/background/bronze.png",0,int(random.randint(int(tileDivide * 20), int(WIDTH - tileDivide * 20))), int(HEIGHT - 40),[random.randint(-1,1),random.randint(-3,-1)],140)
            self.trophiesAwarded[0]=True
        elif not self.trophiesAwarded[1] and self.score>75:
            self.spawnParticle("scripts/assets/sprites/background/silver.png",0,int(random.randint(int(tileDivide * 20), int(WIDTH - tileDivide * 20))), int(HEIGHT - 40),[random.randint(-1,1),random.randint(-3,-1)],140)
            self.trophiesAwarded[1] = True
        elif not self.trophiesAwarded[2] and self.score>250:
            self.spawnParticle("scripts/assets/sprites/background/gold.png",0,int(random.randint(int(tileDivide * 20), int(WIDTH - tileDivide * 20))), int(HEIGHT - 40),[random.randint(-1,1),random.randint(-3,-1)],140)
            self.trophiesAwarded[2] = True


        self.playerCollision()
        self.all_sprites.update()
        self.players.update()
        self.enemyBullets.update()
        self.playerBullets.update()

    def draw(self):
        self.window.blit(self.bg2, (-self.gameBgMove1, 0))
        self.window.blit(self.bg2Copy, (-self.gameBgMove1 + WIDTH, 0))
        self.gameBgMove1 += 1
        self.gameBgMove2+=2
        if self.gameBgMove1 >= self.bg1.get_width():
            self.gameBgMove1 = 0
        if self.gameBgMove2 >= self.bottomGui.get_width():
            self.gameBgMove2 = 0

        self.all_sprites.draw(self.window)
        if self.player.intro:
            self.window.blit(self.tutImg,(WIDTH/2 - self.tutImg.get_width()/2,HEIGHT/1.41 - self.tutImg.get_height()/2))
        # for bullet in self.enemyBullets:
        #     pg.draw.ellipse(self.window,BLACK,bullet.rect)

        self.window.blit(self.bottomGui, (-self.gameBgMove2, HEIGHT - self.bottomGui.get_height()))
        self.window.blit(self.bottomGui2, (-self.gameBgMove2 + WIDTH, HEIGHT - self.bottomGui.get_height()))
        self.drawGuis()
        self.players.draw(self.window)


        if self.playerHealth<=0:
            self.window.blit(self.badgeGui,(WIDTH/2-self.badgeGui.get_width()/2,HEIGHT/2-self.badgeGui.get_height()/2))
            if self.trophiesAwarded[2]:
                self.window.blit(self.badge3,(WIDTH/2-tileDivide*43,HEIGHT/2-tileDivide*7))
            elif self.trophiesAwarded[1]:
                self.window.blit(self.badge2,(WIDTH/2-tileDivide*43,HEIGHT/2-tileDivide*7))
            elif self.trophiesAwarded[0]:
                self.window.blit(self.badge1,(WIDTH/2-tileDivide*43,HEIGHT/2-tileDivide*7))
            draw_text_right(self.window,str(self.score),poop,tileDivide*120,tileDivide*117,self.font4)
            draw_text_right(self.window, str(self.score), poop, tileDivide * 120, tileDivide * 139, self.font4)
        else:
            draw_text_center(self.window, str(self.score), WHITE, WIDTH / 2, HEIGHT / 6, self.font2)

        if self.startingGame:
            if self.deathCircle < 2500:
                self.deathCircle += 10
            else:
                self.startingGame=False
            pg.draw.circle(self.window, BLACK, self.player.rect.center, self.deathCircle,
                           math.ceil(WIDTH * 2))  # death circle

        pg.display.flip()

    def saveData(self):

        fileRead = open("scripts/playerData.txt", "r")
        thing = fileRead.read()
        self.highScore = int(thing)
        if int(thing)<self.score:
            fileWrite = open("scripts/playerData.txt", "w")
            self.highScore = self.score
            fileWrite.write(str(self.score))
            fileWrite.close()
            print("dfg")
        fileRead.close()  # hopefully this works


    def spawnParticle(self, type, amount, x=0, y=0, moveVec=[1,1],decayTime=255,game=False):

        if amount > 0:
            particle = Particle(type, x, y, amount, self, moveVec)
        else:
            particle = Particle(type, x, y, amount, False, moveVec)
        self.particle_sprites.add(particle)
        self.all_sprites.add(particle)

    def playerCollision(self):
        collide = pg.sprite.spritecollideany(self.player, self.enemyBullets)
        if collide != None:
            if collide.waitTime<=0:
                if self.player.playerActive:
                    pg.mixer.Channel(1).play(deathSound)
                self.player.playerActive=False
        if self.player.rect.top>HEIGHT-self.bottomGui.get_height():
            if self.player.playerActive:
                pg.mixer.Channel(1).play(deathSound)
                self.player.playerActive=False
            if self.player.rect.top>HEIGHT:
                self.playerHealth-=1
                if self.playerHealth>0:
                    self.player.kill()
                    self.player = Player(False,False)
                    self.players.add(self.player)
                else:
                    self.saveData()

    def createBullet(self,num):
        yval1 = random.randint(150,220)*tileDivide
        xval1 = random.randint(100, 144)*tileDivide
        speed = [-random.randint(1,2),0]
        speed1 = [0, random.randint(1, 2)]
        if num==0: # x axis tube
            bullet = Bullet(0,WIDTH,yval1,speed)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
            bullet = Bullet(1,WIDTH,yval1-(random.randint(50,150)*tileDivide),speed)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
        elif num==1: # x axis cheep cheep
            bullet = Bullet(2, WIDTH, int(random.randint(int(20*tileDivide),int(HEIGHT+20*tileDivide-self.bottomGui.get_height()))), [-2,-3])
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
        elif num==2: # x axis bullet bill
            bullet = Bullet(3, WIDTH, random.randint(0,int(HEIGHT-self.bottomGui.get_height())), [-2, 0])
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)

        elif num==3: # y axis tube
            bullet = Bullet(0, xval1,0, speed1,90)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
            bullet = Bullet(1, xval1 - (random.randint(50, 100) * tileDivide), 0, speed1,90)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
        elif num==4: # y axis cheep cheep
            bullet = Bullet(2, random.randint(0,int(WIDTH)), 0, [random.randint(-1,1), 0],90)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)
        elif num==5: # y axis bullet bill
            bullet = Bullet(3, random.randint(0,int(WIDTH)), 0, [0, 4],90)
            bullet.add(self.enemyBullets)
            bullet.add(self.all_sprites)


    async def play(self):
        while self.is_playing:
            # tick clock
            self.clock.tick(FPS)
            self.get_game_events()
            if self.startScreenActive:
                self.startScreen()
            else:
                if self.playerHealth>0:
                    self.update()
                self.draw()
            await asyncio.sleep(0)


    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if not self.playerClicking:
                    if not self.startScreenActive:
                        if not self.startingGame:
                            self.player.playerJump()
                else:
                    self.playerClicking=True
            elif event.type == pg.MOUSEBUTTONUP:
                self.playerClicking=False

    def rectMouseOverlap(self,mouse_pos,mouseButtons,rect,num):

            x = False
            y = False
            if mouse_pos[0] < rect.right and mouse_pos[0] > rect.left:
                x=True
            if mouse_pos[1] < rect.bottom and mouse_pos[1] > rect.top:
                y=True

            if x and y:
                self.hoverStart[num]=True
                if mouseButtons[0] or mouseButtons[1] or mouseButtons[2]:
                    return True
            else:
                self.hoverStart[num]=False

    def drawGuis(self):

        # draw_text(self.window)


        # draw hearts
        xval = tileDivide*50
        a=-1
        for a in range(self.playerHealth):
            self.window.blit(self.heartImg,(xval,HEIGHT-self.heartImg.get_height()-tileDivide*6))
            xval+=self.heartImg.get_width()+tileDivide
        for b in range(1,3-a):
            self.window.blit(self.emptyHeartImg, (xval,HEIGHT-self.heartImg.get_height()-tileDivide*6))
            xval += self.heartImg.get_width() + tileDivide



    def startScreen(self):
        self.window.blit(self.bg1, (-self.gameBgMove1,0))
        self.window.blit(self.bg1Copy, (-self.gameBgMove1 + WIDTH,0))
        self.window.blit(self.bottomGui, (-self.gameBgMove2, HEIGHT-self.bottomGui.get_height()))
        self.window.blit(self.bottomGui2, (-self.gameBgMove2 + WIDTH, HEIGHT-self.bottomGui.get_height()))
        self.all_sprites.update()
        self.all_sprites.draw(self.window)
        self.players.update()
        self.players.draw(self.window)

        if self.clickingTime>0:
            self.clickingTime-=1

        if self.startScreenTime>=1:
            self.buttonImage = pg.transform.rotate(self.buttonImageT,-self.startScreenTime)
            xval = WIDTH-WIDTH/8-(self.startScreenTime**0.5)*tileDivide*6.5
            yval = self.startScreenTime**1.5-self.buttonImage.get_height()
            if self.buttonBounce:
                yval += -((self.bounceTime)**0.80)*40
            if self.startScreenTime**1.5>=self.player.rect.top:
                self.buttonBounce=True
                self.bounceTime+=1
                if self.startSiren==False:
                    self.startSiren=True
                    pg.mixer.Channel(4).play(pg.mixer.Sound("scripts/assets/sounds/sirenn.ogg"))
                if yval > HEIGHT:
                    if not self.circle1:
                        self.bounceTime=0
                        self.circle1=True
                        self.circle2=False
                        self.textNum = 0
                        self.letterNum = 0
                        self.textWaitTime = 0
                        self.scuffed=False
                        self.curText=introText2
                        if self.endStart:
                            self.startScreenActive=False
                            self.player.kill()
                            self.player = Player(False,True)
                            self.players.add(self.player)
                            return
                        else:
                            self.endStart=True
                            pg.mixer.music.fadeout(4000)
                            pg.mixer.Channel(5).play(pg.mixer.Sound("scripts/assets/sounds/helicpoter.ogg"), 0, 0, 8000)

            self.window.blit(self.buttonImage,(xval,yval))
            self.startScreenTime+=1

        else:
            if not self.circle2:
                self.window.blit(self.titleImg,(WIDTH/2-self.titleImg.get_width()/2,HEIGHT/8.41))
                self.startImgRect.topleft = (40, HEIGHT / 2.8)
                self.aboutImgRect.topleft = (WIDTH-40-self.aboutImg.get_width(),HEIGHT/2.8)

                if self.hoverStart[0]:
                    self.window.blit(self.hoverStartImg, self.startImgRect)
                else:
                    self.window.blit(self.startImg, self.startImgRect)
                if self.hoverStart[1]:
                    self.window.blit(self.hoverAboutImg, self.aboutImgRect.topleft)
                else:
                    self.window.blit(self.aboutImg, self.aboutImgRect.topleft)

                if not self.circle1:
                    self.circle1 = self.rectMouseOverlap(pg.mouse.get_pos(), pg.mouse.get_pressed(), self.startImgRect, 0)
                    if self.circle1:
                        pg.mixer.music.fadeout(4000)
                        pg.mixer.Channel(5).play(pg.mixer.Sound("scripts/assets/sounds/helicpoter.ogg"),0,0,8000)
                    if self.rectMouseOverlap(pg.mouse.get_pos(), pg.mouse.get_pressed(), self.aboutImgRect, 1):
                        self.circle1=True
                        self.aboutPage=True
                        self.curText = aboutText

        self.dispIntroText(self.curText)

        if self.circle2:
            if self.deathCircle < 2100:
                self.deathCircle += 10
            else:
                if self.textNum == 0:
                    if self.aboutPage:
                        self.circle2=False
                        self.aboutPage=False
                        self.textNum = 0
                        self.letterNum = 0
                        self.textWaitTime = 0
                        self.scuffed = False
                        self.curText = introText
                    else:
                        if self.startScreenTime < 1:
                            self.startScreenTime += 1
            pg.draw.circle(self.window, BLACK, self.player.rect.center, self.deathCircle,
                           math.ceil(WIDTH * 2))  # death circle



        self.gameBgMove1 += 1
        if self.gameBgMove1 >= self.bg1.get_width():
            self.gameBgMove1 = 0
        self.gameBgMove2+=2
        if self.gameBgMove2 >= self.bottomGui.get_width():
            self.gameBgMove2 = 0

        pg.display.flip()

    def dispIntroText(self,text):
        if self.circle1 == True:
            if self.deathCircle > 1100:
                self.deathCircle -= 10
            else:
                if self.textNum == 0:
                    self.textNum = 1
                    self.letterNum = 0
                    pg.mixer.Channel(0).play(pg.mixer.Sound(text[0][1]))
            pg.draw.circle(self.window, BLACK, self.player.rect.center, self.deathCircle,
                           math.ceil(WIDTH * 2))  # death circle


        if self.textNum > 0:
            self.textWaitTime += 1
            if self.textWaitTime >= self.waitTime:
                if self.textNum > len(text):
                    self.circle1 = False
                    self.circle2 = True
                    self.textNum = 0
                    if not self.endStart and not self.aboutPage:
                        pg.mixer.Channel(0).play(pg.mixer.Sound("scripts/assets/sounds/fall.ogg"))
                if not self.circle2:

                    self.waitTime = random.randint(2,5)
                    self.letterNum += 1
                    self.textWaitTime = 0
                    if len(text[self.textNum - 1]) == 1:
                        if self.letterNum >= len(text[self.textNum - 1][0]):
                            try:
                                if len(text[self.textNum]) != 1:
                                    pg.mixer.Channel(0).play(pg.mixer.Sound(text[self.textNum][1]))
                            except:
                                self.scuffed = True
                            self.letterNum = 0
                            self.textNum += 1
                            self.waitTime = 10
                    else:
                        if pg.mixer.Channel(0).get_busy() == False and self.letterNum >= len(
                                text[self.textNum - 1][0]):
                            try:
                                if len(text[self.textNum]) != 1:
                                    pg.mixer.Channel(0).play(pg.mixer.Sound(text[self.textNum][1]))
                            except:
                                self.scuffed = True
                            self.letterNum = 0
                            self.textNum += 1
                        elif not self.letterNum >= len(
                                text[self.textNum - 1][0]):
                            pg.mixer.Channel(3).play(pg.mixer.Sound(random.choice(clickSounds)))

            if not self.circle2:
                if not self.scuffed:
                    ynum = WIDTH / 10
                    draw_text_center(self.window, "TAP ANYWHERE TO SKIP", WHITE, WIDTH / 2, HEIGHT - WIDTH/20,
                                     self.font1)
                    pressing = pg.mouse.get_pressed()

                    for a in range(self.textNum):
                        try:
                            textcolor = text[a][2]
                        except:
                            textcolor = WHITE

                        if a < self.textNum - 1:
                            draw_text(self.window, text[a][0], textcolor, WIDTH / 40, ynum, self.font1)
                        else:
                            draw_text(self.window, text[a][0][:self.letterNum], textcolor, WIDTH / 40, ynum,
                                      self.font1)
                        ynum += WIDTH / 12
                    if (pressing[0] or pressing[1] or pressing[2]) and self.clickingTime == 0:
                        try:
                            if len(text[self.textNum]) != 1:
                                pg.mixer.Channel(0).play(pg.mixer.Sound(text[self.textNum][1]))
                        except:
                            self.scuffed = True
                        self.letterNum = 0
                        self.textNum += 1
                        self.clickingTime = 6
                else:
                    pg.mixer.Channel(5).fadeout(1000)
                    pg.mixer.music.play(-1, 0.0, 1000)


    def end_screen(self):
        self.saveData()
        return "quit"
