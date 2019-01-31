import math
import pygame
from gameController import GameController
from camera import Camera
from hud import HUD
from menu import Menu
from gameObject import GameObject
from trigger import Trigger
from terrain import Block, Brick, Wall, Sky, Ground, Door
from character import Character
from npc import NPC, Gaurd
from player import Player
from item import Item

#an object which contains the entire game (singleton style)
class NinjaGame:
    """ A python singleton """

    #The single instance class implementation
    class __impl:
        """This implementation hides the singleton interface\
        in an inner class and creates exactly one instance of\
        the inner class. The outer class is a handle to the inner\
        class and delegates any requests to it. While the id() of\
        the handle objects changes, the id() of the inner class which\
        implements the singleton behaviour is constant."""
        
#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

        #reference to our game singletons
        __game = GameController()
        __camera = Camera()
        __hud = HUD()

        #reference to game timers
        timers = {}

#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

        #get the game controller instance
        def getGame(this):
            return this.__game

        #get the camera instance
        def getCamera(this):
            return this.__camera

        #get the hud instance
        def getHud(this):
            return this.__hud

#------------------------------------------------------------------------------#
#                                  Mutators                                    #
#------------------------------------------------------------------------------#

        #no mutators in here
             
#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#                               Initilization                                  #
#------------------------------------------------------------------------------#

        #Initlize our single instance
        def __init__(this):
            #Ninja Game constructor methods
            this.initGame()
            this.runGame()

        #loads any pygame functions or objects before the user gets a chance to act
        def initGame(this):
            #initilize pygame's sound component
            #frequency, size, channels, buffersize
            pygame.mixer.pre_init(44100, 16, 2, 4096) 
            #boot up pygame and print boot info
            message = pygame.init()
            print("Successes, Failures\n", message)
            #set the resolution of the game display
            this.getGame().setDisplay(pygame.display.set_mode(this.getGame().getResolution()))
            #set the name of the game
            pygame.display.set_caption(this.getGame().getGameName())
            this.getGame().setTimer(this, "quitTimer", 10)
            this.getGame().setTimer(this, "spaceTimer", 5)


#------------------------------------------------------------------------------#
#                              Game Processes                                  #
#------------------------------------------------------------------------------#

        def runGame(this):
            #the game loop to keep the game running
            while this.getGame().getGameRunning():
                #If we are in the menu
                if this.getGame().getAtMainMenu():
                    this.runMainMenu()
                #If we are in the options menu
                elif this.getGame().getAtOptionsMenu():
                    this.runOptionsMenu()
                #If we are in the game...
                elif this.getGame().getAtGame():
                    this.startGameplay()

            #if we manage to break out of the loop without quitting...
            #automatically call the quit method
            this.quitGame()


        #this is where the actual game gets played
        def startGameplay(this):
            pygame.mixer.music.load('sounds/music/level.wav')
            pygame.mixer.music.play(-1)
            #load the map and all of the objects
            this.loadMap()
            this.getHud().initGameHUD()
            #reset the game over flag so this does not repeat
            this.getGame().setGameOver(False)
            this.getGame().setVictory(False)
            this.getGame().setGameOverPlayed(False)
            
            #------------------ Game Loop Begin -------------------
            
            #setup the event timer so that the game does not freeze by itself
            #set the event ID to be Uservent + 1 (25)
            timer_event = pygame.USEREVENT +1
            #set up the timer event to occur every set of miliseconds determined by the second argument
            pygame.time.set_timer(timer_event, 1)
            
            #while we are considered in the game
            while(this.getGame().getAtGame()):
                
                #------------ Event Processes ------------
                #check to see if the player has a game over and if has been played yet
                if this.getGame().getGameOver()\
                   and not this.getGame().getGameOverPlayed():
                    #use the game over method if this is the case
                    this.gameOver()

                #checks to see if the player is trying to use input and assigns the action
                #takes the pygame event argument that was created from the for loop
                command = this.processInput()

                #as long as the game isnt over...
                #player selects the new action and the player procces it
                if not this.getGame().getGameOver():
                    this.getGame().getPlayer().recieveCommand(command)
                else:
                    this.getGame().getPlayer().recieveCommand("idle")

                #AI selects the new action and the AI processes it
                this.checkAIStates(this.getGame().getNPCSprites())

                #check to see if all characters are in the middle of an action
                #finishes the action if the chracters are in the middle of one
                this.checkStates(this.getGame().getNPCSprites())
                this.checkStates(this.getGame().getPlayer())

                #add forces (including gravity) to all object lists, then the player
                this.addForces(this.getGame().getTerrainSprites())
                this.addForces(this.getGame().getItemSprites())
                this.addForces(this.getGame().getNPCSprites())
                this.addForces(this.getGame().getPlayer())

                #check to see if any triggers have been activated
                this.checkTriggers()

                #---------- Camera Update ----------------

                #check to see if the camera needs to move
                this.getCamera().checkMove()

                #update the position of all sprites according to how the camera is shifting
                this.getCamera().update(this.getGame().getTerrainSprites())
                this.getCamera().update(this.getGame().getItemSprites())
                this.getCamera().update(this.getGame().getNPCSprites())
                this.getCamera().update(this.getGame().getTriggerSprites())
                this.getCamera().update(this.getHud().getMovingHUDSprites())

                """
                #update the position of all sprite buffers
                this.getCamera().update(this.getGame().terrainSpriteBuffer)
                this.getCamera().update(this.getGame().itemSpriteBuffer)
                this.getCamera().update(this.getGame().NPCSpriteBuffer)
                this.getCamera().update(this.getGame().triggerSpriteBuffer)
                """

                this.getCamera().update(this.getGame().getPlayer())                

                #----------- Graphics Rendering -----------

                #run the render graphics method
                this.renderGraphics()

                #----------- Graphics Update Process --------------

                #updates all sprites to their proper positions
                this.getGame().getTerrainSprites().update()
                this.getGame().getItemSprites().update()
                this.getGame().getNPCSprites().update()
                this.getGame().getTriggerSprites().update()
                this.getGame().getPlayer().update()
                this.getHud().getHUDSprites().update()
                                     
                #update the display outside of the update loop to reflect any changes
                pygame.display.update()

                """
                buffering methods to be added in at a later date
                #---------- Appearing and Vanishing ----------
                
                #a method that removes all sprites out of view
                this.vanish(this.getGame().getTerrainSprites())
                this.vanish(this.getGame().getItemSprites())
                this.vanish(this.getGame().getNPCSprites())
                this.vanish(this.getGame().getTriggerSprites())
                this.vanish(this.getHud().getMovingHUDSprites())

                this.appear(this.getGame().terrainSpriteBuffer)
                this.appear(this.getGame().itemSpriteBuffer)
                this.appear(this.getGame().NPCSpriteBuffer)
                this.appear(this.getGame().triggerSpriteBuffer)
                """
                #---------- Game Timers ----------------

                this.getGame().countdownTimers(this)

                #---------- Update Process ---------------
                    
                #update frames per second outside fo the update loop and set the delta time to the variable
                this.getGame().deltaTime = (this.getGame().clock.tick(this.getGame().gameFPS) / 4)

                #ensure the pygame event system is still working properly
                pygame.event.pump()


                    
            #-------------------- Game Loop End ------------------------


        def loadMap(this):
            this.loadMapLayer('map1/', 'terrain.txt', "terrain")
            this.loadMapLayer('map1/', 'character.txt', "character")
            this.loadMapLayer('map1/', 'item.txt', "item")
            this.loadMapLayer('map1/', 'triggers.txt', "trigger")

        def loadMapLayer(this, mapPath, filename, objectType):
            path1 = 'maps/'
            filepath = path1 + mapPath + filename
            mapfile = open(filepath, 'r')
            idxX = 0
            idxY = 1
            
            #loop through the map file to find the dimmensions of the map
            with open(filepath, 'r') as mapfile:
                while True:
                    block = mapfile.read(1)
                    if not block:
                        break
                    elif block == '\n':
                        idxY += 1
                        idxX = 0
                    else:
                        idxX += 1
            mapfile.close()
            
            #reset the coordinate index values
            idxX = 0
            idxY = 0
            #loop through the map file to turn the character array into an objects array
            with open(filepath, 'r') as mapfile:
                while True:
                    block = mapfile.read(1)
                    if not block:
                        break
                    elif block == '\n':
                        idxY += 1
                        idxX = 0
                    else:
                        this.loadObject(block, objectType, idxX, idxY)
                        idxX += 1
            mapfile.close()

        def loadObject(this, block, objectType, idxX, idxY):
            blockScale = this.getGame().getBlockScale()
            tBuffer = this.getGame().terrainSpriteBuffer
            iBuffer = this.getGame().itemSpriteBuffer
            nBuffer = this.getGame().NPCSpriteBuffer
            
            if objectType == "terrain":
                #match the character with the object and add it to the map array
                if block == 'b':
                    tBuffer[str(idxX) + "," + str(idxY)] = Brick((idxX * blockScale), (idxY * blockScale))
                elif block == 'w':
                    tBuffer[str(idxX) + "," + str(idxY)] = Wall((idxX * blockScale), (idxY * blockScale))
                elif block == 's':
                    tBuffer[str(idxX) + "," + str(idxY)] = Sky((idxX * blockScale), (idxY * blockScale))
                elif block == 'd':
                    tBuffer[str(idxX) + "," + str(idxY)] = Door((idxX * blockScale), (idxY * blockScale))
                elif block == 'g':
                    tBuffer[str(idxX) + "," + str(idxY)] = Ground((idxX * blockScale), (idxY * blockScale))
            #if it is a character type object
            elif objectType == "character":
                #match the character with the object and add it to the map array
                if block == 'r':
                    nBuffer[str(idxX) + "," + str(idxY)] = Gaurd("Standing Gaurd", (idxX * blockScale), (idxY * blockScale))
                elif block == 'p':
                    Player((idxX * blockScale), (idxY * blockScale))
            #if it is an item type object
            elif objectType == "item":
                pass
            #if it is a trigger type object
            elif objectType == "trigger":
                #match the character with the object and add it to the map array
                if block == 'm':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("howToMoveMessage", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
                elif block == 'a':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("howToAttackMessage", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
                elif block == 'e':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("enemyInfoMessage", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
                elif block == 'r':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("enemyBroadcastMessage", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
                elif block == 'v':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("victory", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
                elif block == 'c':
                    tBuffer[str(idxX) + "," + str(idxY)] = Trigger("clearMessages", (idxX * blockScale), (idxY * blockScale), blockScale, (blockScale * 2))
            
        def renderGraphics(this):
            """ The way this works, is that it builds the display
            in layers based on what comes first and the last thing
            that gets drawn is the sprite/shape on the bottom of the
            graphics rendering code block """
            
            #wipe the slate clean
            this.getGame().getDisplay().fill(this.getGame().getColor("black"))

            #add all sprites to the game display
            this.getGame().getTerrainSprites().draw(this.getGame().getDisplay())
            this.getGame().getItemSprites().draw(this.getGame().getDisplay())
            this.customDraw(this.getGame().getNPCSprites())
            this.customDraw(this.getGame().getPlayer())
            this.getHud().getHUDSprites().draw(this.getGame().getDisplay())

        #function for using the custome draw function for a sprite group
        def customDraw(this, sObject):
            #if the object instance is a single sprite
            if isinstance(sObject, pygame.sprite.Sprite):
                #use the custom-made draw function
                sObject.draw(this.getGame().getDisplay())

            #if the object instance is a sprite group
            if isinstance(sObject, pygame.sprite.Group):
                #loop through the sprite group
                for sprite in sObject:
                    #use the custom-made draw function
                    sprite.draw(this.getGame().getDisplay())
        """
        functions to be added in at a later date

        def vanish(this, spriteGroup):
            block = this.getGame().getBlockScale()
            vanishRect = pygame.Rect((0,0),(this.getGame().getResolution()))
            #expand the rect to account for the loading buffer
            vanishRect.inflate_ip(block * this.getGame().loadingBuffer,\
                                block * this.getGame().loadingBuffer)
            
            #loop through the sprite group
            for sprite in spriteGroup:
                #if the sprite is not within the load rect...
                if not vanishRect.contains(sprite.getRect()):
                    #remove the sprite
                    sprite.remove()

        def appear(this, spriteList):
            block = this.getGame().getBlockScale()
            vanishRect = pygame.Rect((0,0),(this.getGame().getResolution()))
            #expand the rect to account for the loading buffer
            loadRect = vanishRect.inflate(block * (this.getGame().loadingBuffer + 2),\
                                block * (this.getGame().loadingBuffer + 2))
            #expand the vanishing buffer
            vanishRect.inflate_ip(block * (this.getGame().loadingBuffer + 2),\
                                block * (this.getGame().loadingBuffer))

            #loop through each sprite in the sprite buffer
            for key, value in spriteList.items():
                #if the sprite is not within the vanish rect
                #but is within the load rect....
                if not vanishRect.contains(value.getRect())\
                   and loadRect.contains(value.getRect()):
                    #ensure the item gets added to the correct list
                    if isinstance(value, Block):
                        this.getGame().getTerrainSprites().add(value)
                    elif isinstance(value, Item):
                        this.getGame().getItemSprites().add(value)
                    elif isinstance(value, NPC):
                        this.getGame().getNPCSprites().add(value)                        
                    elif isinstance(value, Trigger):
                        this.getGame().getTriggerSprites().add(value)
        """
        
        def processInput(this):
            """Will go back and change jump to a MOD key to try to fix jumping issue"""

            #assign the reference to the game keys list
            keys = this.getGame().keys
            mods = pygame.key.get_mods()

            #keysPressed = this.getGame().noKeysPressed
            keysPressed = pygame.key.get_pressed()

            #reset all the keys that are pressed
            for idx in range(0,len(keys)):
                keys[idx] = False

            #if the keys that are pressed = the boolean tuple                
            if keysPressed == this.getGame().wPressed:
                keys[0] = True
            elif keysPressed == this.getGame().sPressed:
                keys[1] = True            
            elif keysPressed == this.getGame().aPressed:
                keys[2] = True
            elif keysPressed == this.getGame().dPressed:
                keys[3] = True
            elif keysPressed == this.getGame().upPressed:
                keys[4] = True
            elif keysPressed == this.getGame().downPressed:
                keys[5] = True
            elif keysPressed == this.getGame().leftPressed:
                keys[6] = True
            elif keysPressed == this.getGame().rightPressed:
                keys[7] = True
            elif keysPressed == this.getGame().spacePressed:
                keys[8] = True
            elif keysPressed == this.getGame().escPressed:
                keys[9] = True

            #if the mods are pressed = one number for a specific key
            if mods == this.getGame().rCtrlPressed:
                keys[10] = True
            
            #print(keysPressed)
            #print(keys)
            #print (mods)

            if keysPressed == this.getGame().noKeysPressed:
                return "idle"
            #return a command based on which keys are pressed
            if keys[8]:
                if this.getGame().checkTimer(this, "spaceTimer"):
                    #ensure we dont press the button twice
                    this.getGame().setTimer(this, "spaceTimer", 5)
                    return "jump"
            elif keys[9]:
                if this.getGame().checkTimer(this, "quitTimer"):
                    if not this.getGame().getAtMainMenu():
                        this.quitLevel()
                        #ensure we dont press the button twice
                        this.getGame().setTimer(this, "quitTimer", 10)
                    else:
                        return this.quitGame()
            elif keys[10]:
                return "attack"
            elif keys[0] or keys[4]:
                return "goUp"
            elif keys[1] or keys[5]:
                return "goDown"
            elif keys[2] or keys[6]:
                return "goLeft"
            elif keys[3] or keys[7]:
                return "goRight"
            
            #if no actions are being taken or no keys are being pressed... return idle
            return "idle"

        #function for using the check AI state function for a group of sprites
        def checkAIStates(this, sObject):
            #loop through the sprite group
            for sprite in sObject:
                #use the checkState function
                sprite.checkAIState()

        #function for using the check state function for a sprite or group
        def checkStates(this, sObject):
            #if the object instance is a single sprite
            if isinstance(sObject, pygame.sprite.Sprite):
                #use the checkState function
                sObject.checkState()

            #if the object instance is a sprite group
            if isinstance(sObject, pygame.sprite.Group):
                #loop through the sprite group
                for sprite in sObject:
                    #use the checkState function
                    sprite.checkState()

        
        #add gravity to an object array or just the player
        def addForces(this, sObject):

            #if the object instance is a single sprite
            if isinstance(sObject, pygame.sprite.Sprite):
                #add force to a single object
                this.addSingleForce(sObject)

            #if the object instance is a sprite group
            elif isinstance(sObject, pygame.sprite.Group):
                #loop through the sprite group
                for sprite in sObject:
                    #add force to a single object
                    this.addSingleForce(sprite)
                    

        def addSingleForce(this, sObject):
            #if the object instance is a character or NPC sprite
            if isinstance(sObject, Character)\
               or isinstance(sObject, NPC):
                #have gravity affect the object if they are in the air
                if sObject.mass > 0:
                    sObject.addForce(0, (this.getGame().gravity / 2))
                    
                #implement speed loss over time
                if sObject.getState("isIdle"):
                    if not sObject.speedX == 0:
                        if sObject.speedX > 0:
                            sObject.addForce(-this.getGame().speedLoss,0)
                        elif sObject.speedX < 0:
                            sObject.addForce(this.getGame().speedLoss,0)
                        #if there is less than 1 unit of force
                        if abs(sObject.speedX) < 1:
                            #set the speed to 0
                            sObject.speedX = 0
                            
                # if the object is in the middle of moving left or right...
                if sObject.speedX > 0 or sObject.speedX < 0:
                    #move the object and see if they collides with another object
                    if not sObject.move(sObject.speedX * this.getGame().deltaTime ,0):
                        if not sObject.getState("isJumping"):
                            #if they collide, then set the x speed to 0
                            sObject.speedX = 0
                
                #if the object is in the air
                if sObject.speedY > 0 or sObject.speedY < 0:
                    #move the object and see if he collides with another object
                    if not sObject.move(0,(sObject.speedY * this.getGame().deltaTime)):
                        #if they collides, set the y speed to 0
                        sObject.speedY = 0
                        
            #if the object is not a character sprite
            else:
                #if the object has mass
                if sObject.mass > 0:
                    #make the object fall
                    sObject.move(0,(this.getGame().deltaTime / 2) * this.getGame().gravity)

        def checkTriggers(this):
            #loop through each trigger
            for trigger in this.getGame().getTriggerSprites():
                #check to see if the trigger is colliding with the player
                if this.getGame().getPlayer().getRect().colliderect(trigger.getRect()):
                    #trigger the event
                    trigger.event()
                    
            #countdown the timers on the triggers
            Trigger.game.countdownTimers(Trigger)

        #a method to run if the player has a game over
        def gameOver(this):
            #if it is not a victorious game over
            if not this.getGame().getVictory():
                pygame.mixer.music.load('sounds/music/gameOver.wav')
                pygame.mixer.music.play(-1)
                #remove any text box elements (if there is any)
                this.getHud().removeTextBox()
                #Create a text box with a message
                this.getHud().createBoxWithMessage(  "*-----------------------------------------------*"\
                                                    +"|     _____                 ____                |"\
                                                    +"|    / ___/__ ___ _  ___   / __ \_  _____ ____  |"\
                                                    +"|   / (_ / _ `/  ` \/ -_) / /_/ / |/ / -_) __/  |"\
                                                    +"|   \___/\_,_/_/_/_/\__/  \____/|___/\__/_/     |"\
                                                    +"|                                               |"\
                                                    +"|                                               |"\
                                                    +"|   Press ESC key to go back to the main menu   |"\
                                                    +"*-----------------------------------------------*",\
                           this.getHud().getTextBoxLocX(), this.getHud().getTextBoxLocY(),\
                           this.getHud().getTextBoxSizeX(), this.getHud().getTextBoxSizeY() + 2,\
                           False)
            #if it is a victorious game over
            elif this.getGame().getVictory():
                pygame.mixer.music.load('sounds/music/victory.wav')
                pygame.mixer.music.play(-1)
                #remove any text box elements (if there is any)
                this.getHud().removeTextBox()
                #Create a text box with a message
                this.getHud().createBoxWithMessage("   _    ___      __                     "\
                                                  +"  | |  / (_)____/ /_____  _______  __   "\
                                                  +"  | | / / / ___/ __/ __ \/ ___/ / / /   "\
                                                  +"  | |/ / / /__/ /_/ /_/ / /  / /_/ /    "\
                                                  +"  |___/_/\___/\__/\____/_/   \__, /     "\
                                                  +"                            /____/      "\
                                                  +"                                        "\
                                                  +"                                        "\
                                                  +"  Press ESC to return to the main menu  ",\
                                                   128,212,43,13, False)
            #reset the game over flag so this does not repeat
            this.getGame().setGameOverPlayed(True)
            
    #----------------------------- Main Menu Method -------------------------


        def runMainMenu(this):
            pygame.mixer.music.load('sounds/music/title.wav')
            pygame.mixer.music.play(-1)
            #Create a main menu and while bool to store selection
            this.getHud().createBoxWithMessage("*-----------------------------------------------------*"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|               P r e s s     S P A C E               |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|         S  T  A  R  T          G  A  M  E           |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"*-----------------------------------------------------*",\
                                               8,8,58,18, False)
            this.getHud().createBoxWithMessage("*-----------------------------------------------------*"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|            Q  U  I  T          G  A  M  E           |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"|                P r e s s    E S C                   |"\
                                              +"|                                                     |"\
                                              +"|                                                     |"\
                                              +"*-----------------------------------------------------*",\
                                               8,328,58,18, False)
            this.getHud().createBoxWithMessage("        ______   _           __   _     "\
                                              +"       / __/ /  (_)__  ___  / /  (_)    "\
                                              +"      _\ \/ _ \/ / _ \/ _ \/ _ \/ /     "\
                                              +"     /___/_//_/_/_//_/\___/_.__/_/      "\
                                              +"                                        "\
                                              +"     ___                        _       "\
                                              +"    / _ | ___ ___ ___ ____ ___ (_)__    "\
                                              +"   / __ |(_-<(_-</ _ `(_-<(_-</ / _ \   "\
                                              +"  /_/ |_/___/___/\_,_/___/___/_/_//_/   ",\
                                               128,212,43,13, False)
            mainMenu = Menu("Main")
            mainMenu.addMenuItem("Start", this.getGame().imgBlank, 0,0,960,320)
            #mainMenu.addMenuItem("Start", this.getGame().startImage, 0,0,480,320)
            #mainMenu.addMenuItem("Options", this.getGame().optionsImage, 480,0,480,320)
            mainMenu.addMenuItem("Quit", this.getGame().imgBlank, 0,320,960,320)
            
            #------------------ Main Menu Loop Begin -------------------
            
            #while we are considered in the main menu
            while(this.getGame().getAtMainMenu()):
                #for event in pygame.event.get():

                #------------ Event Processes ------------
                
                #a method that checks to see if a menu item get pressed
                #and assigns the process name to a process variable
                #process = mainMenu.selectOption(this.getGame().getDisplay(), event)

                process = this.processInput()

                this.runSelectedProcess(process)
                #----------- Graphics Rendering -----------

                """ The way this works, is that it builds the display
                in layers based on what comes first and the last thing
                that gets drawn is the sprite/shape on the bottom of the
                graphics rendering code block """
                    
                #draw the HUD sprites on the screen
                this.getHud().getHUDSprites().update()

                #run the render graphics method
                this.renderGraphics()
                
                #update the screen
                pygame.display.update()

                #Run the display menu items method
                #mainMenu.displayMenuItems(this.getGame().getDisplay())

                #------------ Game Timers ----------------

                this.getGame().countdownTimers(this)
                
                #----------- Update Process --------------
                                     
                #update the display outside of the event loop to reflect any changes
                pygame.display.update()

                #update frames per second outside fo the update loop and set the delta time to the variable
                this.getGame().deltaTime = (this.getGame().clock.tick(this.getGame().gameFPS) / 4)

                #ensure the pygame event system is still working properly
                pygame.event.pump()

                    
            #-------------------- Main Menu Loop End ------------------------

        def runOptionsMenu(this):
            print("You are in the options menu, nothing here yet...")
            this.runSelectedProcess("Main Menu")

        def runSelectedProcess(this, process):     
            if process == "jump":
                print("Starting Start Process...")
                this.getGame().setAtMainMenu(False)
                this.getGame().setAtOptionsMenu(False)
                this.getGame().setAtGame(True)
                
            elif process == "Main Menu":
                print("Returning to the Main Menu...")
                this.getGame().setAtMainMenu(True)
                this.getGame().setAtOptionsMenu(False)
                this.getGame().setAtGame(False)
            
            elif process == "Options":
                print("Starting Options Process...")
                this.getGame().setAtMainMenu(False)
                this.getGame().setAtOptionsMenu(True)
                this.getGame().setAtGame(False)
            
            elif process == "Quit":
                print("Continuing Quit Process...")
                this.getGame().setGameRunning(False)
                this.getGame().setAtMainMenu(False)
                this.getGame().setAtOptionsMenu(False)
                this.getGame().setAtGame(False)
                this.quitGame()
            
            elif process == "Invalid":
                print("You have selected an invalid proceess... please try again")
                
            else:
                pass

        def quitLevel(this):
            #Clear out all sprite groups
            this.getGame().getTerrainSprites().empty()
            this.getGame().getItemSprites().empty()
            this.getGame().getNPCSprites().empty()
            this.getGame().getTriggerSprites().empty()
            this.getHud().getHUDSprites().empty()
            #Remove the player
            this.getGame().getPlayer().kill()
            #reset the camera
            this.getCamera().reset()
            #reset the game over flag
            this.getGame().setGameOver(False)
            #reset the victory flag
            this.getGame().setVictory(False)
            #remove the game over text Box
            this.getHud().removeTextBox()
            #run the main menu process
            this.runSelectedProcess("Main Menu")

        def quitGame(this):
            pygame.quit()
            quit()



#-----------------------Rest of the outer class---------------------------------------

    # storage for the instance reference
    __instance = None

    #Create Singleton Instance
    def __init__(this):
        # Check whether we already have an instance
        if NinjaGame.__instance is None:
            
            # Create and remember instance
            NinjaGame.__instance = NinjaGame.__impl()
            
        # Store instance reference as the only member in the handle
        this.__dict__['_NinjaGame__instance'] = NinjaGame.__instance

    def __getattr__(this, attr):
        """ Delegate access to implementation """
        return getattr(this.__instance, attr)

    def __setattr__(this, attr, value):
        """ Delegate access to implementation """
        return setattr(this.__instance, attr, value)

    



