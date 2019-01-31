import pygame
from gameObject import GameObject
#---------------------------Menu Objects-------------------------

#An object which represetns the menu in game
class Menu():

    def __init__(this, name):
        this.menuName = str(name)
        this.menuItemList = []

    def addMenuItem(this, name, image, posX, posY, sizeX, sizeY):
        MI = MenuItem(name, image, posX, posY, sizeX, sizeY)
        this.menuItemList.append(MI)

    def displayMenuItems(this, gameDisplay):
        idx = 0
        for MI in this.menuItemList[:]:
            idx += 1
            MI.draw(gameDisplay)
    """
    def selectOption(this, gameDisplay, event):

        #default selection is invalid
        selection = "Invalid"

        #if the user clicks on the main menu....
        if event.type == pygame.MOUSEBUTTONDOWN:
            #loop through each menu item
            for MI in this.menuItemList[:]:
                #comparing the X and Y coordinates of each menu item to see
                #if a menu item is actually selected
                if MI.getRect().collidepoint(pygame.mouse.get_pos()):
                    #return the name of the menu item that was selected
                    return MI.__str__()
    """


#An object that is a selectable menu item
class MenuItem(GameObject):

    def __init__(this, name, image, posX, posY, sizeX, sizeY):
        super().__init__(name, image, posX, posY, sizeX, sizeY)

    def __str__(this):
        return this.getName()


