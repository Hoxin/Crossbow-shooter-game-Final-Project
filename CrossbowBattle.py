
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
           'https://armorgames.com/play/3642/medieval-rampage'
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

background = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Dirt_Background_1200x800_HighRes.png")
healthbar = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/healthbar.png")
health = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Healthbar.png")

player = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelGunman_84x59.png")

Basic_Arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Basic_Arrow_32x7.png")
Steel_Arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Steel_Arrow_32x7.png")
HollowPoint_Arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/HollowPoint_Arrow_32x7.png")
Tri_Arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Tri_Arrow_32x7.png")
Frost_Arrow = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Frost_Arrow_32x7.png")

fireball = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/Fireball_60x23.png")
enemy_one = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelEnemy_1_48x56.png")
enemy_two = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelEnemy_2_62x62.png")
enemy_three = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelEnemy_3_140x54.png")
enemy_four = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/PixelEnemy_4_58x72.png")

# enemy_Boss_one = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/")
# enemy_Boss_two = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/")
# enemy_Boss_three = pygame.image.load(ScriptPath_Local + "resources/CrossbowGameImages/")


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


class Arrows():
    def __init__(self, arrowImage, arrowSpeed, arrowDamage):
        self.arrowImage = arrowImage
        self.arrowSpeed = arrowSpeed
        self.arrowDamage = arrowDamage
    def Get_arrowSpeed(self):
        return self.arrowSpeed
    def Get_arrowDamage(self):
        return self.arrowDamage
    def Set_ArrowAttributes(self, image, speed, damage):
        self.arrowImage = image
        self.arrowSpeed = speed
        self.damage = damage

    def Basic_Coordinates(self):
        radconvert = (360 / (2 * math.pi))
        mousePos = pygame.mouse.get_pos()
        playerAngle = math.atan2(mousePos[1] - playerInitialpos[1], mousePos[0] - playerInitialpos[0])
        playerRotation = pygame.transform.rotate(player, 360 - playerAngle * radconvert)
        playerPos = (playerInitialpos[0] - playerRotation.get_rect().width / 2,
                     playerInitialpos[1] - playerRotation.get_rect().height / 2)
        arrows.append([math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       math.atan2(mousePos[1] - (playerInitialpos[1]), mousePos[0] - (playerInitialpos[0])),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2),
                       playerPos[0] + (player.get_rect().width / 2), playerPos[1] + (player.get_rect().height / 2)])
    def Basic_Control(self):
        index = 0
        arrowVelx = math.cos(bullet[0]) * self.arrowSpeed
        arrowVely = math.sin(bullet[0]) * self.arrowSpeed
        bullet[3] += arrowVelx
        bullet[4] += arrowVely
        if bullet[3] < -64 or bullet[3] > displayWidth or bullet[4] < -64 or bullet[4] > displayHeigth:
            arrows.pop(index)
        for projectile in arrows:
            radconvert = (360 / (2 * math.pi))
            global arrowGameImage
            arrowGameImage = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            screen.blit(arrowGameImage, (projectile[3], projectile[4]))
    def Basic_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def HollowPoint_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    # arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def Tri_Control(self):
        index1 = 0
        index2 = 1
        index3 = 2
        arrow1Velx = math.cos(bullet[0]) * self.arrowSpeed
        arrow1Vely = math.sin(bullet[0]) * self.arrowSpeed
        arrow2Velx = math.cos(bullet[3]) * self.arrowSpeed
        arrow2Vely = math.sin(bullet[3]) * self.arrowSpeed
        arrow3Velx = math.cos(bullet[4]) * self.arrowSpeed
        arrow3Vely = math.sin(bullet[4]) * self.arrowSpeed
        bullet[3] += arrow1Velx
        bullet[4] += arrow1Vely
        bullet[5] += arrow2Velx
        bullet[6] += arrow2Vely
        bullet[7] += arrow3Velx
        bullet[8] += arrow3Vely
        if bullet[3] < -64 or bullet[3] > displayWidth or bullet[4] < -64 or bullet[4] > displayHeigth and \
                bullet[5] < -64 or bullet[5] > displayWidth or bullet[6] < -64 or bullet[6] > displayHeigth and \
                bullet[7] < -64 or bullet[7] > displayWidth or bullet[8] < -64 or bullet[8] > displayHeigth:
            arrows.pop(index1)
            arrows.pop(index2)
            arrows.pop(index3)
        for projectile in arrows:
            radconvert = (360 / (2 * math.pi))
            global arrowGameImage
            arrowGameImage1 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            arrowGameImage2 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            arrowGameImage3 = pygame.transform.rotate(self.arrowImage, 360 - projectile[0] * radconvert)
            screen.blit(arrowGameImage1, (projectile[3], projectile[4]))
            screen.blit(arrowGameImage2, (projectile[5], projectile[6]))
            screen.blit(arrowGameImage3, (projectile[7], projectile[8]))
    def Tri_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

    def Frost_Hit(self):
        enemyIndex = 0
        for enemy in enemyList:
            enemy.Enemy_Control()
            pos = enemy.Get_enemyPos()
            if pos != playerPos:
                enemy.Enemy_Move()
            if enemy.Get_enemyPos()[0] >= Player1.Get_playerPos()[0] and enemy.Get_enemyPos()[0] <= \
                    Player1.Get_playerPos()[0] + player.get_rect().width and \
                    enemy.Get_enemyPos()[1] >= Player1.Get_playerPos()[1] and enemy.Get_enemyPos()[1] <= \
                    Player1.Get_playerPos()[1] + player.get_rect().height:
                global playerHealth
                playerHealth = playerHealth - enemy.Get_enemyDamage()
                if playerHealth <= 0:
                    print(Dead)
                    global Run_Game
                    Run_Game = False
            arrowIndex = 0
            for projectile in arrows:
                if projectile[3] >= enemy.Get_enemyPos()[0] and projectile[3] <= enemy.Get_enemyPos()[0] + \
                        enemy.Get_enemyDimensions()[0] and \
                        projectile[4] >= enemy.Get_enemyPos()[1] and projectile[4] <= enemy.Get_enemyPos()[1] + \
                        enemy.Get_enemyDimensions()[1]:
                    enemyHealth = enemy.Get_enemyHealth() - self.arrowDamage
                    arrows.pop(arrowIndex)
                    if enemyHealth <= 0:
                        enemyList.pop(enemyIndex)
                    elif enemyHealth > 0:
                        enemy.Set_enemyHealth(enemyHealth)
                arrowIndex += 1
            enemyIndex += 1

Arrow_Type = Arrows(Basic_Arrow, 2.0, 4)
Selected_Arrow = Basic_Arrow
def Arrow_Attribute_Selecter():
    if Selected_Arrow == Basic_Arrow:
        Arrow_Type.Set_ArrowAttributes(Basic_Arrow, 2.0, 4)
    if Selected_Arrow == Steel_Arrow:
        Arrow_Type.Set_ArrowAttributes(Steel_Arrow, 2.0, 7)
    if Selected_Arrow == HollowPoint_Arrow:
        Arrow_Type.Set_ArrowAttributes(HollowPoint_Arrow, 2.0, 2)
    if Selected_Arrow == Tri_Arrow:
        Arrow_Type.Set_ArrowAttributes(Tri_Arrow, 2.0, 3)
    if Selected_Arrow == Frost_Arrow:
        Arrow_Type.Set_ArrowAttributes(Frost_Arrow, 2.0, 4)

def Arrow_Coordinate_Selecter():
    if Selected_Arrow == Basic_Arrow or Steel_Arrow or HollowPoint_Arrow or Tri_Arrow or Frost_Arrow:
        Arrow_Type.Basic_Coordinates()
def Arrow_Control_Selecter():
    if Selected_Arrow == Basic_Arrow or Steel_Arrow or HollowPoint_Arrow or Frost_Arrow:
        Arrow_Type.Basic_Control()
    if Selected_Arrow == Tri_Arrow:
        Arrow_Type.Tri_Control()
def Arrow_Hit_Selecter():
    if Selected_Arrow == Basic_Arrow or Steel_Arrow:
        Arrow_Type.Basic_Hit()
    if Selected_Arrow == HollowPoint_Arrow:
        Arrow_Type.HollowPoint_Hit()
    if Selected_Arrow == Tri_Arrow:
        Arrow_Type.Tri_Hit()
    if Selected_Arrow == Frost_Arrow:
        Arrow_Type.Frost_Hit()


class Character():
    def __init__(self, image, playerSpeed, playerHealth, WeaponType):
        self.image = image
        self.playerSpeed = playerSpeed
        self.playerHealth = playerHealth
        self.WeaponType = WeaponType
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
Player1 = Character(player, 1.00, 200, "")
playerHealth = Player1.Get_PlayerHealth()


class Enemy():
    def __init__(self, image, enemySpeed, enemyDamage, enemyHealth, xcor, ycor, xdimension, ydimension):
        self.image = image
        self.enemySpeed = enemySpeed
        self.enemyDamage = enemyDamage
        self.enemyHealth = enemyHealth
        self.xcor = xcor
        self.ycor = ycor
        self.xdimension = xdimension
        self.ydimension = ydimension
        self.enemyPos = (0, 0)
    def Enemy_Control(self):
        radconvert = (360 / (2 * math.pi))
        enemyAngle = math.atan2(playerPos[1] - self.ycor, playerPos[0] - self.xcor)
        global enemyRotation
        enemyRotation = pygame.transform.rotate(self.image, 360 - enemyAngle * radconvert)
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
    def Get_enemyHealth(self):
        return self.enemyHealth
    def Get_enemyDimensions(self):
        x = self.xdimension
        y = self.ydimension
        enemyDimensions = (x, y)
        return enemyDimensions
    def Set_enemyHealth(self, health):
        self.enemyHealth = health

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

def Get_Enemy():
    EnemySelect = randint(1, 4)
    if EnemySelect == 1:
        SelectedEnemy = Enemy(enemy_one, 0.60, 0.3, 13, SpawnLocation[0], SpawnLocation[1], enemy_one.get_rect().width, enemy_one.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 2:
        SelectedEnemy = Enemy(enemy_two, 0.45, 0.5, 21, SpawnLocation[0], SpawnLocation[1], enemy_two.get_rect().width, enemy_two.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 3:
        SelectedEnemy = Enemy(enemy_three, 0.90, 0.2, 8, SpawnLocation[0], SpawnLocation[1], enemy_three.get_rect().width - 65, enemy_three.get_rect().height)
        return SelectedEnemy
    if EnemySelect == 4:
        SelectedEnemy = Enemy(enemy_four, 0.35, 1, 32, SpawnLocation[0], SpawnLocation[1], enemy_four.get_rect().width, enemy_four.get_rect().height)
        return SelectedEnemy

enemyList = []
EnemyCount = 0
SpawnCount = 15000
Countdown = 25
MaximumEnemies = 45

Run_Game = True
while Run_Game:
    screen.fill(0)
    GameSurface.SetColBG()

    Player1.PlayerSetup()

    for bullet in arrows:
        Arrow_Control_Selecter()

    if SpawnCount <= 0:
        SpawnLocation = GetSpawnCoordinates()
        enemyList.append(Get_Enemy())
        EnemyCount += 1
        SpawnCount = 5000
    elif SpawnCount != 0:
        SpawnCount = SpawnCount - Countdown
    if EnemyCount == MaximumEnemies:
        SpawnCount = 5000
        Countdown = 0

    Arrow_Hit_Selecter()

    screen.blit(healthbar, (5, 5))
    for currenthealth in playerHealth:
        screen.blit(health, (currenthealth + 8, 8))

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
            if event.key == K_1:
                Selected_Arrow = Basic_Arrow
                Arrow_Attribute_Selecter()
            if event.key == K_2:
                Selected_Arrow = Steel_Arrow
                Arrow_Attribute_Selecter()
            if event.key == K_3:
                Selected_Arrow = HollowPoint_Arrow
                Arrow_Attribute_Selecter()
            if event.key == K_4:
                Selected_Arrow = Tri_Arrow
                Arrow_Attribute_Selecter()
            if event.key == K_5:
                Selected_Arrow = Frost_Arrow
                Arrow_Attribute_Selecter()
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
            Arrow_Coordinate_Selecter()

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