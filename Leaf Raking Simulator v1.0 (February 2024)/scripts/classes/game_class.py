from scripts.settings import *
from scripts.classes.player_class import Player
from scripts.classes.leaf_class import Leaf
from scripts.classes.gui_class import GUI
from scripts.classes.rake_class import Rake
from scripts.classes.roomba_class import Roomba


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
        self.bg = pg.image.load("scripts/assets/sprites/maps/0.jpg").convert_alpha()
        self.bg = pg.transform.scale(self.bg, (WIDTH,HEIGHT))

        self.is_playing = True



        # name 0, bounds(lengthX, offsetX, lengthY, offsetY) 1, exit locations((xLeft,xRight,yLeft,yRight,location)(xLeft,xRight,yLeft,yRight,location)) 2, leaf amount 3, leaf value 4, bg img source 5, leaf img source 6, price 7, owned? 8, [leafsize x, leafsize y] 9, equipped 10
        self.locations = [["mom's lawn",[WIDTH,0,HEIGHT-190,70],[[WIDTH-50,WIDTH+50,HEIGHT*0.5,HEIGHT*0.75,""]],35,1,"scripts/assets/sprites/maps/0.jpg","scripts/assets/sprites/leaves/0.png", 0 , True, [11,21], False],
                          ["local park",[WIDTH,0,HEIGHT-190,70],"",55,6,"scripts/assets/sprites/maps/1.jpg","scripts/assets/sprites/leaves/1.png", 400, False, [19,22], False],
                          ["the local skyscraper",[930,285,430,110], "",24,34,"scripts/assets/sprites/maps/2.jpg","scripts/assets/sprites/leaves/2.png",3700,False,[13,18],False],
                          # ["amazon rain forest"],
                          ["frozen ice caps",[860,150,330,175], "",25,143,"scripts/assets/sprites/maps/3.jpg","scripts/assets/sprites/leaves/3.png",24000,False,[11,21],False],
                          ["the royal gardens",[WIDTH,0,HEIGHT-240,120],"",75,562,"scripts/assets/sprites/maps/4.jpg","scripts/assets/sprites/leaves/4.png",225000,False,[17,20],False],
                          ["an erupting volcano",[910,200,HEIGHT-190,70],"",40,3498,"scripts/assets/sprites/maps/5.jpg","scripts/assets/sprites/leaves/5.png",1900000,False,[11,21],False],
                          # ["leaf raking heaven",[WIDTH,0,HEIGHT-190-200,270],[[WIDTH-50,WIDTH+50,HEIGHT*0.5,HEIGHT*0.75,""]],55,18998,"scripts/assets/sprites/maps/6new.jpg","scripts/assets/sprites/leaves/6new.png", 0 , True, [12,22], False],
                          # ["bonus map :3",[WIDTH,0,HEIGHT,0],[[WIDTH-50,WIDTH+50,HEIGHT*0.5,HEIGHT*0.75,""]],300,4,"scripts/assets/sprites/shop.png","scripts/assets/sprites/shop.png", 800, False, [19,22],False]
                          ]

        # go by current rake
        self.tips = [["Welcome to Leaf Raking Simulator!",'"Is this dude seriously raking leaves with a spoon?" - Local school child','"You will NEVER become a world class Leaf Raker!" - Your Neighbor','Use arrow keys or WASD to move!','Purchase a new "rake" in the shop!','Your family cries of dissapointment when they see you','"local hysterical man rakes his leaves with a spoon" - LeavesVille News'],
                     ['"What is this freak doing in my favorite park???" - Your Neighbor',"Great job getting out fo your mom's backyard!",'You have become known as "an average leaf raker"!',"Purcahse a roomba to assist you with your raking!",'"My yard has more leaves that need raked young man!!" - Your mom','"Mom can you make this man go away so I can play?" - Local child'],
                     ['"You get down from there right this instant!!" - Your mom','"How did leaves even get up there?" - Python teacher',"Safety nets have been installed so that players cannot harm themselves!",'"This guy is still making me angry, and I do not know why!" - Your Neighbor', "That's a nice rake youy got there!",'"Man covers city floor in leaves while raking leaves top of skyscraper!" - LeavesTown News'],
                     ['"Man pushes frozen leaves into ocean, reversing global warming?!" - LeavesCapital News','"Man enslaves roombas to work for him on frozen glacier!" - LeavesCity News',"Glaciers are cold! Rake plenty of leaves so you don't freeze!",'"My neighbor is out raking the ice caps?! That makes me so angry!" - Your neighbor',"Brrrrrrrrrrrrrrrr so cold :(", "Ermm, witawwy were awe da polar bearws ???"],
                     ['"You have done me a big favor! I will pay you gratiously for raking my leaves!" - The King of England','"How did he get the king to let him rake the leaves!? He must be using witch craft!" - Your Neighbor','"Experts say that these leaves are actually infused with gold" - LeavesCapital News',"You must feel lucky to be able to rake such an important persons leaves!",'You may finally be able to consider yourself a world class leaf raker!',"rake them leaves gang lolol","I'm running out of tip bar ideas mmmm sad"],
                     ['"Oh now he has done it, he is SO grounded when he gets home!!!1!!!" - Your mom',"If you can believe it, this isn't even the most unrealistic level! Lucky you!","Take a deep breath in and feel those toxic volcanic fumes!",'"A rescue helicopter has been sent to rescue a man raking leaves inside of an active volcano!" - LeavesEmpire News','"A helicopter has just been seen falling into an active volcano! Stay away!" - VolcanicLeaf News',"All your work to reduce global warming has now been reversed!","If you haven't figured it out quite yet, use WASD or arrow keys to move!"],
                     ["*Mama, we made it. Leaf Raking Heaven!*",'"Oh he is going straight to Leaf Raking Hell when he gets home!!1!!" - Your mom',"If you pray hard enough, you may see a Leaf Raking Agnel!!",'"Finally, that weird kid has finally stopped raking leaves onto my lawn!!" - Your Neighbor',"Updates (hopefully) coming soon!",'"Local man seen shifting into another place of existence? We are still profoundly confused!" - LeavesVille News',"Check out ILikeClamChowder on itch.io!",'Glowy leaves :3 yaiy','"Glowing leaves seen falling onto peoples heads, selling for millions!" - LeavesEmpire News']]
        self.tipPos = 1280

        self.leafCur = 0
        self.upgMultiplier = 1
        self.eventActive = False
        self.temp = 0
        self.rakeT = False
        self.shopSpin1 = False
        self.shopSpin2 = False
        self.temp2 = 600
        self.temp3 = 0

        self.shopOpen = False
        self.startscreenOpen = True
        self.startScreenBg()

        # load images

        # load fonts
        self.regfont1 = pg.font.Font("scripts/assets/fonts/yoster-island/yoster.ttf", 30)
        self.regFont2 = pg.font.Font("scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf",60)
        self.regFont3 = pg.font.Font("scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf",30)
        self.regFont4= pg.font.Font("scripts/assets/fonts/marioKart/Mario-Kart-DS.ttf", 25)
        self.regFont5 = pg.font.Font("scripts/assets/fonts/Quinque/Quinquefive-ALoRM.ttf",8)
        self.regfont6 = pg.font.Font("scripts/assets/fonts/yoster-island/yoster.ttf", 40)


    def prepGame(self,map,rake,roomba):
        self.leaves = pg.sprite.Group()
        self.load_map(map)
        self.player = Player(WIDTH / 2, HEIGHT / 2, self)
        self.rake = Rake(rake, self)
        self.roomba = Roomba(roomba, self)

        self.all_sprites.add(self.roomba)
        self.main_sprites.add(self.roomba)
        self.all_sprites.add(self.player)
        self.main_sprites.add(self.player)
        self.all_sprites.add(self.rake)
        self.main_sprites.add(self.rake)

        fileRead = open("scripts/playerData.txt", "r")
        count = 0
        count2 = 0
        count3 = 0
        count4 = 0
        for line in fileRead.readlines():
            if count == 1:
                self.leafCur = int(line)
            if count == 2:
                for char in line:
                    try:
                        if int(char) == 0:
                            bool = False
                        else:
                            bool = True
                        self.locations[count2][8] = bool
                        count2 += 1
                    except:
                        pass
            if count == 3:
                for char in line:
                    try:
                        if int(char) == 0:
                            bool = False
                        else:
                            bool = True
                        rakeA[count3][6] = bool
                        count3 += 1
                    except:
                        pass
            if count == 4:
                for char in line:
                    try:
                        if int(char) == 0:
                            bool = False
                        else:
                            bool = True
                        roombaA[count4][5] = bool
                        count4 += 1
                    except:
                        pass
            count += 1

    def addCurrency(self, amount):
        if not self.startscreenOpen:
            self.leafCur += amount*self.upgMultiplier


    def spawnLeaf(self,price,image, sizex, sizey):
        leaf = ""
        leaf = Leaf(self,random.randrange(self.location[1][1],self.location[1][0]+self.location[1][1]-int(sizex)),random.randrange(self.location[1][3],self.location[1][2]+self.location[1][3]-int(sizey)) ,price,image, sizex, sizey)
        self.leaves.add(leaf)
        self.all_sprites.add(leaf)

    def sillyEvent(self):

        if self.eventActive == False:
            self.temp = 0
            if random.randint(1, 100) == 1:
                print("silly event :33333")
                self.eventActive = True
            return
        self.temp = self.temp + 1
        if self.temp >= 600:
            self.eventActive = False

    def load_map(self,location):

        self.location = self.locations[location]
        self.location[10] = True
        try:
            self.curTip = self.tips[location]
        except:
            self.curTip = self.tips[0]
            print("NO TIP WORK??")
        self.curcurTip = random.choice(self.curTip)

        for leaf in self.leaves:
            leaf.kill()
        #load leaves, also will need to load leaf image
        for i in range(0,self.location[3]):
            self.spawnLeaf(self.location[4],self.location[6], self.location[9][0],self.location[9][1])

        # load bg image
        self.bg = pg.image.load(self.location[5]).convert_alpha()
        self.bg = pg.transform.scale(self.bg, (WIDTH, HEIGHT))

    def teleport(self):
        
        if self.location == self.locations[1]:
            self.load_map(self.locations[0])
        else:
            self.load_map(self.locations[1])


    def createGUIS(self):
        self.buttons = pg.sprite.Group()
        self.clickable = pg.sprite.Group()
        tipBar = GUI("topGUI", WIDTH/2, 100, WIDTH, 200, "scripts/assets/topbg.png",True)
        self.buttons.add(tipBar)
        bottomGUI = GUI("bottomGUI", WIDTH / 2, HEIGHT-75, WIDTH, 150, "scripts/assets/bottombg.png",True)
        self.buttons.add(bottomGUI)
        curRakeImg = GUI("curRakeImg", WIDTH / 5, HEIGHT-70, 6, 6, self.rake.rakeNum[0])
        self.buttons.add(curRakeImg)
        shop = GUI("shop", WIDTH - 100, HEIGHT-100, 200, 50, "color")
        self.buttons.add(shop)
        self.clickable.add(shop)
        # prestige = GUI("prestige", WIDTH - 180, HEIGHT - 40, 200, 50, "color")
        # self.buttons.add(prestige)
        # self.clickable.add(prestige)


        # shop items from here on out
        self.shopButtons = pg.sprite.Group()
        self.allShopSprites = pg.sprite.Group()

        shopBg = GUI("shop", WIDTH/2, HEIGHT/2, WIDTH, HEIGHT, "scripts/assets/shopbg.png", True)
        self.allShopSprites.add(shopBg)
        shopClose = GUI("shopClose", WIDTH-25, 25,50, 50, "scripts/assets/X.png", True)
        self.allShopSprites.add(shopClose)
        self.shopButtons.add(shopClose)

        xval1 = 360
        for location in self.locations:
            try:
                mapIcon = GUI("mapIcon", xval1, 293, 75, 125, location[6], "baba")
                mapIcon.name = location[0]
                mapIcon.price = location[7]
                mapIcon.owned = location[8]
                mapIcon.equipped = location[10]
            except:
                mapIcon = GUI("mapIcon", xval1, 293, 75, 125, "scripts/assets/sprites/player/unused/1.png", "baba")
                mapIcon.name = location[0]
                mapIcon.price = "Unkown"
                mapIcon.owned = "Unkown"
                mapIcon.equipped = "Unkown"
            self.allShopSprites.add(mapIcon)
            self.shopButtons.add(mapIcon)
            xval1+=120

        xval2 = 360
        for rake in rakeA:
            try:
                rakeIcon = GUI("rakeIcon", xval2, 476, 75, 125, rake[0], "baba")
                rakeIcon.name = rake[4]
                rakeIcon.price = rake[5]
                rakeIcon.owned = rake[6]
                rakeIcon.equipped = rake[9]
            except:
                rakeIcon = GUI("rakeIcon", xval2, 476, 75, 125, "scripts/assets/sprites/player/unused/1.png", "baba")
                rakeIcon.name = "Unkown"
                rakeIcon.price = "Unkown"
                rakeIcon.owned = "Unkown"
                rakeIcon.equipped = "Unkown"
            self.allShopSprites.add(rakeIcon)
            self.shopButtons.add(rakeIcon)
            xval2 += 140

        spinningRakeIcon = GUI("spinningRakeIcon", 204, 354, 100, 100, self.rake.rakeNum[0], True, True)
        self.allShopSprites.add(spinningRakeIcon)


        xval3 = 360
        for roomba in roombaA:
            try:
                roombaIcon = GUI("roombaIcon", xval3, 660, 75, 125, roomba[0], "baba")
                roombaIcon.name = roomba[3]
                roombaIcon.price = roomba[4]
                roombaIcon.owned = roomba[5]
                roombaIcon.equipped = roomba[9]
            except:
                roombaIcon = GUI("roombaIcon", xval3, 660, 75, 125, "scripts/assets/sprites/player/unused/1.png", "baba")
                roombaIcon.name = "Unkown"
                roombaIcon.price = "Unkown"
                roombaIcon.owned = "Unkown"
                roombaIcon.equipped = "Unkown"
            self.allShopSprites.add(roombaIcon)
            self.shopButtons.add(roombaIcon)
            xval3 += 150

        spinningRoombaIcon = GUI("spinningRoombaIcon", 204, 630, 100, 100, self.roomba.roombaNum[0], True, True)
        self.allShopSprites.add(spinningRoombaIcon)

        self.all_sprites.add(self.buttons)




    def update(self):
        pg.display.set_caption(str(self.clock.get_fps()))
        self.all_sprites.update(self.clock.tick(FPS))
        self.leafOverlap()
        self.roombaLeafOverlap()
        self.sillyEvent()

        self.temp3+=1
        if self.temp3 >=900:
            self.saveData()
            self.temp3 = 0

        # self.mouseOverlap()
        # self.sillyEvent()



    def draw(self):
        self.window.fill(BLACK)
        self.window.blit(self.bg, (0, 0))
        if self.shopOpen:
            self.allShopSprites.draw(self.window)
            self.shopGuiText()
        else:
            if self.startscreenOpen == False:
                self.all_sprites.draw(self.window)
                self.buttons.draw(self.window)
                self.guiText()
            else:
                self.startScreenBg()
        pg.display.flip()

    def guiText(self):
        button_transparency = 100
        for button in self.buttons:
            if button.type == "topGUI":
                button.image = pg.image.load("scripts/assets/topbg.png").convert_alpha()
                thing = draw_text(self.window, self.curcurTip, BLACK,self.tipPos,5, self.regfont1, True)
                speed = int((thing[0]-thing[1])/300)
                if speed < 2:
                    speed = 2
                if speed >4:
                    speed = 4
                self.tipPos -= speed
                if thing[0] < 0:
                    self.tipPos = 1280
                    self.curcurTip = random.choice(self.curTip)
            if button.type == "bottomGUI":
                draw_text(self.window, "Current leaves: "+str(self.leafCur), BLACK, 10, 570+35,self.regfont1)
                draw_text(self.window, "Current Rake:     "+self.rake.rakeNum[4], BLACK, 10, 570+75,self.regfont1)
                draw_text(self.window, "Current Map: " + self.location[0], BLACK, 10, 570+115,self.regfont1)
            if button.type == "curRakeImg":
                button.image = pg.image.load(self.rake.rakeNum[0]).convert_alpha()
                height = button.image.get_height()
                width = button.image.get_width()
                if width > height:
                    button.image = pg.transform.scale(button.image, (tile_size[0]*11, height /(width / tile_size[0]) *11))
                else:
                    button.image = pg.transform.scale(button.image, (width / (height / tile_size[0])*11, tile_size[0]*11))
                # button.image = pg.transform.scale(button.image, (tile_size[0]*self.rake.rakeNum[2]/self.rake.rakeNum[3]*7,tile_size[1]*self.rake.rakeNum[3]/self.rake.rakeNum[2]*7))
            if button.type == "shop":
                button.image.fill((255, 255, 255, 0))
                button.image.set_alpha(0)
                draw_text(self.window, "shop", DGREEN, button.xpos - 10, button.ypos - button.height / 2,self.regfont6)
            if button.type == "prestige":
                button.image.fill((255, 255, 255, 0))
                button.image.set_alpha(0)
                draw_text(self.window, "prestige", RED, button.xpos - 10, button.ypos - button.height / 2,self.regfont6)

    def shopGuiText(self):
        for button in self.allShopSprites:
            if button.type == "spinningRakeIcon":
                if self.shopSpin1 == False:
                    self.shopSpin1 = True
                    button.spinDegree = random.randint(0,359)
                    button.spinSpeed = random.randint(1,4)
                    button.image = pg.transform.rotate(button.imageT,button.spinDegree)
                    button.curRot = 0
                button.curRot += button.spinSpeed
                button.updateImageTS(self.rake.rakeNum[0])
                button.image = pg.transform.rotate(button.imageT, button.curRot)
                button.rect.centerx = button.xpos - int(button.image.get_width()) / 2
                button.rect.centery = button.ypos - int(button.image.get_height()) / 2
            if button.type == "spinningRoombaIcon":
                if self.shopSpin2 == False:
                    self.shopSpin2 = True
                    button.spinDegree = random.randint(0,359)
                    button.spinSpeed = random.randint(1,4)
                    button.image = pg.transform.rotate(button.imageT,button.spinDegree)
                    button.curRot = 0
                button.curRot += button.spinSpeed
                button.updateImageTS(self.roomba.roombaNum[0])
                button.image = pg.transform.rotate(button.imageT, button.curRot)
                button.rect.centerx = button.xpos - int(button.image.get_width())/2
                button.rect.centery = button.ypos - int(button.image.get_height())/2
            if button.type == "mapIcon":
                if len(button.name) > 10:
                    i=0
                    for let in button.name:
                        if let == " " and i >= 8:
                            draw_text(self.window, (button.name[0:i]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 60, self.regFont5)
                            draw_text(self.window, (button.name[i:len(button.name)]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                        i += 1
                        if i >= len(button.name) - 1:
                            draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                else:
                    draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                if button.owned:
                    if button.equipped:
                        draw_text(self.window, "equipped", DGREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                    else:
                        draw_text(self.window, "equip?", GREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                else:
                    draw_text(self.window, str(button.price), YELLOW, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
            if button.type == "rakeIcon":
                if len(button.name) > 10:
                    i=0
                    for let in button.name:
                        if let == " " and i >= 7:
                            draw_text(self.window, (button.name[0:i]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 60, self.regFont5)
                            draw_text(self.window, (button.name[i:len(button.name)]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                        i += 1
                        if i >= len(button.name) - 1:
                            draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                else:
                    draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                if button.owned:
                    if button.equipped:
                        draw_text(self.window, "equipped", DGREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                    else:
                        draw_text(self.window, "equip?", GREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                else:
                    draw_text(self.window, str(button.price), YELLOW, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
            if button.type == "roombaIcon":
                if len(button.name) > 8:
                    i=0
                    for let in button.name:
                        if let == " " and i >= 7:
                            draw_text(self.window, (button.name[0:i]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 60, self.regFont5)
                            draw_text(self.window, (button.name[i:len(button.name)]), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                        i += 1
                        if i >= len(button.name) - 1:
                            draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                            break
                else:
                    draw_text(self.window, (button.name), BLACK, button.xpos - button.width / 2 - 10,button.ypos - 50, self.regFont5)
                if button.owned:
                    if button.equipped:
                        draw_text(self.window, "equipped", DGREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                    else:
                        draw_text(self.window, "equip?", GREEN, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)
                else:
                    draw_text(self.window, str(button.price), YELLOW, button.xpos - button.width / 2 +10, button.ypos + 37, self.regFont4)




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
                if shopButton:
                    if button.owned:
                        if buttonCategory == "rake":
                            for i in range(0, len(rakeA)):
                                rakeA[i][6] = True
                                rakeA[i][9] = False
                                button.equipped = False
                                if rakeA[i][4] == button.name:
                                    self.rake.loadNewRake(i)
                                    rakeA[i][9] = True
                                    rakeA[i][6] = True
                                    for buttona in self.shopButtons:
                                        if buttona.type == "rakeIcon":
                                            buttona.equipped = False
                                    button.equipped = True
                                    break
                        elif buttonCategory == "map":
                            for i in range(0, len(self.locations)):
                                self.locations[i][8] = True
                                self.locations[i][10] = False
                                button.equipped = False
                                if self.locations[i][0] == button.name:
                                    self.load_map(i)
                                    self.locations[i][10] = True
                                    self.locations[i][8] = True
                                    for buttona in self.shopButtons:
                                        if buttona.type == "mapIcon":
                                            buttona.equipped = False
                                    button.equipped = True
                                    break

                        elif buttonCategory == "roomba":
                            for i in range(0, len(roombaA)):
                                roombaA[i][5] = True
                                roombaA[i][9] = False
                                button.equipped = False
                                if roombaA[i][3] == button.name:
                                    self.roomba.loadNewRoomba(i)
                                    roombaA[i][9] = True
                                    roombaA[i][5] = True
                                    for buttona in self.shopButtons:
                                        if buttona.type == "roombaIcon":
                                            buttona.equipped = False
                                    button.equipped = True
                                    break
                    else:
                        if self.leafCur >= button.price:
                            self.leafCur -= button.price
                            button.owned = True
                            if buttonCategory == "rake":
                                for i in range(0, len(rakeA)):
                                    rakeA[i][9] = False
                                    button.equipped = False
                                    if rakeA[i][4] == button.name:
                                        self.rake.loadNewRake(i)
                                        rakeA[i][9] = True
                                        rakeA[i][6] = True
                                        for buttona in self.shopButtons:
                                            if buttona.type == "rakeIcon":
                                                buttona.equipped = False
                                        button.equipped = True
                                        break
                            elif buttonCategory == "map":
                                for i in range(0, len(self.locations)):
                                    self.locations[i][10] = False
                                    button.equipped = False
                                    if self.locations[i][0] == button.name:
                                        self.load_map(i)
                                        self.locations[i][10] = True
                                        self.locations[i][8] = True
                                        for buttona in self.shopButtons:
                                            if buttona.type == "mapIcon":
                                                buttona.equipped = False
                                        button.equipped = True
                                        break
                            elif buttonCategory == "roomba":
                                for i in range(0, len(roombaA)):
                                    roombaA[i][9] = False
                                    button.equipped = False
                                    if roombaA[i][3] == button.name:
                                        self.roomba.loadNewRoomba(i)
                                        roombaA[i][9] = True
                                        roombaA[i][5] = True
                                        for buttona in self.shopButtons:
                                            if buttona.type == "roombaIcon":
                                                buttona.equipped = False
                                        button.equipped = True
                                        break


                        else:
                            print("not enough money")
                else:
                    return button.type

    def saveData(self):
        string1 = ""
        for location in self.locations:
            if location[8]:
                string1+="1"
            else:
                string1+="0"
        string2 = ""
        for location in rakeA:
            # print(location)
            if location[6]:
                string2+="1"
            else:
                string2+="0"
        string3 = ""
        for location in roombaA:
            if location[5]:
                string3+="1"
            else:
                string3+="0"

        fileWrite = open("scripts/playerData.txt", "w")
        # print(string1,string2,string3)
        fileWrite.write("# currency, map, rake, roomba\n"+str(self.leafCur)+"\n"+str(string1)+"\n"+str(string2)+"\n"+str(string3))
        fileWrite.close() # hopefully this works


    def leafOverlap(self):
        # self.player.rect.centerx
        # hits = pg.sprite.spritecollideany(self.rake,self.leaves)
        # if hits !=None:
        #     hits.pushed(self.player.velX,self.player.velY)
        for leaf in self.leaves:
            if self.rake.rect.left < leaf.rect.right:
                if self.rake.rect.right > leaf.rect.left:
                    if self.rake.rect.top < leaf.rect.bottom:
                        if self.rake.rect.bottom > leaf.rect.top:
                            leaf.pushed(self.player.velX,self.player.velY)
            if self.roomba.rect.left < leaf.rect.right:
                if self.roomba.rect.right > leaf.rect.left:
                    if self.roomba.rect.top < leaf.rect.bottom:
                        if self.roomba.rect.bottom > leaf.rect.top:
                            leaf.roombaPushed(self.roomba.speedXfr,self.roomba.speedYfr)

    def roombaLeafOverlap(self):
        # self.player.rect.centerx
        # for leaf in self.leaves:
        #     if self.roomba.rect.left < leaf.rect.right:
        #         if self.roomba.rect.right > leaf.rect.left:
        #             if self.roomba.rect.top < leaf.rect.bottom:
        #                 if self.roomba.rect.bottom > leaf.rect.top:
        #                     leaf.roombaPushed(self.roomba.speedXfr,self.roomba.speedYfr)
        pass



    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.startscreenOpen:
                    self.startscreenOpen = False
                    self.rake.rakeNum[9] = False
                    self.roomba.roombaNum[9] = True
                    self.location[10] = False
                    self.player.kill()
                    self.rake.kill()
                    self.roomba.kill()
                    for leaf in self.leaves:
                        leaf.kill()
                    self.prepGame(0, 0, 0)
                    self.createGUIS()
                else:
                    if self.shopOpen:
                        overlap = self.mouseOverlap(self.shopButtons)
                        if overlap == "shopClose":
                            self.shopOpen = False
                        elif overlap == "rakeIcon":
                            self.mouseOverlap(self.shopButtons, True, "rake")
                        elif overlap == "roombaIcon":
                            self.mouseOverlap(self.shopButtons, True, "roomba")
                        elif overlap == "mapIcon":
                            self.mouseOverlap(self.shopButtons, True, "map")
                        else:
                            print(overlap)
                        self.saveData()
                    else:
                        overlap = self.mouseOverlap(self.clickable)
                        if overlap == "shop":
                            self.shopOpen = True
                        elif overlap == "prestige":
                            print("prestige")
                        else:
                            print(overlap)

    def startScreenBg(self):
        self.temp2+=3
        if self.temp2 >= 600:
            # map, rake, roomba
            try:
                self.player.kill()
                self.rake.kill()
                self.roomba.kill()
                for leaf in self.leaves:
                    leaf.kill()
            except:
                pass
            # map rake roomba
            self.prepGame(random.randint(0,5),random.randint(0,5),random.randint(0,5))
            self.temp2 = random.randint(-600,0)
        try:
            self.window.fill(BLACK)
            self.window.blit(self.bg, (0, 0))
            self.leaves.draw(self.window)
            self.main_sprites.draw(self.window)
            image = pg.Surface((WIDTH,HEIGHT), pg.SRCALPHA)
            image.fill((0,0,0,100))
            self.window.blit(image, (0, 0))
        except:
            pass
        dark = pg.Surface((WIDTH,HEIGHT))
        dark.fill(BLACK)
        dark.set_alpha(40)
        self.window.blit(dark, (WIDTH / 2 - dark.get_width() / 2, HEIGHT / 2 - dark.get_height() / 2))
        try:
            draw_text_center(self.window, "LEAF RAKING SIMULATOR!", WHITE, WIDTH / 2, HEIGHT / 2,
                             self.regFont2)
            draw_text(self.window, "v1.00", RED, WIDTH / 1.22, HEIGHT / 2,
                             self.regFont3)
            draw_text_center(self.window, "click anywhere to start!", WHITE, WIDTH / 2, HEIGHT / 1.73,
                             self.regFont3)
        except:
            pass

    def end_screen(self):
        return "quit"