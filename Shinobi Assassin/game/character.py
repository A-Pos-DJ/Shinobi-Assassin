import pygame
from gameObject import GameObject


#Object class that derives from game object to represent people
class Character(GameObject):

    def __init__(this, name, image, posX, posY, sizeX, sizeY, density, mass):
        super().__init__(name, image, posX, posY, sizeX, sizeY)
        this.density = density
        this.mass = mass

        
#------------------------------------------------------------------------------#
#                                                                              #
#                              Class  Attributes                               #
#                                                                              #
#------------------------------------------------------------------------------#

        #character game attributes
        this.healthMax = int(0)         #maximum number of health
        this.health = int(0)            #current health

        #character image variables
        this.tempImage ="imageObj"      #storage for an image when blinking
        this.imageOffsetX = int(0)      #how much an image needs to be adjusted on the X axis
        this.imageOffsetY = int(0)      #how much an image needs to be adjusted on the Y axis

        #character finite state variables
        this.isFacing = str("0")        #the direction the character is facing
        this.state = {}                 #a dictionary of character states

        #character animation states
        this.idleAnim = []              #idle animation boolean list
        this.useAnim = []               #use animation boolean list
        this.runAnim = []               #run animation boolean list
        this.attackAnim = []            #attack animation boolean list
        this.deathAnim = []             #death animation boolean list

        #character physics variables
        this.jumpForceX = float(0)      #how much X force is put into a jump
        this.jumpForceY = float(0)      #how much Y force is put into a jump
        this.runSpeed = float(0)        #how fast a character runs
        this.maxSpeed = float(0)        #the maximum speed a character can achieve
        this.attackForce = float(0)     #how much force a character adds when they hit with an attack
        this.speedX = float(0)          #the current X speed of the character
        this.speedY = float(0)          #the current Y speed of the character

        #character timer and triggers
        this.timers = {}                #a dictonary of timer names and the number represented
        this.jumpTimeTrig = int(0)      #how long a jump lasts
        this.midJumpTimeTrig = int(0)   #how long before it is considered mid-jump
        this.attackTimeTrig = int(0)    #how long an attack lasts
        this.attackEffectTrig = int(0)  #how long into an attack the actual attack happens
        this.contAnimTimeTrig = int(0)  #how long a frame of continuous animation lasts
        this.singleAnimTimeTrig = int(0)#how long a frame of a single animation lasts
        this.jumpCool = int(0)          #how long before a character can jump again
        this.attackCool = int(0)        #how long before a character can attack again        
        this.useCool = int(0)           #how long before a character can use an item        
        this.hurtCool = int(0)          #how long before you can take damage again
        this.deadEnd = int(0)           #how long your corpse lasts before it goes away
        this.blinkEnd = int(0)          #how long the character disappears durring blink animation

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
        this.setupStates()
        this.setupTimers()

    #sets up all timers that will be used to prevent errors
    def setupTimers(this):      
        this.setTimer("contAnim", -1)
        this.setTimer("singleAnim", -1)
        this.setTimer("action", -1)
        this.setTimer("midJump", -1)
        this.setTimer("jumpCool", -1)
        this.setTimer("attackEffect", -1)
        this.setTimer("attackCool", -1)
        this.setTimer("useCool", -1)
        this.setTimer("hurtCool", -1)
        this.setTimer("deadEnd", -1)
        this.setTimer("blinkEnd", -1)


    def setupStates(this):
        this.setState("isIdle", True)
        this.setState("isRunning", False)
        this.setState("isJumping", False)
        this.setState("isAttacking", False)
        this.setState("isUsing", False)
        this.setState("isHurt", False)
        this.setState("isDead", False)
        this.setState("inMidAction", False)
        this.setState("alreadyHit", False)
        this.setState("alreadyHurt", False)
        this.setState("blink", False)
        this.setState("blinkOn", False)

    def setCharacterDefaults(this):
        #character game attributes
        this.healthMax = 6          #maximum number of health
        this.health = 6             #current health

        #character image variables
        this.tempImage = "imageObj" #storage for an image when blinking
        this.imageOffsetX = this.game.getBlockScale()
        this.imageOffsetY = 0       #how much an image needs to be adjusted on the Y axis

        #character finite state variables
        this.isFacing = "right"     #the direction the character is facing
        this.state = {}             #a dictionary of character states

        #character animation states
        this.idleAnim = [True, False, False, False, False, False, False, False, False, False]
        this.useAnim = [True, False, False, False, False, False, False, False, False, False]
        this.runAnim = [True, False, False, False, False, False, False, False, False, False]
        this.attackAnim = [True, False, False, False, False, False, False, False, False, False]
        this.deathAnim = [True, False, False, False, False, False, False, False, False, False]

        #character physics variables
        this.jumpForceX = 1.5       #how much X force is put into a jump
        this.jumpForceY = 4         #how much Y force is put into a jump
        this.runSpeed = 0.5         #how fast a character runs
        this.maxSpeed = 2           #the maximum speed a character can achieve
        this.attackForce = 2        #how much force a character adds when they hit with an attack
        this.speedX = 0             #the current X speed of the character
        this.speedY = 0             #the current Y speed of the character

        #character timer and triggers
        this.timers = {}            #a dictonary of timer names and the number represented
        this.jumpTimeTrig = 15      #how long a jump lasts
        this.midJumpTimeTrig = 7    #how long before it is considered mid-jump
        this.attackTimeTrig = 10    #how long an attack lasts
        this.attackEffectTrig = 6   #how long into an attack the actual attack happens
        this.contAnimTimeTrig = 10  #how long a frame of continuous animation lasts
        this.singleAnimTimeTrig = 2 #how long a frame of a single animation lasts        
        this.jumpCool = 20          #how long before a character can jump again
        this.attackCool = 20        #how long before a character can attack again        
        this.useCool = 20           #how long before a character can use an item  
        this.hurtCool = 50          #how long before you can take damage again
        this.hurtEnd = 30           #how long you stay invincible
        this.deadEnd = 35           #how long your corpse lasts before it goes away
        this.blinkEnd = 3           #how long the character disappears durring blink animation
        
#------------------------------------------------------------------------------#
#                                                                              #
#                       Character  Command  Reciever                           #       
#                                                                              #
#------------------------------------------------------------------------------#

    #takes the command recieved from either player inputs or from computer
    #AI and then adjusts the state of the character to match their command
    def recieveCommand(this, command):

        if command == "idle":
            if not this.getState("inMidAction"):
                this.setState("isIdle", True)
                this.setState("isRunning", False)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
            elif this.getState("inMidAction"):
                pass
            
        elif command == "goLeft":
            if not this.getState("inMidAction"):
                this.isFacing = "left"
                this.setState("isIdle", False)
                this.setState("isRunning", True)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
            elif this.getState("inMidAction"):
                pass
            
        elif command == "goRight":
            if not this.getState("inMidAction"):
                this.isFacing = "right"
                this.setState("isIdle", False)
                this.setState("isRunning", True)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
            elif this.getState("inMidAction"):
                pass
            
        elif command == "goUp":
            pass
        
        elif command == "goDown":
            pass
        
        elif command == "jump":
            if not this.getState("inMidAction"):
                if this.checkGrounded():
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", True)
                    this.setState("isAttacking", False)
                    this.setState("isUsing", False)
                else:
                    pass
            elif this.getState("inMidAction"):
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", True)
                    this.setState("isAttacking", False)
                    this.setState("isUsing", False)
                    
        elif command == "attack":
            if not this.getState("inMidAction"):
                if this.checkGrounded():
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", False)
                    this.setState("isAttacking", True)
                    this.setState("isUsing", False)
                else:
                    pass
            elif this.getState("inMidAction"):
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", False)
                    this.setState("isAttacking", True)
                    this.setState("isUsing", False)
                    
        elif command == "using":
            if not this.getState("inMidAction"):
                if this.checkGrounded():
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", False)
                    this.setState("isAttacking", False)
                    this.setState("isUsing", True)
                else:
                    pass
            elif this.getState("inMidAction"):
                    this.setState("isIdle", False)
                    this.setState("isRunning", False)
                    this.setState("isJumping", False)
                    this.setState("isAttacking", False)
                    this.setState("isUsing", True)
        
        #if not this.getName() == "Player":        
            #print(this.getName(), " :: Command: ", command)
                    

#------------------------------------------------------------------------------#
#                                                                              #
#                        Character Finite State Machine                        #       
#                                                                              #
#------------------------------------------------------------------------------#
    #this is basically a finite state machine checker
    def checkState(this):

        #check to see if the player is dead, set the death state to be true
        if this.health <= 0\
           and not this.getState("isDead"):
            this.setState("isDead", True)
            this.setState("inMidAction", False)
            #ensure the character is not blinking durring death
            this.setState("blink", False)

        #isIdle
        if this.getState("isIdle")\
        and not this.getState("isRunning")\
        and not this.getState("isJumping")\
        and not this.getState("isAttacking")\
        and not this.getState("isUsing")\
        and not this.getState("isDead"):
            if not this.getState("inMidAction"):
                action = "idle"
            elif this.getState("inMidAction"):
                action = "midAction"

        #isRunning
        if not this.getState("isIdle")\
        and this.getState("isRunning")\
        and not this.getState("isJumping")\
        and not this.getState("isAttacking")\
        and not this.getState("isUsing")\
        and not this.getState("isDead"):
            if not this.getState("inMidAction"):
                action = "toRun"
            elif this.getState("inMidAction"):
                action = "midAction"

        #isJumping        
        if not this.getState("isIdle")\
        and not this.getState("isRunning")\
        and this.getState("isJumping")\
        and not this.getState("isAttacking")\
        and not this.getState("isUsing")\
        and not this.getState("isDead"):
            if not this.getState("inMidAction"):
                if this.checkTimer("jumpCool"):
                    action = "toJump"
                elif not this.checkTimer("jumpCool"):
                    action = "idle"
            elif this.getState("inMidAction"):
                action = "midJump"

        #isAttacking
        if not this.getState("isIdle")\
        and not this.getState("isRunning")\
        and not this.getState("isJumping")\
        and  this.getState("isAttacking")\
        and not this.getState("isUsing")\
        and not this.getState("isDead"):
            if not this.getState("inMidAction"):
                if this.checkTimer("attackCool"):
                    action = "toAttack"
                elif not this.checkTimer("attackCool"):
                    action = "idle"
            elif this.getState("inMidAction"):
                action = "midAttack"

        #isUsing
        if not this.getState("isIdle")\
        and not this.getState("isRunning")\
        and not this.getState("isJumping")\
        and not this.getState("isAttacking")\
        and this.getState("isUsing")\
        and not this.getState("isDead"):
            if not this.getState("inMidAction"):
                if this.checkTimer("useCool"):
                    action = "toUse"
                elif not this.checkTimer("useCool"):
                    action = "idle"
            elif this.getState("inMidAction"):
                action = "midUse"

        #isHurt
        if this.getState("isHurt")\
        and not this.getState("isDead"):
            if not this.getState("alreadyHurt"):
                action = "toHurt"
            elif this.checkTimer("hurtCool"):
                #character is no longer considered hurt
                this.setState("isHurt", False)
                #can take damage again
                this.setState("alreadyHurt", False)
                #remove flashing effect
                this.setState("blink", False)

        #isDead
        if this.getState("isDead"):
            if not this.getState("inMidAction"):
                action = "toDeath"
            if this.getState("inMidAction"):
                action = "midDeath"

        """
        if not this.getName() == "Player":
            print(this.getName(), " :: Action: ", action)
        """
        
        if not this.game.getVictory():
            #based on which state the character is supposed to be in, run the action
            this.action(action)
        elif this.game.getVictory():
            if not this == this.game.getPlayer():
                if not action == "toDeath"\
                   or not action == "midDeath":
                    action = "idle"
            else:
                action = "idle"
            this.speedX = 0
            this.speedY = 0
            this.action(action)


#------------------------------------------------------------------------------#
#                                                                              #
#                             Character  Actions                               #
#                                                                              #
#------------------------------------------------------------------------------#

    #this runs the action result of the finite state machine
    def action(this, action):
#------------------------------------------------------------------------------#
#                                Idle  Actions                                 #
#------------------------------------------------------------------------------#
        if action == "idle":
            this.setState("isIdle", True)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", False)
            this.setState("isUsing", False)
            this.animateActionCont(this.idleAnim, this.imgIdle)


#------------------------------------------------------------------------------#
#                                 Run  Actions                                 #
#------------------------------------------------------------------------------#
        if action == "toRun":
            this.setState("isIdle", False)
            this.setState("isRunning", True)
            this.setState("isJumping", False)
            this.setState("isAttacking", False)
            this.setState("isUsing", False)
            
            if this.isFacing == "right":
                if abs(this.speedX) < this.maxSpeed or this.speedX < 0:
                    this.addForce(this.runSpeed,0)
            elif this.isFacing == "left":
                if abs(this.speedX) < this.maxSpeed or this.speedX > 0:
                    this.addForce(-this.runSpeed,0)
            this.animateActionCont(this.runAnim, this.imgRun)      

#------------------------------------------------------------------------------#
#                                 Jump  Actions                                #
#------------------------------------------------------------------------------#
        if action == "toJump":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", True)
            this.setState("isAttacking", False)
            this.setState("isUsing", False)
            
            if this.isFacing == "right":
                this.addForce(this.jumpForceX, -this.jumpForceY - (this.game.gravity / 2))
            elif this.isFacing == "left":
                this.addForce(-this.jumpForceX, -this.jumpForceY - (this.game.gravity / 2))
                
            this.setState("inMidAction", True)
            this.setTimer("action", this.jumpTimeTrig)
            this.setTimer("midJump", this.midJumpTimeTrig)
            #if there is not a game over...
            if not this.game.getGameOver():
                #play the jump sound
                pygame.mixer.Sound.play(this.wavJump)
            this.animateActionCont(this.runAnim, this.imgRun)


        if action == "midJump":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", True)
            this.setState("isAttacking", False)
            this.setState("isUsing", False)
            this.animateActionCont(this.runAnim, this.imgRun)

            if this.checkTimer("midJump")\
               and this.checkGrounded():
                this.setState("isIdle", True)
                this.setState("isRunning", False)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
                this.setState("inMidAction", False)
                this.speedX = 0
                this.setTimer("jumpCool", this.jumpCool)
            
            if this.checkTimer("action"):
                this.setState("isIdle", True)
                this.setState("isRunning", False)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
                this.setState("inMidAction", False)
                this.setTimer("jumpCool", this.jumpCool)

#------------------------------------------------------------------------------#
#                               Attack  Actions                                #
#------------------------------------------------------------------------------#
        if action == "toAttack":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", True)
            this.setState("isUsing", False)

            this.setState("inMidAction", True)
            this.setTimer("action", this.attackTimeTrig)
            this.setTimer("attackEffect", this.attackEffectTrig)
            this.resetAnimationSequence(this.attackAnim)
            this.animateActionSingle(this.attackAnim, this.imgAttack)

        if action == "midAttack":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", True)
            this.setState("isUsing", False)
            this.animateActionSingle(this.attackAnim, this.imgAttack)

            if this.checkTimer("attackEffect"):
                #if there is not a game over...
                if not this.game.getGameOver():
                    #play the attack sound
                    pygame.mixer.Sound.play(this.wavAttack)
                this.attack()

            if this.checkTimer("action"):
                this.setState("isIdle", True)
                this.setState("isRunning", False)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
                this.setState("inMidAction", False)
                this.setState("alreadyHit", False)
                this.setTimer("attackCool", this.attackCool)

#------------------------------------------------------------------------------#
#                                Use  Actions                                  #
#------------------------------------------------------------------------------#
        if action == "toUse":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", True)
            this.setState("isUsing", False)
            
            if this.isFacing == "right":
                pass
                #this.addForce(this.jumpForceX, -this.jumpForceY - (this.game.gravity / 2))
            elif this.isFacing == "left":
                pass
                #this.addForce(-this.jumpForceX, -this.jumpForceY - (this.game.gravity / 2))
                
            this.setState("inMidAction", True)
            this.setTimer("action", this.useTimeTrig)
            this.resetAnimationSequence(this.useAnim)
            this.animateActionSingle(this.useAnim, this.imgUse)

        if action == "midUse":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", True)
            this.setState("isUsing", False)
            this.animateActionSingle(this.useAnim, this.imgUse)
            
            if this.checkTimer("action"):
                this.setState("isIdle", True)
                this.setState("isRunning", False)
                this.setState("isJumping", False)
                this.setState("isAttacking", False)
                this.setState("isUsing", False)
                this.setState("inMidAction", False)
                this.setTimer("useCool", this.useCool)

#------------------------------------------------------------------------------#
#                                 Hurt  Actions                                #
#------------------------------------------------------------------------------#
        if action == "toHurt":
            this.setTimer("hurtCool", this.hurtCool)
            this.takeDamage()
            #start flashing effect
            this.setState("blink", True)


#------------------------------------------------------------------------------#
#                                Death  Actions                                #
#------------------------------------------------------------------------------#
        if action == "toDeath":
            this.setState("isIdle", False)
            this.setState("isRunning", False)
            this.setState("isJumping", False)
            this.setState("isAttacking", False)
            this.setState("isUsing", False)
            this.setState("isHurt", False)
            this.setState("inMidAction", True)
            this.setState("isDead", True)
            this.setState("blink", False)
            this.setTimer("deadEnd", this.deadEnd)
            this.resetAnimationSequence(this.deathAnim)
            this.animateActionSingle(this.deathAnim, this.imgDeath)

        if action == "midDeath":
            #ensure the character does not get thrusted across the map
            if this.speedX > 0:
                if this.speedX <= 0.5:
                    this.speedX = 0
                else:
                    this.speedX -= 0.5
            if this.speedX < 0:
                if this.speedX >= -0.5:
                    this.speedX = 0
                else:
                    this.speedX += 0.5
                
            this.animateActionSingle(this.deathAnim, this.imgDeath)
            #add in a timer to take the character back to the main menu
            if this.checkTimer("deadEnd"):
                #if there is not a game over...
                if not this.game.getGameOver():
                    #play the death sound
                    pygame.mixer.Sound.play(this.wavDeath)
                if this == this.game.getPlayer():
                    #make the game to be over
                    this.game.setGameOver(True)
                if not this == this.game.getPlayer():
                    this.remove()

#------------------------------------------------------------------------------#
#                          Actions, Timers, & Effects                          #
#------------------------------------------------------------------------------#       
        #add a second to the amount of time passing on each timer
        this.countdownTimers()
        
        #animate blinking if the character is supposed to be blinking
        this.animateBlinking()

        """
        if this.getName() == "Player":
            print(this.getName(), " :: ", this.timers)
        """
        
        
#------------------------------------------------------------------------------#
#                              End  Of  Actions                                #
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
#                            Physics and Collision                             #
#------------------------------------------------------------------------------#

    #move an object a certain number of x and y coordinates specified by the tuple argument
    def move(this, moveX, moveY):     
        canMove = True
        xOffset = 0
        yOffset = 0

        #ensure the player is moving to the nearest 0.5
        moveX = this.game.truncateFloat(moveX)
        moveY = this.game.truncateFloat(moveY)

        #if we are going fast enough to warp through blocks...
        #reduce the speed to one pixel before warping through a block
        if abs(moveX) >= this.game.getBlockScale():
            if moveX < 0:
                moveX = -this.game.getBlockScale() + 1
            elif moveX > 0:
                moveX = this.game.getBlockScale() - 1                
        if abs(moveY) >= this.game.getBlockScale():
            if moveY < 0:
                moveY = -this.game.getBlockScale() + 1
            elif moveY > 0:
                moveY = this.game.getBlockScale() - 1                
            
        #check to see if there is collision in all of these object lists and the player
        xOffset, yOffset, canMove = this.checkCollisionOffsets(moveX, moveY, xOffset, yOffset, canMove, this.game.getTerrainSprites())
        xOffset, yOffset, canMove = this.checkCollisionOffsets(moveX, moveY, xOffset, yOffset, canMove, this.game.getItemSprites())
        xOffset, yOffset, canMove = this.checkCollisionOffsets(moveX, moveY, xOffset, yOffset, canMove, this.game.getNPCSprites())
        xOffset, yOffset, canMove = this.checkCollisionOffsets(moveX, moveY, xOffset, yOffset, canMove, this.game.getPlayer())
        
        if canMove:
            #move the object by the amount specified
            this.getRect().move_ip(moveX, moveY)
            #return the fact that the player was able to move without collision
            return True
        else:
            this.getRect().move_ip(xOffset, yOffset)
            return False

    
    #a method used when checking the amount of space before a collision
    def checkCollisionOffsets(this, moveX, moveY, xOffset, yOffset, canMove, sObject):        
        leadRect = this.getRect().copy()
        leadRect.move_ip(moveX, moveY)

        #if the object instance is a single sprite
        if isinstance(sObject, pygame.sprite.Sprite):
            #ensure that the collision object is not itself
            #and the object is not able to be passed through
            #and  the object is colliding with the leading rectangle
            if not sObject == this and sObject.density > 0\
               and not sObject == this.game.getPlayer()\
               and leadRect.colliderect(sObject.getRect()):
                
                #if moving left
                if moveX < 0:
                    #if we collide with the right side of an item while moving left
                    if this.getRect().left + moveX <= sObject.getRect().right:   
                        #set the movement flag to false
                        canMove = False
                        #check to see if there is a collision that is closer than the current offset
                        if xOffset > (sObject.getRect().right - this.getRect().left):
                            xOffset = (sObject.getRect().right - this.getRect().left)
                            
                #if moving right
                elif moveX > 0:
                    #if we collide with the left side of an item while moving right
                    if this.getRect().right + moveX >= sObject.getRect().left:
                        #set movement flag to false
                        canMove = False
                        #check to see if there is a collision that is closer than the current offset
                        if xOffset < (sObject.getRect().left - this.getRect().right):
                            xOffset = (sObject.getRect().left - this.getRect().right)

                #if we are moving up
                if moveY < 0:
                    #if we collide with the bottom side of an item while moving up
                    if this.getRect().top + moveY <= sObject.getRect().bottom:
                        #set movement flag to false
                        canMove = False
                        #check to see if there is a collision that is closer than the current offset
                        if yOffset > (sObject.getRect().bottom - this.getRect().top):
                            yOffset = (sObject.getRect().bottom - this.getRect().top)

                #if we are moving down
                elif moveY > 0:
                    #if we collide with the top side of an item while moving down
                    if this.getRect().bottom + moveY >= sObject.getRect().top:
                        #set the movement flag to false
                        canMove = False
                        #the character is considered on the ground if he/she is colliding with the ground
                        #this.onGround = True
                        #check to see if there is a collision that is closer than the current offset
                        if yOffset < (sObject.getRect().top - this.getRect().bottom):
                            yOffset = (sObject.getRect().top - this.getRect().bottom)

        #if the object instance is a sprite group
        elif isinstance(sObject, pygame.sprite.Group):
            #loop through each collision object
            for co in sObject:
                #ensure that the collision object is not itself
                #and the object is not able to be passed through
                #and  the object is colliding with the leading rectangle
                if not co == this and co.density > 0\
                   and leadRect.colliderect(co.getRect()):
                    
                    #if moving left
                    if moveX < 0:
                        #if we collide with the right side of an item while moving left
                        if this.getRect().left + moveX <= co.getRect().right:   
                            #set the movement flag to false
                            canMove = False
                            #check to see if there is a collision that is closer than the current offset
                            if xOffset > (co.getRect().right - this.getRect().left):
                                xOffset = (co.getRect().right - this.getRect().left)
                                
                    #if moving right
                    elif moveX > 0:
                        #if we collide with the left side of an item while moving right
                        if this.getRect().right + moveX >= co.getRect().left:
                            #set movement flag to false
                            canMove = False
                            #check to see if there is a collision that is closer than the current offset
                            if xOffset < (co.getRect().left - this.getRect().right):
                                xOffset = (co.getRect().left - this.getRect().right)

                    #if we are moving up
                    if moveY < 0:
                        #if we collide with the bottom side of an item while moving up
                        if this.getRect().top + moveY <= co.getRect().bottom:
                            #set movement flag to false
                            canMove = False
                            #check to see if there is a collision that is closer than the current offset
                            if yOffset > (co.getRect().bottom - this.getRect().top):
                                yOffset = (co.getRect().bottom - this.getRect().top)

                    #if we are moving down
                    elif moveY > 0:
                        #if we collide with the top side of an item while moving down
                        if this.getRect().bottom + moveY >= co.getRect().top:
                            #set the movement flag to false
                            canMove = False
                            #the character is considered on the ground if he/she is colliding with the ground
                            #this.onGround = True
                            #check to see if there is a collision that is closer than the current offset
                            if yOffset < (co.getRect().top - this.getRect().bottom):
                                yOffset = (co.getRect().top - this.getRect().bottom)
                                
        return xOffset, yOffset, canMove

    def addForce(this, forceX, forceY):
        if forceX > 0:
            this.speedX += forceX
        elif forceX < 0:
            this.speedX += forceX
        if forceY > 0:
            this.speedY += forceY
        elif forceY < 0:
            this.speedY += forceY

            
#------------------------------------------------------------------------------#
#                             Image and Animation                              #
#------------------------------------------------------------------------------#

    #A method so that the player can be drawn without being in a sprite group
    def draw(this, screen):
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

    def adjustImage(this):
        this.setImage(pygame.transform.scale(this.getImage(), \
              (this.game.getBlockScale() * 2, this.game.getBlockScale() * 2)))
        this.getImage().scroll(-17, 0)
      
    def animateActionCont(this, stateList, imgList):
        for idx in range (0, len(stateList)):
            if stateList[idx]:
                this.setImage(imgList[idx])
                this.tempImage = imgList[idx]
                this.adjustImage()
                if this.checkTimer("contAnim"):
                    stateList[idx] = False
                    this.setTimer("contAnim", this.contAnimTimeTrig)
                    if idx < (len(stateList) - 1):
                        stateList[idx + 1] = True
                    else:
                        stateList[0] = True

    def animateActionSingle(this, stateList, imgList):
        for idx in range (0, len(stateList)):
            if stateList[idx]:
                this.setImage(imgList[idx])
                this.tempImage = imgList[idx]
                this.adjustImage()
                if this.checkTimer("singleAnim"):
                    stateList[idx] = False
                    this.setTimer("singleAnim", this.singleAnimTimeTrig)
                    if idx < (len(stateList) - 1):
                        stateList[idx + 1] = True

    def resetAnimationSequence(this, stateList):
        for idx in range (0, len(stateList)):
            if idx == 0:
                stateList[idx] = True
            elif not idx == 0:
                stateList[idx] = False

    def animateBlinking(this):
        if this == this.game.getPlayer():
            #if the character is supposed to be blinking
            if this.getState("blink"):
                #if the character is supposed to be blank
                if this.getState("blinkOn")\
                   and this.checkTimer("blinkEnd"):
                    #store the current image
                    this.tempImage = this.getImage()
                    #set the image to be blank
                    this.setImage(this.imgBlank)
                    #set the blink timer
                    this.setTimer("blinkEnd", this.blinkEnd)
                    #show an image the next time this is animated
                    this.setState("blinkOn", False)
                #if the character is not supposed to be blank
                elif not this.getState("blinkOn")\
                     and this.checkTimer("blinkEnd"):
                    #set the current image to the stored image
                    this.setImage(this.tempImage)
                    #clear the stored image
                    this.tempImage = this.imgBlank
                    #set the blink timer
                    this.setTimer("blinkEnd", this.blinkEnd)
                    #do not show an image the next time this is animated
                    this.setState("blinkOn", True)
        

                        
#------------------------------------------------------------------------------#
#                          Character State Methods                             #
#------------------------------------------------------------------------------#

    #adds a character state if it does not exist. Then, sets the state to the
    #input boolean
    def setState(this, stateName, boolean):
        this.state[stateName] = boolean

    #checks the character state
    def getState(this, stateName):
        #check to see if the state exists in the dictionary
        if not this.state.get(stateName) == None:    
            #check to see if enough timer has passed on the timer to trigger an event
            return this.state[stateName]

        elif this.state.get(stateName) == None:
            print(this.getName(), " :: State -", stateName, "- has not been created yet")
            return False


#------------------------------------------------------------------------------#
#                            Timers and Cooldown                               #
#------------------------------------------------------------------------------#

    #adds a timer if it does not exist and then sets the timer to the trigger time
    def setTimer(this, timerName, timeTrigger):
        this.timers[timerName] = timeTrigger

    #check to see if a timer has expired
    def checkTimer(this, timerName):
        #check to see if the timer exists in the dictionary
        if not this.timers.get(timerName) == None:    
            #check to see if enough timer has passed on the timer to trigger an event
            if this.timers[timerName] <= 0:
                return True
            else:
                return False
        elif this.timers.get(timerName) == None:
            print(this.getName(), " :: ", timerName, " has not been created yet")
            return False

    def countdownTimers(this):
        #loop through the dictonary to subtract one second from each timer
        for idx in this.timers:
            if this.timers[idx] > 0:
                this.timers[idx] -= 1

#------------------------------------------------------------------------------#
#                           Game  Related  Methods                             #
#------------------------------------------------------------------------------#

    #take damage as the character and update the HUD if it is the player
    def takeDamage(this):
        #take a point of damage
        this.health -= 1
        #mark that the character has been hurt already
        this.setState("alreadyHurt", True)
        #if this is the player
        if this == this.game.getPlayer():
            #if there is not a game over...
            if not this.game.getGameOver():
                #play the hurt sound
                pygame.mixer.Sound.play(this.wavHurt)
            #sync the HUD to represent the number of hearts on screen
            this.game.getPlayer().getHud().syncHearts()

    #attack with the character
    def attack(this):
        #create a references to reduce code bloat
        block = this.game.getBlockScale()
        player = this.game.getPlayer()
        #create a duplicate of the character's rect
        damageRect = this.getRect().copy()
        #reduce it to a size of a block
        damageRect.inflate_ip(0, -block)
        
        if this.isFacing == "right":
            #move the damage rect almost a block length to the right
            damageRect.move_ip((block - block//4), 0)

        elif this.isFacing == "left":
            #move the damage rect almost a block length to the left
            damageRect.move_ip(-(block - block//4), 0)
            
        #if the player is attacking
        if this == this.game.getPlayer():
            #Loop though NPC sprite group
            for enemy in this.game.getNPCSprites():
                #if the damage rect is colliding with an NPC and
                #the NPC is not already taking damage or dead
                #and the player has not already hit an NPC yet
                if damageRect.colliderect(enemy.getRect())\
                   and not enemy.getState("isHurt")\
                   and not enemy.getState("isDead")\
                   and not this.getState("alreadyHit"):
                    #change the state of the NPC to being hurt
                    enemy.setState("isHurt", True)
                    #add some impact on the hit
                    if this.isFacing == "left":    
                        enemy.addForce(-this.attackForce, 0)
                    elif this.isFacing == "right":    
                        enemy.addForce(this.attackForce, 0)
                    #ensure a player can only attaok one NPC in one attack
                    this.setState("alreadyHit", True)

        #if an NPC is attacking
        elif isinstance(this, Character)\
             and not this == this.game.getPlayer():
            #if the damage rect is colliding with the Player and
            #the player is not already taking damage or dead
            #and the NPC has not already hit the player
            if damageRect.colliderect(player.getRect())\
               and not player.getState("isHurt")\
               and not player.getState("isDead")\
               and not this.getState("alreadyHit"):
                #change the state of the player to being hurt
                player.setState("isHurt", True)
                #add some impact on the hit
                if this.isFacing == "left":    
                    player.addForce(-this.attackForce, 0)
                elif this.isFacing == "right":    
                    player.addForce(this.attackForce, 0)
                #ensure a single NPC does not hit the player twice in one attack
                this.setState("alreadyHit", True)

                    
    #a method that removes the character from the game after they are dead
    def remove(this):
        this.kill()


#------------------------------------------------------------------------------#
#                           End Of Character Class                             #
#------------------------------------------------------------------------------#
