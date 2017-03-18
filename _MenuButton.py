from GameTile import *
import pygame

class MenuButton(GameTile):
    def __init__(self, rect, screen, x, y, action):
        super().__init__(rect, screen, x, y)
        self.color = (157, 157, 157)
        self.action = action

    def setColor(self, color):
        self.color = color

    def getAction(self):
        return self.action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
