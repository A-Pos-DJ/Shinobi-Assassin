import pygame
from character import Character

#Object class that derives from a character in the game to represent NPCs
class NPC(Character):
    
    def __init__(this, name, image, posX, posY, density, mass):
        super().__init__(name, image, posX, posY, this.game.getBlockScale(),\
                         this.game.getBlockScale() * 2, density, mass)
        
        #add this NPC to the list of NPC Sprites
        this.game.getNPCSprites().add(this)    


#Object class that derives from a character in the game to represent NPCs
class Gaurd(NPC):

    def __init__(this, name, posX, posY):
        image = pygame.image.load("sprites/characters/assassin/tile000.png")
        super().__init__(name, image, posX, posY, 0, 1)
        
        #initilize the gaurd
        this.init()


#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

    #gaurd images
    imgIdle = [pygame.image.load("sprites/characters/assassin/tile000.png"),\
                    pygame.image.load("sprites/characters/assassin/tile001.png"),\
                    pygame.image.load("sprites/characters/assassin/tile002.png"),\
                    pygame.image.load("sprites/characters/assassin/tile003.png"),\
                    pygame.image.load("sprites/characters/assassin/tile004.png"),\
                    pygame.image.load("sprites/characters/assassin/tile005.png"),\
                    pygame.image.load("sprites/characters/assassin/tile006.png"),\
                    pygame.image.load("sprites/characters/assassin/tile007.png"),\
                    pygame.image.load("sprites/characters/assassin/tile008.png"),\
                    pygame.image.load("sprites/characters/assassin/tile009.png")]
    imgUse = [pygame.image.load("sprites/characters/assassin/tile010.png"),\
                   pygame.image.load("sprites/characters/assassin/tile011.png"),\
                   pygame.image.load("sprites/characters/assassin/tile012.png"),\
                   pygame.image.load("sprites/characters/assassin/tile013.png"),\
                   pygame.image.load("sprites/characters/assassin/tile014.png"),\
                   pygame.image.load("sprites/characters/assassin/tile015.png"),\
                   pygame.image.load("sprites/characters/assassin/tile016.png"),\
                   pygame.image.load("sprites/characters/assassin/tile017.png"),\
                   pygame.image.load("sprites/characters/assassin/tile018.png"),\
                   pygame.image.load("sprites/characters/assassin/tile019.png")]
    imgRun = [pygame.image.load("sprites/characters/assassin/tile020.png"),\
                    pygame.image.load("sprites/characters/assassin/tile021.png"),\
                    pygame.image.load("sprites/characters/assassin/tile022.png"),\
                    pygame.image.load("sprites/characters/assassin/tile023.png"),\
                    pygame.image.load("sprites/characters/assassin/tile024.png"),\
                    pygame.image.load("sprites/characters/assassin/tile025.png"),\
                    pygame.image.load("sprites/characters/assassin/tile026.png"),\
                    pygame.image.load("sprites/characters/assassin/tile027.png"),\
                    pygame.image.load("sprites/characters/assassin/tile028.png"),\
                    pygame.image.load("sprites/characters/assassin/tile029.png")]
    imgAttack = [pygame.image.load("sprites/characters/assassin/tile030.png"),\
                      pygame.image.load("sprites/characters/assassin/tile031.png"),\
                      pygame.image.load("sprites/characters/assassin/tile032.png"),\
                      pygame.image.load("sprites/characters/assassin/tile033.png"),\
                      pygame.image.load("sprites/characters/assassin/tile034.png"),\
                      pygame.image.load("sprites/characters/assassin/tile035.png"),\
                      pygame.image.load("sprites/characters/assassin/tile036.png"),\
                      pygame.image.load("sprites/characters/assassin/tile037.png"),\
                      pygame.image.load("sprites/characters/assassin/tile038.png"),\
                      pygame.image.load("sprites/characters/assassin/tile039.png")]
    imgDeath = [pygame.image.load("sprites/characters/assassin/tile040.png"),\
                     pygame.image.load("sprites/characters/assassin/tile041.png"),\
                     pygame.image.load("sprites/characters/assassin/tile042.png"),\
                     pygame.image.load("sprites/characters/assassin/tile043.png"),\
                     pygame.image.load("sprites/characters/assassin/tile044.png"),\
                     pygame.image.load("sprites/characters/assassin/tile045.png"),\
                     pygame.image.load("sprites/characters/assassin/tile046.png"),\
                     pygame.image.load("sprites/characters/assassin/tile047.png"),\
                     pygame.image.load("sprites/characters/assassin/tile048.png"),\
                     pygame.image.load("sprites/characters/assassin/tile049.png")]
    imgBlank = pygame.image.load("sprites/characters/assassin/blank.png")



#------------------------------------------------------------------------------#
#                                                                              #
#                               Class  Methods                                 #
#                                                                              #
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#                                Initilization                                 #
#------------------------------------------------------------------------------#

    def init(this):
        this.setCharacterDefaults()
        this.setGaurdDefaults()
        this.setupStates()
        this.setupAIStates()
        this.setupTimers()
        this.setupAITimers()
        this.adjustImage()

    def setGaurdDefaults(this):
        #artifical intelligence variables
        this.AIType = "standing"    #type of AI will determine what the AI's goal is
        this.AIState = {}           #a dictionary of AI states
        this.AISpotDist = 10        #length to the center of blocks the AI can spot the player
        this.AIBroadcastDist = 15   #length to the center of blocks the AI can broadcast to other AI's
        this.AIDesiredLocation = this.getRect().copy()
        this.AILastSpotted = this.getRect().copy()
        this.testRect = None

        #character finite state variables
        this.isFacing = "right"     #the direction the character is facing
        this.postFacing = "right"   #the direction an AI faces when returning to post
        
        #character game variables
        this.healthMax = 1          #maximum number of health
        this.health = 1             #current health

        #character physics variables
        this.jumpForceX = 1.5       #how much X force is put into a jump
        this.jumpForceY = 4         #how much Y force is put into a jump
        this.runSpeed = 0.125       #how fast a character runs
        this.cautionSpeed = 0.25    #how fast an NPC goes durring caution
        this.alertSpeed = 0.50      #how fast an NPC goes durring alert
        this.maxSpeed = 1           #the maximum speed a character can achieve
        this.attackForce = 2        #how much force a character adds when they hit with an attack

        #character timer and triggers
        this.jumpTimeTrig = 15      #how long a jump lasts
        this.midJumpTimeTrig = 7    #how long before it is considered mid-jump
        this.attackTimeTrig = 10    #how long an attack lasts
        this.contAnimTimeTrig = 10  #how long a frame of continuous animation lasts
        this.singleAnimTimeTrig = 2 #how long a frame of a single animation lasts        
        this.jumpCool = 10          #how long before a character can jump again
        this.attackCool = 20        #how long before a character can attack again        
        this.useCool = 20           #how long before a character can use an item  
        this.hurtCool = 20          #how long before you can take damage again
        this.hurtEnd = 30           #how long you stay invincible
        this.deadEnd = 30           #how long your corpse lasts before it goes away
        this.cautionEnd = 75        #how long until the AI caution status ends
        this.alertEnd = 75          #how long until the AI alert status ends

        #gaurd sounds
        this.wavJump = pygame.mixer.Sound("sounds/effects/gaurdJump.wav")
        this.wavAttack = pygame.mixer.Sound("sounds/effects/gaurdAttack.wav")
        this.wavDeath = pygame.mixer.Sound("sounds/effects/gaurdDeath.wav")

    def setupAIStates(this):
        this.setAIState("normal", True)
        this.setAIState("caution", False)
        this.setAIState("alert", False)
        this.setAIState("atPost", True)

        #pathfinding booleans
        this.setAIState("botLeft", False)
        this.setAIState("lowLeft", False)
        this.setAIState("upLeft", False)
        this.setAIState("topLeft", False)
        this.setAIState("top", False)
        this.setAIState("topRight", False)
        this.setAIState("upRight", False)
        this.setAIState("lowRight", False)
        this.setAIState("botRight", False)
        this.setAIState("bottom", False)


    #sets up all timers that will be used to prevent errors
    def setupAITimers(this):      
        this.setTimer("cautionEnd", -1)
        this.setTimer("alertEnd", -1)
    

#------------------------------------------------------------------------------#
#                                                                              #
#                 Artificial Inteligence Finite State Machine                  #
#                                                                              #
#------------------------------------------------------------------------------#
    def checkAIState(this):
#------------------------------------------------------------------------------#
#                           Passive  State  Checker                            #
#------------------------------------------------------------------------------#
        #setup action string
        action = "idle"

        #if the character is in caution status
        #and enough time has passed to revert to normal status
        if this.checkTimer("cautionEnd")\
           and not this.getAIState("normal")\
           and this.getAIState("caution")\
           and not this.getAIState("alert"):
            this.setAIState("normal", True)
            this.setAIState("caution", False)
            this.setAIState("alert", False)

        #if the character is in alert status
        #and enough time has passed to revert to caution status          
        if this.checkTimer("alertEnd")\
           and not this.getAIState("normal")\
           and not this.getAIState("caution")\
           and this.getAIState("alert"):
            this.setAIState("normal", False)
            this.setAIState("caution", True)
            this.setAIState("alert", False)
            #setup a new timer for the caution status to remain in effect
            this.setTimer("cautionEnd", this.cautionEnd)

        """Before an AI goes to preform an action, we must ensure that the
        enviroment changes the state appropriately"""
        #see if the player is spotted durring the AI's Decision Making
        if not this.getState("isDead"):
            this.passivePerception()
#------------------------------------------------------------------------------#
#                               State  Checker                                 #
#------------------------------------------------------------------------------#

        #If things are normal
        if this.getAIState("normal")\
           and not this.getAIState("caution")\
           and not this.getAIState("alert"):
            #The AI Returns to its normal task (based on AI type)
            action = "normal"

        #If things under caution
        if not this.getAIState("normal")\
           and this.getAIState("caution")\
           and not this.getAIState("alert"):
            #The AI is cautiously searching for the player
            action = "caution"
   
        #If things under alert
        if not this.getAIState("normal")\
           and not this.getAIState("caution")\
           and this.getAIState("alert"):
            #The AI is actively hunting the player at the last known location
            action = "alert"

        #print("AI Action :: ", action)

        #based on which state the AI is supposed to be in, run the action
        this.actionAI(action)

        
#------------------------------------------------------------------------------#
#                                                                              #
#                                 AI  Actions                                  #
#                                                                              #
#------------------------------------------------------------------------------#

    #this runs the action result of the AI finite state machine
    def actionAI(this, action):
#------------------------------------------------------------------------------#
#                              Normal  Actions                                 #
#------------------------------------------------------------------------------#
        if action == "normal":
            #if we are not at our post
            if not this.getAIState("atPost"):
                #return to the post
                this.returnToPost()
            #if we are at our post
            elif this.getAIState("atPost"):
                #resume action based on type
                if this.AIType == "standing":
                    #just stand there and look pretty
                    this.recieveCommand("idle")
                elif this.AIType == "walking":
                    pass
                elif this.AIType == "jumping":
                    pass


        
#------------------------------------------------------------------------------#
#                             Caution  Actions                                 #
#------------------------------------------------------------------------------#
        elif action == "caution":
            this.moveToTarget(this.AILastSpotted)

        elif action == "alert":
            this.moveToTarget(this.AILastSpotted)
            
#------------------------------------------------------------------------------#
#                               Alert  Actions                                 #
#------------------------------------------------------------------------------#




#------------------------------------------------------------------------------#
#                                 AI  Methods                                  #
#------------------------------------------------------------------------------#

    #the AI's ability to distingush the player if they are paying attention or not
    def passivePerception(this):
        #create a references to reduce code bloat
        block = this.game.getBlockScale()
        player = this.game.getPlayer()
        #create duplicates of the character's rect
        spotRect = this.getRect().copy()
        proximityRect = this.getRect().copy()
        #create a temporary reference to the character's spot distance
        #based on which status the enemy is in
        if this.getAIState("normal"):
            spotDist = (block * this.AISpotDist) // 2   
        elif this.getAIState("caution"):
            spotDist = (block * this.AISpotDist)
        elif this.getAIState("alert"):
            spotDist = (block * this.AISpotDist) // (3/4)
        #adjust the size of the spot rect to the length of the sight
        spotRect.inflate_ip(spotDist, -block)
        #adjust the size of the proximity rect to the area around the character
        proximityRect.inflate_ip(block // 4, block // 4)
        #move the spot rect half of the spot length to the right/left
        #and to where the character can see
        if this.isFacing == "right":
            spotRect.move_ip(spotDist // 2, (-block // 2))
        elif this.isFacing == "left":
            spotRect.move_ip(-spotDist // 2, (-block // 2))
            
        #((if the spot rect is colliding with the Player and the
        #spot rect is not obsured with terrain objects)
        #or if the player is within close enough proximity)
        #but also player is not taking damage (so they have a chance to escape)
        if (spotRect.colliderect(player.getRect())\
            and not this.checkObstructions())\
                or (proximityRect.colliderect(player.getRect()))\
                and not player.getState("isHurt")\
                and not player.getState("isDead"):
                    this.setAIState("normal", False)
                    this.setAIState("caution", False)
                    this.setAIState("alert", True)
                    this.setAIState("atPost", False)
                    this.runSpeed = this.alertSpeed
                    this.setTimer("alertEnd", this.alertEnd)
                    this.AILastSpotted = player.getRect().inflate(\
                        -(block //2), -block)
                    this.sendBroadcast()
            

    #send a broadcast to all nearby characters
    def sendBroadcast(this):
        #create a duplicate of the character's rect
        broadcastRect = this.getRect().copy()
        #adjust the size of the broadcast rect to the length of the 
        #broadcastRect.inflate_ip(this.AIBroadcastDist, (this.AIBroadcastDist // 2))
        broadcastRect.inflate_ip(this.AIBroadcastDist * this.game.getBlockScale(),\
                                 (this.AIBroadcastDist * this.game.getBlockScale())\
                                 - this.game.getBlockScale())
        #loop through each NPC
        for ally in this.game.getNPCSprites():
            #ensure we are not giving ourself a command
            if not ally == this:
                #If the ally is within broadcast range
                if broadcastRect.colliderect(ally.getRect()):
                    #If the ally is not already in alert
                    if not ally.getAIState("alert"):
                        #set the ally to be cautious
                        ally.setAIState("normal", False)
                        ally.setAIState("caution", True)
                        ally.setAIState("alert", False)
                        ally.setAIState("atPost", False)
                        ally.runSpeed = ally.cautionSpeed
                        ally.setTimer("cautionEnd", ally.cautionEnd)
                        #send the location last spotting to the AI
                        ally.AILastSpotted = this.AILastSpotted.copy()

    def checkObstructions(this):
        #create references to reduce code bloat
        block = this.game.getBlockScale()
        halfBlock = block // 2
        playerRect = this.game.getPlayer().getRect().copy()
        thisRect = this.getRect().copy()

        #create a line of sight rectangle between the NPC and the player
        if this.isFacing == "left":
            lineOfSightRect = pygame.Rect(playerRect.left + halfBlock, thisRect.top,\
                                   ((thisRect.right - halfBlock) - (playerRect.left + halfBlock))\
                                   , block)

        #create a line of sight rectangle between the NPC and the player
        elif this.isFacing == "right":
            lineOfSightRect = pygame.Rect(thisRect.right - halfBlock, thisRect.top,\
                                   ((playerRect.right - halfBlock) - (thisRect.left + halfBlock))\
                                   , block)

        #loop through every block of terrain
        for terrain in this.game.getTerrainSprites():
            #if the terrain cannot be passed through
            if terrain.density > 0:
                #if the line of sight collides with a terrain object
                if lineOfSightRect.colliderect(terrain.getRect()):
                    #there is an obstruction in sight return true
                    return True

        #if we managed to get through every colideable terrain object with
        # no obstructions... then return false, there is no obstructions
        return False
        
    def moveToTarget(this, target):
        #check to see if the player is within attacking range
        if not this.checkAttack():        
            #check the area around us to see where we can go
            this.checkArea()
            
            #if the target is above the AI
            if target.bottom < this.getRect().top:
                this.moveToTop(target)

            #if the target is below the AI
            elif target.top > this.getRect().bottom:
                this.moveToBottom(target)

            #if the target is neither above or below the target
            elif not target.bottom < this.getRect().top\
                 and not target.top > this.getRect().bottom:
                
                #if the target is to the left of the AI
                if target.right < this.getRect().left:
                    this.moveToLeft(target)
                #if the player was last spotted to the right of the AI
                elif target.left > this.getRect().right:
                    this.moveToRight(target)

    #check to see if the player is within range to attack, then attack
    def checkAttack(this):
        #create a references to reduce code bloat
        block = this.game.getBlockScale()
        player = this.game.getPlayer()
        #create a duplicate of the character's rect
        attackRect = this.getRect().copy()
        #reduce it to a size of a block
        attackRect.inflate_ip(0, -block)
        
        if this.isFacing == "right":
            #move the damage rect a block length to the right
            attackRect.move_ip((block - block//4), 0)
        elif this.isFacing == "left":
            #move the damage rect a block length to the left
            attackRect.move_ip(-(block - block//4), 0)
            
        if attackRect.colliderect(player.getRect())\
           and not player.getState("isDead"):
            #if we are debugging the game
            if this.game.debugMode:
                this.testRect = attackRect.copy()
            this.recieveCommand("attack")
            return True
        #if the NPC is not within attacking range, or the player is dead
        else:
            return False

    #checks the area round the AI to help with pathfinding
    def checkArea(this):
        block = this.game.getBlockScale()
        halfBlock = block // 2
        quarterBlock = block // 4

        #if we are debugging the game
        if this.game.debugMode:
            this.testRect = pygame.Rect(this.getRect().left,\
                               this.getRect().top + halfBlock,\
                               block, block)
            this.testRect.inflate_ip(block , block + halfBlock)

        #loop through each direction
        for idx in range(1,10):
            #create a rect in the middle of the AI
            leadRect = pygame.Rect(this.getRect().left,\
                                   this.getRect().top + halfBlock,\
                                   block, block)
            #take a little bit off the boarders of the rect
            leadRect.inflate_ip(-quarterBlock, -quarterBlock)

            #bottom left
            if idx == 1:
                leadRect.move_ip(-block, block + halfBlock)
            #lower left
            elif idx == 2:
                leadRect.move_ip(-block, halfBlock)
            #upper left
            elif idx == 3:
                leadRect.move_ip(-block, -halfBlock)
            #top left
            elif idx == 4:
                leadRect.move_ip(-block, -(block + halfBlock))
            #top
            elif idx == 5:
                leadRect.move_ip( 0 , -(block + halfBlock))
            #top right
            elif idx == 6:
                leadRect.move_ip(block , -(block + halfBlock))
            #upper right
            elif idx == 7:
                leadRect.move_ip(block, -halfBlock)
            #lower right
            elif idx == 8:
                leadRect.move_ip(block, halfBlock)
            #bottom right
            elif idx == 9:
                leadRect.move_ip(block, block + halfBlock)
            #bottom
            elif idx == 10:
                leadRect.move_ip( 0 , block + halfBlock)

            #if there is no occupying square
            if this.checkEmpty(leadRect):
                #bottom left is empty
                if idx == 1:
                    this.setAIState("botLeft", True)
                #lower left is empty
                elif idx == 2:
                    this.setAIState("lowLeft", True)
                #upper left is empty
                elif idx == 3:
                    this.setAIState("upLeft", True)
                #top left is empty
                elif idx == 4:
                    this.setAIState("topLeft", True)
                #top is empty
                elif idx == 5:
                    this.setAIState("top", True)
                #top right is empty
                elif idx == 6:
                    this.setAIState("topRight", True)
                #upper right is empty
                elif idx == 7:
                    this.setAIState("upRight", True)
                #lower right is empty
                elif idx == 8:
                    this.setAIState("lowRight", True)
                #bottom right is empty
                elif idx == 9:
                    this.setAIState("botRight", True)
                #bottom is empty
                elif idx == 10:
                    this.setAIState("bottom", True)
                    
            #if the leading rect is full
            else:
                #bottom left is full
                if idx == 1:
                    this.setAIState("botLeft", False)
                #lower left is full
                elif idx == 2:
                    this.setAIState("lowLeft", False)
                #upper left is full
                elif idx == 3:
                    this.setAIState("upLeft", False)
                #top left is full
                elif idx == 4:
                    this.setAIState("topLeft", False)
                #top is full
                elif idx == 5:
                    this.setAIState("top", False)
                #top right is full
                elif idx == 6:
                    this.setAIState("topRight", False)
                #upper right is full
                elif idx == 7:
                    this.setAIState("upRight", False)
                #lower right is full
                elif idx == 8:
                    this.setAIState("lowRight", False)
                #bottom right is full
                elif idx == 9:
                    this.setAIState("botRight", False)
                #bottom is full
                elif idx == 10:
                    this.setAIState("bottom", False)

    #if the AI is trying to move to the left
    def moveToLeft(this, target):
        #if there is no gaps and no wall to the left    
        if not this.getAIState("botLeft")\
           and this.getAIState("lowLeft")\
           and this.getAIState("upLeft"):
            this.recieveCommand("goLeft")           
        #if there is a gap and no wall to the left    
        elif this.getAIState("botLeft")\
           and this.getAIState("lowLeft")\
           and this.getAIState("upLeft")\
           and this.getAIState("topLeft"):
            this.isFacing = "left"
            this.recieveCommand("jump")
        #if there is a block on either part of the left side
        #but there is a space to the top left and above us
        elif (not this.getAIState("lowLeft")\
              or not this.getAIState("upLeft"))\
              and this.getAIState("topLeft")\
              and this.getAIState("top"):
            this.isFacing = "left"
            this.recieveCommand("jump")
        #if there is a block on either part of the left side
        #and there is not space to the top left and above us 
        elif (not this.getAIState("lowLeft")\
              or not this.getAIState("upLeft"))\
              and (not this.getAIState("topLeft")\
                   or this.getAIState("top")):
            
            #add in a wall pathfinding function here
            this.recieveCommand("goRight")

    #if the AI is trying to move to the right
    def moveToRight(this, target):
        #if there is no gaps and no wall to the left    
        if not this.getAIState("botRight")\
           and this.getAIState("lowRight")\
           and this.getAIState("upRight"):
            this.recieveCommand("goRight")   
        #if there is a gap and no wall to the Right    
        elif this.getAIState("botRight")\
           and this.getAIState("lowRight")\
           and this.getAIState("upRight")\
           and this.getAIState("topRight"):
            this.isFacing = "right"
            this.recieveCommand("jump")
        #if there is a block on either part of the Right side
        #but there is a space to the top Right and above us
        elif (not this.getAIState("lowRight")\
              or not this.getAIState("upRight"))\
              and this.getAIState("topRight")\
              and this.getAIState("top"):
            this.isFacing = "right"
            this.recieveCommand("jump")
        #if there is a block on either part of the Right side
        #and there is not space to the top Right and above us 
        elif (not this.getAIState("lowRight")\
              or not this.getAIState("upRight"))\
              and (not this.getAIState("topRight")\
                   or this.getAIState("top")):
            
            #add in a wall pathfinding function here
            this.recieveCommand("goLeft")

    #If the AI is trying to move below
    def moveToBottom(this, target):
        #if there is a platform below the AI
        if not this.getAIState("bottom"):
            #if there is a gap, AI will face the gap's direction
            if this.pathfinding("platformBelow", target):
                if this.isFacing == "left":
                    this.moveToLeft(target)
                elif this.isFacing == "right":
                    this.moveToRight(target)
            #if there is not a gap below the AI
            else:
                #if the target is to the left of the AI
                if target.right < this.getRect().left:
                    this.moveToLeft(target)
                #if the player was last spotted to the right of the AI
                elif target.left > this.getRect().right:
                    this.moveToRight(target)
        #if there is not a platform below the AI
        else:
            #if the target is to the left of the AI
            if target.right < this.getRect().left:
                this.moveToLeft(target)
            #if the player was last spotted to the right of the AI
            elif target.left > this.getRect().right:
                this.moveToRight(target)

    def moveToTop(this, target):
        #if there is not a platform above the AI
        if this.getAIState("top"):
            #if there is a gap, AI will face the gap's direction
            if this.pathfinding("platformAbove", target):
                #If the AI is facing left and there is space to jump
                if this.isFacing == "left":
                    #if there is space to jump
                    if this.getAIState("topLeft"):
                        this.recieveCommand("jump")
                    #if there is no space to jump..
                    else:
                        #move to the opposite direction
                        this.moveToRight(target)
                #If the AI is facing right and there is space to jump
                elif this.isFacing == "right":
                    #if there is space to jump
                    if this.getAIState("topRight"):
                        this.recieveCommand("jump")
                    #if there is no space to jump
                    else:
                        #move to the opposite direction
                        this.moveToLeft(target)
            #if there is not a gap above the AI
            else:
                #if the target is to the left of the AI
                if target.right < this.getRect().left:
                    this.moveToLeft(target)
                #if the target is to the right of the AI
                elif target.left > this.getRect().right:
                    this.moveToRight(target)
        #if there is a platform above the AI
        else:
            #if the target is to the left of the AI
            if target.right < this.getRect().left:
                this.moveToLeft(target)
            #if the target is to the right of the AI
            elif target.left > this.getRect().right:
                this.moveToRight(target)
                

    #pathfinding method to help the AI get to where it needs to go
    def pathfinding(this, action, target):
        block = this.game.getBlockScale()

        if action == "platformBelow":
            #loop through a 7 block platform size
            for testVar in range (1, 7):
                leftRect = pygame.Rect((this.getRect().centerx - (block // 2),\
                                        this.getRect().centery),\
                                        (block // 2, block // 2))
                rightRect = leftRect.copy()
                
                leftRect.move_ip(-((block // 4) + (block * testVar)), (block // 4) + block)
                rightRect.move_ip(((block // 4) + (block * testVar)), (block // 4) + block)

                #if we are debugging the game
                if this.game.debugMode:
                    this.testRect = pygame.Rect.union(leftRect, rightRect)

                #check the side if where the target is first
                #if the target is to the left of the AI
                if target.right < this.getRect().left: 
                    if this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True
                    elif this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                #if the target to the right of the AI
                elif target.left > this.getRect().right:
                    if this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                    elif this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True
                #if neither are true... check the right first
                else:
                    if this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                    elif this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True

            #if we went through the entire loop and did not find a gap....
            return False        

        elif action == "platformAbove":
            #loop through a 7 block platform size
            for testVar in range (1, 7):
                leftRect = pygame.Rect((this.getRect().centerx - (block // 2),\
                                        this.getRect().centery),\
                                        (block // 2, block // 2))
                rightRect = leftRect.copy()
                
                leftRect.move_ip(-((block // 4) + (block * testVar)), -(block // 4) - block)
                rightRect.move_ip(((block // 4) + (block * testVar)), -(block // 4) - block)

                #if we are debugging the game
                if this.game.debugMode:
                    this.testRect = pygame.Rect.union(leftRect, rightRect)

                #check the side if where the target is first
                #if the target is to the left of the AI
                if target.right < this.getRect().left: 
                    if this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True
                    elif this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                #if the target to the right of the AI
                elif target.left > this.getRect().right:
                    if this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                    elif this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True
                #if neither are true... check the right first
                else:
                    if this.checkEmpty(rightRect):
                        this.isFacing == "right"
                        return True
                    elif this.checkEmpty(leftRect):
                        this.isFacing == "left"
                        return True
            #if we went through the entire loop and did not find a gap to jump up....
            return False
        

        #return false if nothing applies
        print(this.getName(), " :: Pathfinding command '", action, "' does not exist")
        return False

    def returnToPost(this):
        this.moveToTarget(this.AIDesiredLocation.copy())

        #create a rect for the AI to get inside
        post = this.AIDesiredLocation.copy()
        post.inflate_ip(this.game.getBlockScale() // 4,\
                        this.game.getBlockScale() // 4)

        #if the AI is inside of the desired Post Location
        if post.contains(this.getRect()):
            #make the AI stay put and face the correct direction
            this.speedX = 0
            this.speedY = 0
            this.isFacing = this.postFacing
            this.setAIState("atPost", True)
            this.recieveCommand("idle")

    def checkEmpty(this, tRect):
        for tObject in this.game.getTerrainSprites():
            if not tObject == this and tObject.density <= 0\
               and tRect.colliderect(tObject.getRect()):
                #if the rect collides with a terrain block return false
                return True
        #if the rect does not collide with any terrain, return true
        return False

    def checkFull(this, tRect):
        for tObject in this.game.getTerrainSprites():
            if not tObject == this and tObject.density > 0\
               and tRect.colliderect(tObject.getRect()):
                #if the rect collides with a terrain block return false
                return True
        #if the rect does not collide with any terrain, return true
        return False

#------------------------------------------------------------------------------#
#                               AI State Methods                               #
#------------------------------------------------------------------------------#

    #adds a character state if it does not exist. Then, sets the state to the
    #input boolean
    def setAIState(this, stateName, boolean):
        this.AIState[stateName] = boolean

    #checks the character state
    def getAIState(this, stateName):
        #check to see if the state exists in the dictionary
        if not this.AIState.get(stateName) == None:    
            #check to see if enough timer has passed on the timer to trigger an event
            return this.AIState[stateName]

        elif this.AIState.get(stateName) == None:
            print(this.getName(), " :: AI State -", stateName, "- has not been created yet")
            return False

#------------------------------------------------------------------------------#
#                             Image and Animation                              #
#------------------------------------------------------------------------------#

    #A method so that the player can be drawn without being in a sprite group
    def draw(this, screen):

        #If we are trying to debug the game
        if this.game.debugMode:
            #draw out spotted rects for testing purpouses
            pygame.draw.rect(this.game.getDisplay(), this.game.getColor("red"), this.AILastSpotted, 0)
            pygame.draw.rect(this.game.getDisplay(), this.game.getColor("green"), this.AIDesiredLocation, 0)
            if not this.testRect == None:
                pygame.draw.rect(this.game.getDisplay(), this.game.getColor("blue"), this.testRect, 0)

        
        #Flips the image if the player is facing left and crops images accordingly
        if this.isFacing == "right":
            #a rectangle used for cropping the player image
            cropRect = this.getImage().get_rect()
            cropRect = pygame.Rect(\
                cropRect.left, cropRect.top, \
                cropRect.width - this.imageOffsetX, \
                cropRect.height + this.imageOffsetY)
            #put the croped image on screen
            screen.blit(this.getImage(), this.getRect(), cropRect)

        elif this.isFacing == "left":
            #a rectangle used for cropping the player image
            cropRect = this.getImage().get_rect()
            cropRect = pygame.Rect(\
                cropRect.left, cropRect.top, \
                cropRect.width - this.imageOffsetX, \
                cropRect.height + this.imageOffsetY)
            this.getImage().scroll(this.game.getBlockScale(), 0)
            #put the cropped image on screen
            screen.blit(pygame.transform.flip(this.getImage(), True, False),\
                        this.rect, cropRect)



