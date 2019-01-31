import pygame
from gameObject import GameObject
from hud import HUD


#a sprite object that all game objects derive from contains a rect for collision 
class Trigger(GameObject):
    
    def __init__(this, name, posX, posY, sizeX, sizeY):
        this.__name = name
        image = this.game.imgBlank
        this.rect = pygame.Rect(posX, posY, sizeX, sizeY)
        super().__init__(name, image, posX, posY, sizeX, sizeY)
        #add this Trigger to the list of Trigger Sprites
        this.game.getTriggerSprites().add(this)
        #initilize the trigger
        this.init()

    hud = HUD()

#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

    __isTriggered = False    #a boolean to represent if the event has happened recently
    timers = {}         #a dictonary of timers    


#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

    def getIsTriggered(this):
        return this.__isTriggered


#------------------------------------------------------------------------------#
#                                  Mutators                                    #
#------------------------------------------------------------------------------#

    def setIsTriggered(this, boolean):
        this.__isTriggered = boolean
             
#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#
        
    def init(this):
        this.game.setTimer(this, "triggerTimer", -1)
        this.game.setTimer(this, "messageTimer", -1)

    #set off the trigger event
    def event(this):
        #check to see if the event has already been triggered
        #and there are no game overs
        if not this.getIsTriggered()\
           and not this.game.getGameOver():

            if this.game.checkTimer(this, "triggerTimer"):
                if this.getName() == "clearMessages":
                    this.hud.removeTextBox()
                    #ensure that we dont spam this trigger
                    this.game.setTimer(this, "triggerTimer", 25)

            #if enough time has passed to display another message
            if this.game.checkTimer(this, "messageTimer"):
                if this.getName() == "howToMoveMessage":
                    #remove any text box elements (if there is any)
                    this.hud.removeTextBox()
                    #Create a text box with a message
                    this.hud.createBoxWithMessage( "-----------Welcome to Shinobi Assassin-----------"\
                                                  +"                                                 "\
                                                  +"The goal of the game is to make it to the end of "\
                                                  +"   the level without losing all of your hearts   "\
                                                  +"   --Press W,A,S,D or the ARROW keys to move--   "\
                                                  +"         --Press the SPACE-BAR to jump--         "\
                                                  +"          --Press the ESC key to quit--          ",
                               this.hud.getTextBoxLocX(), this.hud.getTextBoxLocY(),\
                               this.hud.getTextBoxSizeX(), this.hud.getTextBoxSizeY(),\
                               False)
                    this.game.setTimer(this, "messageTimer", 50)

                elif this.getName() == "howToAttackMessage":
                    #remove any text box elements (if there is any)
                    this.hud.removeTextBox()
                    #Create a text box with a message
                    this.hud.createBoxWithMessage( "--------------------Attacking--------------------"\
                                                  +"                                                 "\
                                                  +"In order to make an attack, you must approach the"\
                                                  +" enemy carefully and then press the attack button"\
                                                  +"      --Attack Button: RIGHT CONTROL (ctrl)--    "\
                                                  +"Be careful not to get too close or else the enemy"\
                                                  +"         will try to attack you instead          ",\
                               this.hud.getTextBoxLocX(), this.hud.getTextBoxLocY(),\
                               this.hud.getTextBoxSizeX(), this.hud.getTextBoxSizeY(),\
                               False)
                    this.game.setTimer(this, "messageTimer", 50)

                elif this.getName() == "enemyInfoMessage":
                    #remove any text box elements (if there is any)
                    this.hud.removeTextBox()
                    #Create a text box with a message
                    this.hud.createBoxWithMessage( "----------------Enemy  Behavior------------------"\
                                                  +"                                                 "\
                                                  +"  When an enemy spots you, they will attempt to  "\
                                                  +"   chase you down and stab you. They will only   "\
                                                  +"   follow your last known location. After doing  "\
                                                  +"  so, they will continue to search for a period  "\
                                                  +" of time until they go back to their posted area.",\
                               this.hud.getTextBoxLocX(), this.hud.getTextBoxLocY(),\
                               this.hud.getTextBoxSizeX(), this.hud.getTextBoxSizeY(),\
                               False)
                    this.game.setTimer(this, "messageTimer", 50)

                elif this.getName() == "enemyBroadcastMessage":
                    #remove any text box elements (if there is any)
                    this.hud.removeTextBox()
                    #Create a text box with a message
                    this.hud.createBoxWithMessage( "---------------Enemy  Broadcasting---------------"\
                                                  +"                                                 "\
                                                  +"   When an enemy spots you, they will alert all  "\
                                                  +"  other enemies around them. In order to prevent "\
                                                  +"  a group of enemies trying to attack you all at "\
                                                  +"    once, it is better to try and make your way  "\
                                                  +"     through the level without getting spotted   ",\
                               this.hud.getTextBoxLocX(), this.hud.getTextBoxLocY(),\
                               this.hud.getTextBoxSizeX(), this.hud.getTextBoxSizeY(),\
                               False)
                    this.game.setTimer(this, "messageTimer", 50)

                elif this.getName() == "victory":
                    this.game.setVictory(True)
                    this.game.setGameOver(True)



