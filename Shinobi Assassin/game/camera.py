import pygame
from gameController import GameController
from hud import HUD
from menu import Menu
from gameObject import GameObject
from terrain import Block, Brick, Wall, Sky, Ground, Door
from character import Character
from npc import NPC, Gaurd
from player import Player
from item import Item

#A singleton Class that works as the game camera
class Camera:
    class __impl:
        """This implementation hides the singleton interface\
        in an inner class and creates exactly one instance of\
        the inner class. The outer class is a handle to the inner\
        class and delegates any requests to it. While the id() of\
        the handle objects changes, the id() of the inner class which\
        implements the singleton behaviour is constant."""

        #reference to our game info singleton
        game = GameController()

        #Nothing is in the initlizer, may add more at some point
        def __init__(this):
            pass


#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

        #Game Camera Variable
        __moveX = 0
        __moveY = 0
        __offsetX = 0
        __offsetY = 0
        __scrollSpeed = game.getBlockScale() #how fast the camera scrolls if the player is not pushing it
        __blockEdgeX = 20 # how far the player needs to be to the edge of the screen before the camera moves
        __blockEdgeY = 5 # how far the player needs to be to the edge of the screen before the camera moves
        __scrollThreshold = 2 #how many blocks the player needs to be in so the camera scrolls smoothly


#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

        def getMoveX(this):
            return this.__moveX

        def getMoveY(this):
            return this.__moveY

        def getOffsetX(this):
            return this.__offsetX        

        def getOffsetY(this):
            return this.__offsetY

        def getScrollSpeed(this):
            return this.__scrollSpeed

        def getBlockEdgeX(this):
            return this.__blockEdgeX

        def getBlockEdgeY(this):
            return this.__blockEdgeY

        def getScrollThreshold(this):
            return this.__scrollThreshold


#------------------------------------------------------------------------------#
#                                  Mutators                                    #
#------------------------------------------------------------------------------#

        def setMoveX(this, num):
            this.__moveX = num

        def setMoveY(this, num):
            this.__moveY = num

        def setOffsetX(this, num):
            this.__offsetX = num    

        def setOffsetY(this, num):
            this.__offsetY = num

        def setScrollSpeed(this, num):
            this.__scrollSpeed = num

        def setBlockEdgeX(this, num):
            this.__blockEdgeX = num

        def setScrollThreshold(this, num):
            this.__scrollThreshold = num


#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#

        def checkMove(this):
            #setup player variable to reduce code bloat
            player = this.game.getPlayer()
            block = this.game.getBlockScale()
            pixelsX = this.game.getResolution()[0]
            pixelsY = this.game.getResolution()[1]
            
            #If the player is facing the right side of the screen
            if player.isFacing == "right":
                #the player goes past the camera's distance flag
                if player.getRect().right + this.getOffsetX() > \
                   (((pixelsX / block) - this.getBlockEdgeX())\
                    * block) + this.getOffsetX():
                    #If the player is traveling faster than the camera scrolls normally
                    if player.speedX * this.game.deltaTime > this.getScrollSpeed():
                        #tell the camera to move as fast as the player
                        this.setMoveX(player.speedX * this.game.deltaTime)
                    #if the player is not moving as fast as the camera scrolls normally
                    elif player.speedX * this.game.deltaTime <= this.getScrollSpeed():
                        #the player is within a set number of blocks of the movement barrier...
                        if player.getRect().right + this.getOffsetX() < \
                           (((pixelsX / block) \
                             - (this.getBlockEdgeX() - this.getScrollThreshold())) \
                            * block) + this.getOffsetX():
                            #tell the camera to move as fast as the player
                            this.setMoveX(player.speedX * this.game.deltaTime)
                        else:
                            #tell the camera to move as fast as it nomrally scrolls
                            this.setMoveX(this.getScrollSpeed())
                else:
                    this.setMoveX(0)
            
            #If the player is facing the left side of the screen
            elif player.isFacing == "left":
                #the player goes past the camera's distance flag
                if player.getRect().left + this.getOffsetX() < \
                   (this.getBlockEdgeX() * block) + this.getOffsetX():
                    #If the player is traveling faster than the camera scrolls normally
                    if player.speedX * this.game.deltaTime < -this.getScrollSpeed():
                        #tell the camera to move as fast as the player
                        this.setMoveX(player.speedX * this.game.deltaTime)
                    #if the player is not moving as fast as the camera scrolls normally
                    elif player.speedX * this.game.deltaTime >= -this.getScrollSpeed():
                        #the player is within a set number of blocks of the movement barrier...
                        if player.getRect().left + this.getOffsetX() > \
                           ((this.getBlockEdgeX() - this.getScrollThreshold()) \
                            * block) + this.getOffsetX():
                            #tell the camera to move as fast as the player
                            this.setMoveX(player.speedX * this.game.deltaTime)
                        else:
                            #tell the camera to move as fast as it nomrally scrolls
                            this.setMoveX(-this.getScrollSpeed())
                else:
                    this.setMoveX(0)

            #vertical movement


            #the player goes above the camera's distance flag
            if player.getRect().top + this.getOffsetY() > \
               (((pixelsY / block) - this.getBlockEdgeY()) * block) + this.getOffsetY():
                #If the player is traveling faster than the camera scrolls normally
                if player.speedY * this.game.deltaTime > this.getScrollSpeed():
                    #tell the camera to move as fast as the player
                    this.setMoveY(player.speedY * this.game.deltaTime)
                #if the player is not moving as fast as the camera scrolls normally
                elif player.speedY * this.game.deltaTime <= this.getScrollSpeed():
                    #the player is within a set number of blocks of the movement barrier...
                    if player.getRect().top + this.getOffsetY() < \
                       (((pixelsY / block) \
                         - (this.getBlockEdgeY() - this.getScrollThreshold())) \
                        * block) + this.getOffsetY():
                        #tell the camera to move as fast as the player
                        this.setMoveY(player.speedX * this.game.deltaTime)
                    else:
                        #tell the camera to move as fast as it nomrally scrolls
                        this.setMoveY(this.getScrollSpeed())

            #the player goes above the camera's distance flag
            elif player.getRect().bottom + this.getOffsetY() < \
               (this.getBlockEdgeY() * block) + this.getOffsetY():
                #If the player is traveling faster than the camera scrolls normally
                if player.speedY * this.game.deltaTime < -this.getScrollSpeed():
                    #tell the camera to move as fast as the player
                    this.setMoveY(player.speedY * this.game.deltaTime)
                #if the player is not moving as fast as the camera scrolls normally
                elif player.speedY * this.game.deltaTime >= -this.getScrollSpeed():
                    #the player is within a set number of blocks of the movement barrier...
                    if player.getRect().bottom + this.getOffsetX() > \
                       ((this.getBlockEdgeY() - this.getScrollThreshold()) \
                        * block) + this.getOffsetY():
                        #tell the camera to move as fast as the player
                        this.setMoveY(player.speedY * this.game.deltaTime)
                    else:
                        #tell the camera to move as fast as it nomrally scrolls
                        this.setMoveY(-this.getScrollSpeed())
                        
            else:
                this.setMoveY(0)

                
                

        def update(this, sObject):
            """ The camera is an illusion, you think that
            the camera is shifting to the right... in reality
            all of the on screen objects are moving to the left"""
            
            #if we are refering to the player
            if sObject == this.game.getPlayer():
                #if we are moving the camera on the X axis
                if not this.getMoveX() == 0:
                    this.game.getPlayer().shift(-this.getMoveX(), 0)
                    this.setOffsetX(-this.getMoveX() + this.getOffsetX())
                    #set camera X move to 0 after all objects have been moved
                    this.setMoveX(0)

                #if we are moving the camera on the Y axis
                if not this.getMoveY() == 0:
                    this.game.getPlayer().shift(0, -this.getMoveY())
                    this.setOffsetY(-this.getMoveY() + this.getOffsetY())
                    #set camera Y move to 0 after all objects have been moved
                    this.setMoveY(0)

            #if we are refering to a single Rect      
            if isinstance(sObject, pygame.Rect):
                #if we are moving the camera on the X axis
                if not this.getMoveX() == 0:
                    sObject.move_ip(-this.getMoveX(), 0)
                    
                #if we are moving the camera on the Y axis
                if not this.getMoveY() == 0:
                    sObject.move_ip(0, -this.getMoveY())

            #if we are refering to a dictonary      
            if isinstance(sObject, dict):
                block = this.game.getBlockScale()
                loadRect = pygame.Rect((0,0),(this.game.getResolution()))
                #expand the rect to account for the loading buffer
                loadRect.inflate_ip(block * this.game.loadingBuffer,\
                                    block * this.game.loadingBuffer)
                
                #loop through each sprite in the sprite buffer
                for key, value in sObject.items():
                    if not loadRect.contains(value.getRect()):
                        #if we are moving the camera on the X axis
                        if not this.getMoveX() == 0:
                            value.shift(-this.getMoveX(), 0)
                        #if we are moving the camera on the Y axis
                        if not this.getMoveY() == 0:
                            value.shift(0, -this.getMoveY())

            #if we are refering to a sprite group      
            if isinstance(sObject, pygame.sprite.Group):
                #loop through each sprite in the sprite group
                for sprite in sObject:
                    #if the sprite is not an NPC
                    if not isinstance(sprite, NPC):
                        #if we are moving the camera on the X axis
                        if not this.getMoveX() == 0:
                            sprite.shift(-this.getMoveX(), 0)

                        #if we are moving the camera on the Y axis
                        if not this.getMoveY() == 0:
                            sprite.shift(0, -this.getMoveY())

                    #if the sprite is an NPC
                    if isinstance(sprite, NPC):
                        #if we are moving the camera on the X axis
                        if not this.getMoveX() == 0:
                            sprite.shift(-this.getMoveX(), 0)
                            sprite.AIDesiredLocation.move_ip(-this.getMoveX(), 0)
                            sprite.AILastSpotted.move_ip(-this.getMoveX(), 0)
                            #if we are debugging the game
                            if this.game.debugMode:
                                if not sprite.testRect == None:
                                    sprite.testRect.move_ip(-this.getMoveX(), 0)

                        #if we are moving the camera on the Y axis
                        if not this.getMoveY() == 0:
                            sprite.shift(0, -this.getMoveY())
                            sprite.AIDesiredLocation.move_ip(0, -this.getMoveY())
                            sprite.AILastSpotted.move_ip(0, -this.getMoveY())
                            #if we are debugging the game
                            if this.game.debugMode:
                                if not sprite.testRect == None:
                                    sprite.testRect.move_ip(0, -this.getMoveY())


        #resets the camera's move and offset positions
        #mainly used when going back to main menu
        def reset(this):      
            this.setMoveX(0)
            this.setMoveY(0)
            this.setOffsetX(0)
            this.setOffsetY(0)


#------------------------------------------------------------------------------#
#                                                                              #
#                           Rest of the Outer Class                            #
#                                                                              #
#------------------------------------------------------------------------------#

    # storage for the instance reference
    __instance = None

    def __init__(this):
        """ Create singleton instance """
        # Check whether we already have an instance
        if Camera.__instance is None:
            # Create and remember instance
            Camera.__instance = Camera.__impl()

        # Store instance reference as the only member in the handle
        this.__dict__['_Camera__instance'] = Camera.__instance

    def __getattr__(this, attr):
        """ Delegate access to implementation """
        return getattr(this.__instance, attr)

    def __setattr__(this, attr, value):
        """ Delegate access to implementation """
        return setattr(this.__instance, attr, value)
