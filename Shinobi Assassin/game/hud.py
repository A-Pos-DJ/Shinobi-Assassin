import pygame
from gameController import GameController
from gameObject import GameObject

#A singleton class for the HUD
class HUD:
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
#                              HUD  Text  Images                               #
#------------------------------------------------------------------------------#

        #Capital Letter Images
        capA = pygame.image.load("sprites/hud/text/capA.png")
        capB = pygame.image.load("sprites/hud/text/capB.png")
        capC = pygame.image.load("sprites/hud/text/capC.png")
        capD = pygame.image.load("sprites/hud/text/capD.png")
        capE = pygame.image.load("sprites/hud/text/capE.png")
        capF = pygame.image.load("sprites/hud/text/capF.png")
        capG = pygame.image.load("sprites/hud/text/capG.png")
        capH = pygame.image.load("sprites/hud/text/capH.png")
        capI = pygame.image.load("sprites/hud/text/capI.png")
        capJ = pygame.image.load("sprites/hud/text/capJ.png")
        capK = pygame.image.load("sprites/hud/text/capK.png")
        capL = pygame.image.load("sprites/hud/text/capL.png")
        capM = pygame.image.load("sprites/hud/text/capM.png")
        capN = pygame.image.load("sprites/hud/text/capN.png")
        capO = pygame.image.load("sprites/hud/text/capO.png")
        capP = pygame.image.load("sprites/hud/text/capP.png")
        capQ = pygame.image.load("sprites/hud/text/capQ.png")
        capR = pygame.image.load("sprites/hud/text/capR.png")
        capS = pygame.image.load("sprites/hud/text/capS.png")
        capT = pygame.image.load("sprites/hud/text/capT.png")
        capU = pygame.image.load("sprites/hud/text/capU.png")
        capV = pygame.image.load("sprites/hud/text/capV.png")
        capW = pygame.image.load("sprites/hud/text/capW.png")
        capX = pygame.image.load("sprites/hud/text/capX.png")
        capY = pygame.image.load("sprites/hud/text/capY.png")
        capZ = pygame.image.load("sprites/hud/text/capZ.png")

        #Lowercase Letter Images
        lowA = pygame.image.load("sprites/hud/text/lowA.png")
        lowB = pygame.image.load("sprites/hud/text/lowB.png")
        lowC = pygame.image.load("sprites/hud/text/lowC.png")
        lowD = pygame.image.load("sprites/hud/text/lowD.png")
        lowE = pygame.image.load("sprites/hud/text/lowE.png")
        lowF = pygame.image.load("sprites/hud/text/lowF.png")
        lowG = pygame.image.load("sprites/hud/text/lowG.png")
        lowH = pygame.image.load("sprites/hud/text/lowH.png")
        lowI = pygame.image.load("sprites/hud/text/lowI.png")
        lowJ = pygame.image.load("sprites/hud/text/lowJ.png")
        lowK = pygame.image.load("sprites/hud/text/lowK.png")
        lowL = pygame.image.load("sprites/hud/text/lowL.png")
        lowM = pygame.image.load("sprites/hud/text/lowM.png")
        lowN = pygame.image.load("sprites/hud/text/lowN.png")
        lowO = pygame.image.load("sprites/hud/text/lowO.png")
        lowP = pygame.image.load("sprites/hud/text/lowP.png")
        lowQ = pygame.image.load("sprites/hud/text/lowQ.png")
        lowR = pygame.image.load("sprites/hud/text/lowR.png")
        lowS = pygame.image.load("sprites/hud/text/lowS.png")
        lowT = pygame.image.load("sprites/hud/text/lowT.png")
        lowU = pygame.image.load("sprites/hud/text/lowU.png")
        lowV = pygame.image.load("sprites/hud/text/lowV.png")
        lowW = pygame.image.load("sprites/hud/text/lowW.png")
        lowX = pygame.image.load("sprites/hud/text/lowX.png")
        lowY = pygame.image.load("sprites/hud/text/lowY.png")
        lowZ = pygame.image.load("sprites/hud/text/lowZ.png")
        
        #Number Images
        num0 = pygame.image.load("sprites/hud/text/num0.png")
        num1 = pygame.image.load("sprites/hud/text/num1.png")
        num2 = pygame.image.load("sprites/hud/text/num2.png")
        num3 = pygame.image.load("sprites/hud/text/num3.png")
        num4 = pygame.image.load("sprites/hud/text/num4.png")
        num5 = pygame.image.load("sprites/hud/text/num5.png")
        num6 = pygame.image.load("sprites/hud/text/num6.png")
        num7 = pygame.image.load("sprites/hud/text/num7.png")
        num8 = pygame.image.load("sprites/hud/text/num8.png")
        num9 = pygame.image.load("sprites/hud/text/num9.png")

        #Misc Text Images
        txtAnd = pygame.image.load("sprites/hud/text/txtAnd.png")
        txtArrowLeft = pygame.image.load("sprites/hud/text/txtArrowLeft.png")
        txtArrowRight = pygame.image.load("sprites/hud/text/txtArrowRight.png")
        txtAsterisk = pygame.image.load("sprites/hud/text/txtAsterisk.png")
        txtAt = pygame.image.load("sprites/hud/text/txtAt.png")
        txtBackSlash = pygame.image.load("sprites/hud/text/txtBackSlash.png")
        txtCarrot = pygame.image.load("sprites/hud/text/txtCarrot.png")
        txtColon = pygame.image.load("sprites/hud/text/txtColon.png")
        txtComma = pygame.image.load("sprites/hud/text/txtComma.png")
        txtCurlyLeft = pygame.image.load("sprites/hud/text/txtCurlyLeft.png")
        txtCurlyRight = pygame.image.load("sprites/hud/text/txtCurlyRight.png")
        txtDoubleQuote = pygame.image.load("sprites/hud/text/txtDblQuote.png")
        txtDollar = pygame.image.load("sprites/hud/text/txtDollar.png")
        txtEqual = pygame.image.load("sprites/hud/text/txtEqual.png")
        txtExclaim = pygame.image.load("sprites/hud/text/txtExclaim.png")
        txtForwardSlash = pygame.image.load("sprites/hud/text/txtFwdSlash.png")
        txtMinus = pygame.image.load("sprites/hud/text/txtMinus.png")
        txtPercent = pygame.image.load("sprites/hud/text/txtPercent.png")
        txtPeriod = pygame.image.load("sprites/hud/text/txtPeriod.png")
        txtPlus = pygame.image.load("sprites/hud/text/txtPlus.png")
        txtPound = pygame.image.load("sprites/hud/text/txtPound.png")
        txtQuestionMark = pygame.image.load("sprites/hud/text/txtQuesMark.png")
        txtRoundLeft = pygame.image.load("sprites/hud/text/txtRoundLeft.png")
        txtRoundRight = pygame.image.load("sprites/hud/text/txtRoundRight.png")
        txtSemiColon = pygame.image.load("sprites/hud/text/txtSemiColon.png")
        txtSingleQuote = pygame.image.load("sprites/hud/text/txtSnglQuote.png")
        txtSpace = pygame.image.load("sprites/hud/text/txtSpace.png")
        txtSpace2 = pygame.image.load("sprites/hud/text/txtSpace2.png")
        txtSquareLeft = pygame.image.load("sprites/hud/text/txtSquareLeft.png")
        txtSquareRight = pygame.image.load("sprites/hud/text/txtSquareRight.png")
        txtSquiggle = pygame.image.load("sprites/hud/text/txtSquiggle.png")
        txtStraightLine = pygame.image.load("sprites/hud/text/txtStraightLine.png")
        txtTilde = pygame.image.load("sprites/hud/text/txtTilde.png")
        txtUnderscore = pygame.image.load("sprites/hud/text/txtUnderscore.png")

        #Health Images
        heartFull = pygame.image.load("sprites/hud/health/hFull.png")
        heartEmpty = pygame.image.load("sprites/hud/health/hBack.png")

        #Character Image Dictionary
        __textImageDict ={
            'A' : capA, 'B' : capB, 'C' : capC, 'D' : capD, 'E' : capE,
            'F' : capF, 'G' : capG, 'H' : capH, 'I' : capI, 'J' : capJ,
            'K' : capK, 'L' : capL, 'M' : capM, 'N' : capN, 'O' : capO,
            'P' : capP, 'Q' : capQ, 'R' : capR, 'S' : capS, 'T' : capT,
            'U' : capU, 'V' : capV, 'W' : capW, 'X' : capX, 'Y' : capY,
            'Z' : capZ,

            'a' : lowA, 'b' : lowB, 'c' : lowC, 'd' : lowD, 'e' : lowE,
            'f' : lowF, 'g' : lowG, 'h' : lowH, 'i' : lowI, 'j' : lowJ,
            'k' : lowK, 'l' : lowL, 'm' : lowM, 'n' : lowN, 'o' : lowO,
            'p' : lowP, 'q' : lowQ, 'r' : lowR, 's' : lowS, 't' : lowT,
            'u' : lowU, 'v' : lowV, 'w' : lowW, 'x' : lowX, 'y' : lowY,
            'z' : lowZ,

            '0' : num0, '1' : num1, '2' : num2, '3' : num3, '4' : num4,
            '5' : num5, '6' : num6, '7' : num7, '8' : num8, '9' : num9,

            '&' : txtAnd, '<' : txtArrowLeft, '>' : txtArrowRight,
            '*' : txtAsterisk, '@' : txtAt, '\\' : txtBackSlash,
            '^' : txtCarrot, ':' : txtColon, ',' : txtComma,
            '{' : txtCurlyLeft, '}' : txtCurlyRight, '"' : txtDoubleQuote,
            '$' : txtDollar, '=' : txtEqual, '!' : txtExclaim,
            '/' : txtForwardSlash, '-' : txtMinus, '%' : txtPercent,
            '.' : txtPeriod, '+' : txtPlus, '#' : txtPound,
            '?' : txtQuestionMark, '(' : txtRoundLeft, ')' : txtRoundRight,
            ';' : txtSemiColon, ' ' : txtSpace, '[' : txtSquareLeft,
            ']' : txtSquareRight, '~' : txtSquiggle, '|' : txtStraightLine,
            '`' : txtTilde, '_' : txtUnderscore
            }

#------------------------------------------------------------------------------#
#                              HUD  Window  Images                             #
#------------------------------------------------------------------------------#

        #Text Window Images
        txtWinHorizontal = pygame.image.load("sprites/hud/window/horizontal.png")
        txtWinVertical = pygame.image.load("sprites/hud/window/vertical.png")
        txtWinTopLeft = pygame.image.load("sprites/hud/window/topLeft.png")
        txtWinTopRight = pygame.image.load("sprites/hud/window/topRight.png")
        txtWinBotLeft = pygame.image.load("sprites/hud/window/bottomLeft.png")
        txtWinBotRight = pygame.image.load("sprites/hud/window/bottomRight.png")
        txtWinSpaceGray = pygame.image.load("sprites/hud/window/spaceGray.png")
        txtWinSpaceBlack = pygame.image.load("sprites/hud/window/spaceBlack.png")


#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

        #HUD Sprite Groups
        __HUDSprites = pygame.sprite.Group()            #group of sprites in which all HUD elements appear
        __movingHUDSprites = pygame.sprite.Group()      #group of sprites in which all moving hud elements appear
        __textBoxSprites = pygame.sprite.Group()        #group of sprites in which all text box elements appear 
        __heartSprites = pygame.sprite.Group()          #group of sprites in which all Health elements appear


        #Default HUD Settings
        __textBoxBlock = int(game.getBlockScale() // 2) #the size of a text block
        __textBoxLocX = int(game.blockToPosX(2))        #the default location on the X axis of where a text box is placed
        __textBoxLocY = int(game.blockToPosY(1))        #the default location on the Y axis of where a text box is placed
        __textBoxSizeX = int(game.getScreenBlockLengthX() - 4) * 2 #the default width (in text blocks) of a text message block
        __textBoxSizeY = int(10)                        #the default length (in text blocks) of a text message block
        __textBoxMargin = int(2)                        #the default number of text blocks from the border of a text box in which messages may be written
        
        
#------------------------------------------------------------------------------#
#                                  Accessors                                   #
#------------------------------------------------------------------------------#

        def getHUDSprites(this):
            return this.__HUDSprites
        
        def getMovingHUDSprites(this):
            return this.__movingHUDSprites

        def getTextBoxSprites(this):
            return this.__textBoxSprites

        def getHeartSprites(this):
            return this.__heartSprites
        
        def getTextBoxBlock(this):
            return this.__textBoxBlock

        def getTextBoxLocX(this):
            return this.__textBoxLocX
        
        def getTextBoxLocY(this):
            return this.__textBoxLocY
        
        def getTextBoxSizeX(this):
            return this.__textBoxSizeX
        
        def getTextBoxSizeY(this):
            return this.__textBoxSizeY

        def getTextBoxMargin(this):
            return this.__textBoxMargin


#------------------------------------------------------------------------------#
#                                  Mutators                                    #
#------------------------------------------------------------------------------#

        def setHUDSprites(this, group):
            this.__HUDSprites = group
            
        def setHeartSprites(this, group):
            this.__heartSprites = group         

        def setTextBoxBlock(this, num):
            this.__textBoxBlock = num

        def setTextBoxLocX(this, num):
            this.__textBoxLocX = num
        
        def setTextBoxLocY(this, num):
            this.__textBoxLocY = num
        
        def setTextBoxSizeX(this, num):
            this.__textBoxSizeX = num
        
        def setTextBoxSizeY(this, num):
            this.__textBoxSizeY = num

        def setTextBoxMargin(this, num):
            this.__textBoxMargin = num


#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#
        
        #Note: 2 text window blocks = 1 text block
        def createTextBox(this, posX, posY, blockSizeX, blockSizeY, isMoving):

            #ensure the text box is not too small to display text
            if blockSizeX < 10 or blockSizeY < 5:
                print ("The text box was too small to be created")
                return

            #create loop variables
            idx = int(2)
            
            #create the top left corner
            obj = HUDObject("Box Top Left", this.txtWinTopLeft, posX, posY,\
                      this.getTextBoxBlock(), this.getTextBoxBlock())

            #add it to the text box sprite list
            this.getTextBoxSprites().add(obj)
            #if it is supposed to be a moving object
            if isMoving:
                #add it to the moving sprite list
                this.getMovingHUDSprites().add(obj)

        
            #Create the top bar
            idx = 1
            while idx <= (blockSizeX - 1):
                obj = HUDObject("Box Horizontal", this.txtWinHorizontal,\
                          posX + (this.getTextBoxBlock() * idx), posY, \
                          this.getTextBoxBlock(), this.getTextBoxBlock())

                #add it to the text box sprite list
                this.getTextBoxSprites().add(obj)
                #if it is supposed to be a moving object
                if isMoving:
                    #add it to the moving sprite list
                    this.getMovingHUDSprites().add(obj)

                idx += 1
        
            #Create the top right corner
            obj = HUDObject("Box Top Right", this.txtWinTopRight, \
                      posX + (this.getTextBoxBlock() * blockSizeX), posY, \
                      this.getTextBoxBlock(), this.getTextBoxBlock())

            #add it to the text box sprite list
            this.getTextBoxSprites().add(obj)
            #if it is supposed to be a moving object
            if isMoving:
                #add it to the moving sprite list
                this.getMovingHUDSprites().add(obj)

            #Create the left bar
            idx = 1
            while idx <= (blockSizeY - 1):
                obj = HUDObject("Box Vertical", this.txtWinVertical,\
                          posX, posY + (this.getTextBoxBlock() * idx), \
                          this.getTextBoxBlock(), this.getTextBoxBlock())

                #add it to the text box sprite list
                this.getTextBoxSprites().add(obj)
                #if it is supposed to be a moving object
                if isMoving:
                    #add it to the moving sprite list
                    this.getMovingHUDSprites().add(obj)
                
                idx += 1
        
            #Create the right bar
            idx = 1
            while idx <= (blockSizeY - 1):
                obj = HUDObject("Box Vertical", this.txtWinVertical,\
                          posX + (this.getTextBoxBlock() * blockSizeX), \
                          posY + (this.getTextBoxBlock() * idx), \
                          this.getTextBoxBlock(), this.getTextBoxBlock())
                
                #add it to the text box sprite list
                this.getTextBoxSprites().add(obj)
                #if it is supposed to be a moving object
                if isMoving:
                    #add it to the moving sprite list
                    this.getMovingHUDSprites().add(obj)
                    
                idx += 1
        
            #Create the bottom left corner
            obj = HUDObject("Box Bottom Left", this.txtWinBotLeft, \
                      posX, posY + (this.getTextBoxBlock() * blockSizeY) , \
                      this.getTextBoxBlock(), this.getTextBoxBlock())

            #add it to the text box sprite list
            this.getTextBoxSprites().add(obj)
            #if it is supposed to be a moving object
            if isMoving:
                #add it to the moving sprite list
                this.getMovingHUDSprites().add(obj)

            #Create the bottom bar
            idx = 1
            while idx <= (blockSizeX - 1):
                obj = HUDObject("Box Horizontal", this.txtWinHorizontal,\
                          posX + (this.getTextBoxBlock() * idx), \
                          posY + (this.getTextBoxBlock() * blockSizeY), \
                          this.getTextBoxBlock(), this.getTextBoxBlock())

                #add it to the text box sprite list
                this.getTextBoxSprites().add(obj)
                #if it is supposed to be a moving object
                if isMoving:
                    #add it to the moving sprite list
                    this.getMovingHUDSprites().add(obj)
                
                idx += 1
        
            #Create the bottom right corner
            obj = HUDObject("Box Bottom Right", this.txtWinBotRight,\
                      posX + (this.getTextBoxBlock() * blockSizeX), \
                      posY + (this.getTextBoxBlock() * blockSizeY) , \
                      this.getTextBoxBlock(), this.getTextBoxBlock())

            #add it to the text box sprite list
            this.getTextBoxSprites().add(obj)
            #if it is supposed to be a moving object
            if isMoving:
                #add it to the moving sprite list
                this.getMovingHUDSprites().add(obj)
         
            #Fill the box with a space
            obj = HUDObject("Box Space Black", this.txtWinSpaceBlack, \
                      posX + this.getTextBoxBlock(), \
                      posY + this.getTextBoxBlock() , \
                      (int(this.getTextBoxBlock() * (blockSizeX - 1))), \
                      (int(this.getTextBoxBlock() * (blockSizeY - 1))))

            #add it to the text box sprite list
            this.getTextBoxSprites().add(obj)
            #if it is supposed to be a moving object
            if isMoving:
                #add it to the moving sprite list
                this.getMovingHUDSprites().add(obj)

        def createTextMessage(this, text, posX, posY, blockSizeX, blockSizeY, isMoving):
            if len(text) > ((blockSizeX + 1) * (blockSizeY + 1)):
                print("The message is too big for the text box")
            else:
                idx = 0
                idxX = 0
                idxY = 0
                allTextDisplayed = False
                while not allTextDisplayed:
                    for idxY in range (0, blockSizeY + 1):
                        for idxX in range (0, (blockSizeX + 1)):
                            obj = HUDText(text[idx],\
                                    posX + (idxX * this.getTextBoxBlock()),\
                                    posY + (idxY * this.getTextBoxBlock()))
                            
                            #add it to the text box sprite list
                            this.getTextBoxSprites().add(obj)
                            #if it is supposed to be a moving object
                            if isMoving:
                                #add it to the moving sprite list
                                this.getMovingHUDSprites().add(obj)
                                
                            idx += 1
                            #ensure we dont raise an our of bounds error
                            if idx >= len(text):
                                allTextDisplayed = True
                                break
                        if idx >= len(text):
                            break
            
        def createBoxWithMessage(this, text, posX, posY, blockSizeX, blockSizeY, isMoving):
            this.createTextBox(posX, posY, blockSizeX, blockSizeY, isMoving)
            this.createTextMessage(text,\
                                   posX + (this.getTextBoxBlock() * this.getTextBoxMargin()),\
                                   posY + (this.getTextBoxBlock() * this.getTextBoxMargin()),\
                                   blockSizeX - (this.getTextBoxMargin() * 2),\
                                   blockSizeY - (this.getTextBoxMargin() * 2), isMoving)

        def removeTextBox(this):
            for sprite in this.getTextBoxSprites():
                sprite.kill()


        #gets an image from the HUD text Dictionary
        def getTextImage(this, char):
            return this.__textImageDict[char]

        def initGameHUD(this):
            this.getHUDSprites().empty()
            this.addHearts()

        #add the player's hearts to the screen
        def addHearts(this):
            blockLenX = this.game.getScreenBlockLengthX()
            blockLenY = this.game.getScreenBlockLengthY()

            for idx in range(0, this.game.getPlayer().healthMax):
                this.getHeartSprites().add(\
                    HUDObject("Empty Heart " + str(idx), this.heartEmpty,\
                          this.game.blockToPosX(blockLenX - (1.25 + (idx * 1.25))),\
                          this.game.blockToPosY(0.25),\
                          this.game.getBlockScale(), this.game.getBlockScale()))

            this.syncHearts()

        def syncHearts(this):
            blockLenX = this.game.getScreenBlockLengthX()
            blockLenY = this.game.getScreenBlockLengthY()
            
            #loop through each sprite in the heart sprite group and remove
            #all full hearts
            for obj in this.getHeartSprites():
                if "Full Heart" in obj.getName():
                    obj.kill()

            #add all full hearts again
            for idx in range(0, this.game.getPlayer().health):
                this.getHeartSprites().add(\
                    HUDObject("Full Heart " + str(idx), this.heartFull,\
                          this.game.blockToPosX(blockLenX - (1.25 + (idx * 1.25))),\
                          this.game.blockToPosY(0.25),\
                          this.game.getBlockScale(), this.game.getBlockScale()))
            
        def syncGameHUD(this):
            syncHearts()

            
            

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
        if HUD.__instance is None:
            # Create and remember instance
            HUD.__instance = HUD.__impl()

        # Store instance reference as the only member in the handle
        this.__dict__['_HUD__instance'] = HUD.__instance

    def __getattr__(this, attr):
        """ Delegate access to implementation """
        return getattr(this.__instance, attr)

    def __setattr__(this, attr, value):
        """ Delegate access to implementation """
        return setattr(this.__instance, attr, value)


#------------------------------------------------------------------------------#
#                                                                              #
#                           HUD  Object  Classes                               #
#                                                                              #
#------------------------------------------------------------------------------#

#an object which represents a HUD Object
class HUDObject(GameObject):

    def __init__(this, name, image, posX, posY, sizeX, sizeY):
        #Boost the size of the image to represent the rect
        image = pygame.transform.scale(image, (sizeX, sizeY))
        super().__init__(name, image, posX, posY, sizeX, sizeY)
        HUD().getHUDSprites().add(this)
        
#an object which represents the text in the HUD
class HUDText(GameObject):

    def __init__(this, char, posX, posY):
        #get the image from the HUD Dictionary
        image = HUD().getTextImage(char)
        #boost the size of the image to refect the half the size of the block scale
        image = pygame.transform.scale(image, (HUD().getTextBoxBlock(), HUD().getTextBoxBlock()))
        super().__init__("txt\"" + char + "\"", image,\
                         posX, posY, HUD().getTextBoxBlock(), HUD().getTextBoxBlock())
        HUD().getHUDSprites().add(this)  
