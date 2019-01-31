import pygame
from gameController import GameController


#a sprite object that all game objects derive from contains a rect for collision 
class GameObject(pygame.sprite.Sprite):

    #reference to our game info singleton
    game = GameController()
    
    def __init__(this, name, image, posX, posY, sizeX, sizeY):
        this.__name = name
        this.rect = pygame.Rect(posX, posY, sizeX, sizeY)
        super().__init__()
        this.image = image.convert_alpha()
             
#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

    def getName(this):
        return this.__name

    def getRect(this):
        return this.rect

    def getImage(this):
        return this.image


#------------------------------------------------------------------------------#
#                                  Mutators                                    #
#------------------------------------------------------------------------------#

    def setName(this, text):
        this.__name = text

    def setRect(this, obj):
        this.rect = obj

    def setImage(this, obj):
        this.image = obj  


#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#
        
    #shift an object a certain number of x and y coordinates specified by the moveX and moveY arguments
    def move(this, moveX, moveY):
        this.getRect().move_ip(moveX, moveY)

    def shift(this, moveX, moveY):
        this.getRect().move_ip(moveX, moveY)

    def draw(this, screen):
        screen.blit(this.getImage(), this.getRect())

    def checkGrounded(this):
        groundChecker = this.getRect().move(0,1)
        groundChecker.inflate_ip(-1,0)

        for ground in this.game.getTerrainSprites():
            if groundChecker.colliderect(ground.getRect()) and ground.density > 0:
                return True

        return False


