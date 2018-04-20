### Week 2: I FINALLY fixed the issue with PyCharm not loading images, and now I can load my own images. Also, now can move my player around the screen.
### Week 3: The movement of my character is now fully functioning.

import pygame
import math
from pygame.locals import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
displayWidth = 1200
displayHeigth = 800
screen = pygame.display.set_mode((displayWidth, displayHeigth))
pygame.display.set_caption('Crossbow Battle')

ScriptPath = "C:/Users/Chris.Carmona18/OneDrive - Bellarmine College Preparatory/Intro to CS/Chris/"
player = pygame.image.load(ScriptPath + "resources/CrossbowGameImages/PixelGunman.png")
arrow = pygame.image.load(ScriptPath + "resources/CrossbowGameImages/bullet.png")
background = pygame.image.load(ScriptPath + "resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png")
# enemy_one = pygame.image.load("resources/images/")
# enemy_two = pygame.image.load("resources/images/")
# enemy_three = pygame.image.load("resources/images/")

playerInitialpos = [displayWidth * 0.5, displayHeigth * 0.5]
move = [False, False, False, False]

def Background():
    for a in range(displayWidth // background.get_width() + 1):
        for b in range(displayHeigth // background.get_width() + 1):
            screen.blit(background, (0, 0))
# screen.blit(background, (x, y), pygame.Rect(x, y, 62, 62))

def PlayerSetup():
    radconvert = (360 / (2 * 3.14159265358979323))
    mousePos = pygame.mouse.get_pos()
    playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
    playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
    playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2, playerInitialpos[1] - playerRotation.get_rect().height / 2)
    screen.blit(playerRotation, playerPos)

arrows = []

Start_Game = True
while Start_Game:
    screen.fill(0)
    PlayerSetup()
    for bullet in arrows():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Start_Game = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                move[0] = True
            elif event.key == K_a:
                move[2] = True
            elif event.key == K_s:
                move[1] = True
            elif event.key == K_d:
                move[3] = True
        if event.type == pygame.KEYUP:
            if event.key == K_w:
                move[0] = False
            elif event.key == K_a:
                move[2] = False
            elif event.key == K_s:
                move[1] = False
            elif event.key == K_d:
                move[3] = False
    if move[0]:
        playerInitialpos[1] += -0.8
    elif move[1]:
        playerInitialpos[1] += 0.8
    if move[2]:
        playerInitialpos[0] += -0.8
    elif move[3]:
        playerInitialpos[0] += 0.8

    pygame.display.update()







### IGNORE THE FOLLOWING CODE.... IM JUST LEAVING IT HERE:
#
# from turtle import *
# class CharacterCreator():
#     def __init__(self, turtleClass, weaponClass, playerName, playerImage, hitpoints, speed, turnSpeed, forward, backward, left, right):
#         self.turtleClass = Turtle()
#         self.playerName = playerName
#         self.playerImage = playerImage
#         self.hitpoints = hitpoints
#         self.speed = speed
#         self.forward = forward
#         self.backward = backward
#         self.left = left
#         self.right = right
#         self.turnSpeed = turnSpeed
#         self.screen = self.turtleClass.getscreen()
#         self.weaponTurtle = Turtle()
#         self.weaponXcor = self.weaponTurtle.xcor()
#         self.weaponYcor = self.weaponTurtle.ycor()
#
#     def PlayerSetup(self):
#         # self.turtleClass.screensize(100, 400, "black")
#         self.turtleClass.penup()
#         # self.turtleClass.color(self.playerColor)
#     def check(self):
#         if self.turtleClass.xcor() > 300 or self.turtleClass.xcor() < -300 or self.turtleClass.ycor() > 300 or self.turtleClass.ycor() < -300:
#             print("Out of bounds!")
#             self.hitpoints -= 5
#             if self.hitpoints <= 0:
#                 print("You died!")
#                 sleep(3)
#                 self.screen.bye()
#     def Controls(self):
#         def forward():
#             self.turtleClass.fd(self.speed)
#             print(self.turtleClass.pos())
#             self.check()
#         def backward():
#             self.turtleClass.bk(self.speed)
#             print(self.turtleClass.pos())
#             self.check()
#         def turnLeft():
#             self.turtleClass.left(self.turnSpeed)
#             self.turtleClass.fd(self.speed)
#             print(self.turtleClass.pos())
#             self.check()
#         def turnRight():
#             self.turtleClass.right(self.turnSpeed)
#             self.turtleClass.fd(self.speed)
#             print(self.turtleClass.pos())
#             self.check()
#         def ShootCrossbow():
#             self.weaponTurtle.speed(0)
#             x = self.turtleClass.xcor()
#             y = self.turtleClass.ycor()
#             self.weaponTurtle.setpos(x, y)
#         self.screen.onkeypress(forward, self.forward)
#         self.screen.onkeypress(backward, self.backward)
#         self.screen.onkeypress(turnLeft, self.left)
#         self.screen.onkeypress(turnRight, self.right)
#         self.screen.listen()
#
#
# Chris = CharacterCreator(Turtle(), Turtle(), Chris, '', 100, 10, 5, "w", "s", "a", "d", "f")
#
# Chris()