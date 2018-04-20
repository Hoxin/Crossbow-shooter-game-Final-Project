
from turtle import *
import pygame

class Armory():
    def __init__(self, weaponName, arrow_image, attackPower, arrowRange):
        self.weaponName = weaponName
        self.arrow_image = pygame.image.load("resources/image/bullet.png")
        self.attackpower = attackPower
        self.screen = self.arrowTurtle.getscreen()
        self.arrowRange = arrowRange
    def arrowRange_Set():
        ArrowRange = print(self.arrowRange)
        return ArrowRange