import pygame
from character import Character
from hud import HUD


#Object class that derives from a character in the game to represent the player
class Player(Character):

    def __init__(this, posX, posY):
        super().__init__("Player", this.game.playerImage, posX, posY,\
                         this.game.getBlockScale() * 1, this.game.getBlockScale() * 2, 1, 1)

        #initilize the player
        this.init()
        

#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

    #player images
    imgIdle = [pygame.image.load("sprites/characters/peasant/tile000.png"),\
                    pygame.image.load("sprites/characters/peasant/tile001.png"),\
                    pygame.image.load("sprites/characters/peasant/tile002.png"),\
                    pygame.image.load("sprites/characters/peasant/tile003.png"),\
                    pygame.image.load("sprites/characters/peasant/tile004.png"),\
                    pygame.image.load("sprites/characters/peasant/tile005.png"),\
                    pygame.image.load("sprites/characters/peasant/tile006.png"),\
                    pygame.image.load("sprites/characters/peasant/tile007.png"),\
                    pygame.image.load("sprites/characters/peasant/tile008.png"),\
                    pygame.image.load("sprites/characters/peasant/tile009.png")]
    imgUse = [pygame.image.load("sprites/characters/peasant/tile010.png"),\
                   pygame.image.load("sprites/characters/peasant/tile011.png"),\
                   pygame.image.load("sprites/characters/peasant/tile012.png"),\
                   pygame.image.load("sprites/characters/peasant/tile013.png"),\
                   pygame.image.load("sprites/characters/peasant/tile014.png"),\
                   pygame.image.load("sprites/characters/peasant/tile015.png"),\
                   pygame.image.load("sprites/characters/peasant/tile016.png"),\
                   pygame.image.load("sprites/characters/peasant/tile017.png"),\
                   pygame.image.load("sprites/characters/peasant/tile018.png"),\
                   pygame.image.load("sprites/characters/peasant/tile019.png")]
    imgRun = [pygame.image.load("sprites/characters/peasant/tile020.png"),\
                    pygame.image.load("sprites/characters/peasant/tile021.png"),\
                    pygame.image.load("sprites/characters/peasant/tile022.png"),\
                    pygame.image.load("sprites/characters/peasant/tile023.png"),\
                    pygame.image.load("sprites/characters/peasant/tile024.png"),\
                    pygame.image.load("sprites/characters/peasant/tile025.png"),\
                    pygame.image.load("sprites/characters/peasant/tile026.png"),\
                    pygame.image.load("sprites/characters/peasant/tile027.png"),\
                    pygame.image.load("sprites/characters/peasant/tile028.png"),\
                    pygame.image.load("sprites/characters/peasant/tile029.png")]
    imgAttack = [pygame.image.load("sprites/characters/peasant/tile030.png"),\
                      pygame.image.load("sprites/characters/peasant/tile031.png"),\
                      pygame.image.load("sprites/characters/peasant/tile032.png"),\
                      pygame.image.load("sprites/characters/peasant/tile033.png"),\
                      pygame.image.load("sprites/characters/peasant/tile034.png"),\
                      pygame.image.load("sprites/characters/peasant/tile035.png"),\
                      pygame.image.load("sprites/characters/peasant/tile036.png"),\
                      pygame.image.load("sprites/characters/peasant/tile037.png"),\
                      pygame.image.load("sprites/characters/peasant/tile038.png"),\
                      pygame.image.load("sprites/characters/peasant/tile039.png")]
    imgDeath = [pygame.image.load("sprites/characters/peasant/tile040.png"),\
                     pygame.image.load("sprites/characters/peasant/tile041.png"),\
                     pygame.image.load("sprites/characters/peasant/tile042.png"),\
                     pygame.image.load("sprites/characters/peasant/tile043.png"),\
                     pygame.image.load("sprites/characters/peasant/tile044.png"),\
                     pygame.image.load("sprites/characters/peasant/tile045.png"),\
                     pygame.image.load("sprites/characters/peasant/tile046.png"),\
                     pygame.image.load("sprites/characters/peasant/tile047.png"),\
                     pygame.image.load("sprites/characters/peasant/tile048.png"),\
                     pygame.image.load("sprites/characters/peasant/tile049.png")]
    imgBlank = pygame.image.load("sprites/characters/peasant/blank.png")


    #Hud Reference
    __hud = HUD()

#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

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

    #initilize the player
    def init(this):
        this.setCharacterDefaults()
        this.setPlayerDefaults()
        this.setupTimers()
        this.setupStates()
        this.adjustImage()
        this.game.setPlayer(this)

    #set the default values of the player that will be different than
    #the character default values
    def setPlayerDefaults(this):
        #player game attributes
        this.healthMax = 3          #maximum number of health
        this.health = 3             #current health

        #player image variables
        this.imageOffsetX = this.game.getBlockScale()
        this.imageOffsetY = 0       #how much an image needs to be adjusted on the Y axis

        #player physics variables
        this.jumpForceX = 1.5       #how much X force is put into a jump
        this.jumpForceY = 4         #how much Y force is put into a jump
        this.runSpeed = 0.5         #how fast a character runs
        this.maxSpeed = 2           #the maximum speed a character can achieve
        this.attackForce = 3.5        #how much force a character adds when they hit with an attack


        #player timer and triggers
        this.jumpTimeTrig = 15      #how long a jump lasts
        this.midJumpTimeTrig = 7    #how long before it is considered mid-jump
        this.jumpCool = 18          #how long before a character can jump again
        this.attackCool = 10        #how long before a character can attack again        
        this.hurtCool = 200         #how long before you can take damage again

        #player sounds
        this.wavJump = pygame.mixer.Sound("sounds/effects/playerJump.wav")
        this.wavAttack = pygame.mixer.Sound("sounds/effects/playerAttack.wav")
        this.wavHurt = pygame.mixer.Sound("sounds/effects/playerHurt.wav")
        this.wavDeath = pygame.mixer.Sound("sounds/effects/playerDeath.wav")

        


