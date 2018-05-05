
### Week 2: I FINALLY fixed the issue with PyCharm not loading images, and now I can load my own images. Also, now can move my player around the screen.

### Week 3: The movement of my character is now fully functioning.

### Week 14/15 Submission: So I apologize for not submitting this before... But over the last few weeks, I have gotten the player to be able to shoot arrows. I created
### multiple classes to house most of the functions for my enemies, the player, the crossbow attributes, and even the background. Specifically over the last week, I have
### worked on the enemy class to create methods that draw the enemies and orient them to the player's position, as well as another method that moves the enemies in the
### EXACT direction of the player. Also, I have created a spawn system that creates enemies out of the enemy class, and spawns them at random points on the boundaries of the
### game map. Most recently, I have written code that defines all of the collisions between the player and the enemies, as well as between the arrows the player shoots and
### the enemies. Aftera all of this, the core of my game is finished.
### From here on out to presentation day, I want to try and create a round system, where after x amount of enemies are killed, the game will pause, "round 2" will pop up,
### and the game will continue to run again after a few seconds. I also want to create different types of enemies, and be able to have the game randomly spawn different enemies
### each with different attributes.

SOURCES = (
           'https://www.raywenderlich.com/24252/beginning-game-programming-for-teens-with-python'
           'https://www.pinterest.com/pin/288652657348582160/'
           'https://www.webucator.com/blog/2015/03/python-color-constants-module/'
           'https://stackoverflow.com/questions/20044791/how-to-make-an-enemy-follow-the-player-in-pygame'
           'https://gamedev.stackexchange.com/questions/106457/move-an-enemy-towards-the-player-in-pygame'
           'https://docs.python.org/3/library/math.html#hyperbolic-functions'
           'My Dad'
           )

import pygame
import math
from pygame.locals import *
from random import *

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
displayWidth = 1200
displayHeigth = 800
screen = pygame.display.set_mode((displayWidth, displayHeigth))
pygame.display.set_caption('Crossbow Battle')

ScriptPath_OneDrive = "C:/Users/Chris.Carmona18/OneDrive - Bellarmine College Preparatory/Intro to CS/Chris/"
ScriptPath_Local = "C:/Users/Chris.Carmona18/Desktop/Coding Stuff/Chris/"

player = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelGunman_84x61.png")
arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/arrow_31x7.png")
background = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png")
enemy_one = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelEnemy_1_48x56.png")
# enemy_two = pygame.image.load("resources/images/")
# enemy_three = pygame.image.load("resources/images/")

darkgoldenrod = [184, 134, 11]
arrows = []
Dead = "Lmao ur trash"

playerInitialpos = [displayWidth * 0.5, displayHeigth * 0.5]
move = [False, False, False, False]

class Background():
    def __init__(self, image, BG_Color):
        self.image = image
        self.BG_Color = BG_Color
    def SetPicBG(self):
        for a in range(displayWidth // background.get_width() + 1):
            for b in range(displayHeigth // background.get_heigth() + 1):
                screen.blit(background, (0, 0))
                # screen.blit(background, (x, y), pygame.rect(x, y, 62, 62))
    def SetColBG(self):
        screen.fill(self.BG_Color)
GameSurface = Background(background, darkgoldenrod)

class CrossbowAttributes():
    def __init__(self, arrowSpeed, damage):
        self.arrowSpeed = arrowSpeed
        self.damage = damage
Basic_Crossbow = CrossbowAttributes(2, 10)

class Character():
    def __init__(self, image, playerSpeed, playerHealth):
        self.image = image
        self.playerSpeed = playerSpeed
        self.playerHealth = playerHealth
    def PlayerSetup(self):
        radconvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        global playerAngle
        playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
        global playerRotation
        playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
        global playerPos
        playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2, playerInitialpos[1] - playerRotation.get_rect().height / 2)
        screen.blit(playerRotation, playerPos)
    def Get_playerPos(self):
        return playerPos
    def Get_PlayerHealth(self):
        return self.playerHealth
Player1 = Character(player, 0.75, 200)
playerHealth = Player1.Get_PlayerHealth()

def GetSpawnCoordinates():
    SpawnLocation = randint(1, 4)
    if SpawnLocation == 1:
        EnemySpawn = [randint(0, displayWidth), 0]
        return EnemySpawn
    if SpawnLocation == 2:
        EnemySpawn = [randint(0, displayWidth), 800]
        return EnemySpawn
    if SpawnLocation == 3:
        EnemySpawn = [0, randint(0, displayHeigth)]
        return EnemySpawn
    if SpawnLocation == 4:
        EnemySpawn = [1200, randint(0, displayHeigth)]
        return EnemySpawn

EnemySpawnLocations = [GetSpawnCoordinates(), GetSpawnCoordinates(), GetSpawnCoordinates(), GetSpawnCoordinates(), GetSpawnCoordinates()]

class Enemy():
    def __init__(self, image, enemySpeed, enemyDamage, xcor, ycor):
        self.image = image
        self.enemySpeed = enemySpeed
        self.enemyDamage = enemyDamage
        self.xcor = xcor
        self.ycor = ycor
        self.enemyPos = (0, 0)
    def Enemy_Control(self):
        radconvert = (360 / (2 * math.pi))
        enemyAngle = math.atan2(playerPos[1] - self.ycor, playerPos[0] - self.xcor)
        global enemyRotation
        enemyRotation = pygame.transform.rotate(enemy_one, 360 - enemyAngle * radconvert)
        self.enemyPos = [self.xcor - (enemyRotation.get_rect().width / 2 - 30), self.ycor - (enemyRotation.get_rect().height / 2 - 30)]
        screen.blit(enemyRotation, self.enemyPos)
    def Enemy_Move(self):
        enemyAngle = math.atan2(playerPos[1] - self.ycor, playerPos[0] - self.xcor)
        xmove = math.cos(enemyAngle) * self.enemySpeed
        ymove = math.sin(enemyAngle) * self.enemySpeed
        self.xcor += xmove
        self.ycor += ymove
    def Get_enemyPos(self):
        return self.enemyPos
    def Get_enemyDamage(self):
        return self.enemyDamage

enemyList = []
EnemyCount = 0

SpawnCount = 2000
Countdown = 10

Run_Game = True
while Run_Game:
    screen.fill(0)
    GameSurface.SetColBG()

    Player1.PlayerSetup()

    for bullet in arrows:
        index = 0
        arrowVelx = math.cos(bullet[0]) * Basic_Crossbow.arrowSpeed
        arrowVely = math.sin(bullet[0]) * Basic_Crossbow.arrowSpeed
        bullet[1] += arrowVelx
        bullet[2] += arrowVely
        if bullet[1] < -64 or bullet[1] > displayWidth or bullet[2] < -64 or bullet[2] > displayHeigth:
            arrows.pop(index)
        for projectile in arrows:
            radconvert = (360 / (2 * math.pi))
            global arrowGameImage
            arrowGameImage = pygame.transform.rotate(arrow, 360-projectile[0]*radconvert)
            screen.blit(arrowGameImage, (projectile[1], projectile[2]))

    if SpawnCount == 0:
        SpawnLocation = GetSpawnCoordinates()
        enemyList.append(Enemy(enemy_one, 0.4, 1, SpawnLocation[0], SpawnLocation[1]))
        EnemyCount += 1
        SpawnCount = 2000
    elif SpawnCount != 0:
        SpawnCount = SpawnCount - Countdown
    if EnemyCount == 30:
        SpawnCount = 2000
        Countdown = 0
    enemyIndex = 0
    for enemy in enemyList:
        enemy.Enemy_Control()
        pos = enemy.Get_enemyPos()
        if pos != playerPos:
            enemy.Enemy_Move()
        if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= Player1.Get_playerPos()[0] + 50 and \
                enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= Player1.Get_playerPos()[1] + 50:
            playerHealth = playerHealth - enemy.Get_enemyDamage()
            if playerHealth <= 0:
                print(Dead)
                Start_Game = False
        arrowIndex = 0
        for projectile in arrows:
            if projectile[1] >= enemy.Get_enemyPos()[0] and projectile[1] <= enemy.Get_enemyPos()[0] + 45 and \
                    projectile[2] >= enemy.Get_enemyPos()[1] and projectile[2] <= enemy.Get_enemyPos()[1] + 45:
                enemyList.pop(enemyIndex)
                arrows.pop(arrowIndex)
            arrowIndex += 1
        enemyIndex += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run_Game = False
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
        if event.type == MOUSEBUTTONDOWN:
            radconvert = (360 / (2 * math.pi))
            mousePos = pygame.mouse.get_pos()
            playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
            playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
            playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2,playerInitialpos[1] - playerRotation.get_rect().height / 2)
            arrows.append([math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])), playerPos[0] + 30, playerPos[1] + 30])

    if move[0]:
        playerInitialpos[1] += -Player1.playerSpeed
    elif move[1]:
        playerInitialpos[1] += Player1.playerSpeed
    if move[2]:
        playerInitialpos[0] += -Player1.playerSpeed
    elif move[3]:
        playerInitialpos[0] += Player1.playerSpeed

    if playerInitialpos[0] <= 0:
        move[2] = False
    if playerInitialpos[1] <= 0:
        move[0] = False
    if playerInitialpos[0] >= displayWidth:
        move[3] = False
    if playerInitialpos[1] >= displayHeigth:
        move[1] = False

    pygame.display.update()