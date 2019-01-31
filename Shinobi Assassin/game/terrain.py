import pygame
from gameObject import GameObject


#an object which represents the terrain that will be traveled through derived from game object
class Block(GameObject):

    def __init__(this, name, image, posX, posY, sizeX, sizeY, density, mass):
        #boost the size of the image to refect the block scale
        image = pygame.transform.scale(image, (this.game.getBlockScale(), this.game.getBlockScale()))
        super().__init__(name, image, posX, posY, sizeX, sizeY)
        this.density = density
        this.mass = mass
        this.game.getTerrainSprites().add(this)     
    

class Brick(Block):

    def __init__(this, posX, posY):
        super().__init__("Brick", this.game.brickImage, posX, posY, this.game.getBlockScale(), this.game.getBlockScale(), 1, 0)

class Wall(Block):

    def __init__(this, posX, posY):
        super().__init__("Wall", this.game.wallImage, posX, posY, this.game.getBlockScale(), this.game.getBlockScale(), 0, 0)

class Sky(Block):

    def __init__(this, posX, posY):
        super().__init__("Sky", this.game.skyImage, posX, posY, this.game.getBlockScale(), this.game.getBlockScale(), 0, 0)

class Ground(Block):

    def __init__(this, posX, posY):
        super().__init__("Ground", this.game.groundImage, posX, posY, this.game.getBlockScale(), this.game.getBlockScale(), 1, 0)
        
class Door(Block):

    def __init__(this, posX, posY):
        super().__init__("Door", this.game.doorImage, posX, posY, this.game.getBlockScale(), this.game.getBlockScale(), 0, 0)


