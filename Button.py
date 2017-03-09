

import pygame

class Button(object):
    def __init__(self, rect, color, size, screen, x, y):
        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)
        
        self.unclickedColor = blue
        self.missColor = white
        self.hitColor = red
        self.color = color

        # 0 = not guessed, 1 is missed, 2 is hit
        self.status = 0

        self.gridX = x
        self.gridY = y

        self.size = size
        self.screen = screen

        self.rect = rect

    def draw(self):
        if self.status == 1:
            color = self.missColor
        elif self.status == 2:
            color = self.hitColor
        else:
            color = self.unclickedColor

        pygame.draw.rect(self.screen, color, self.rect)

    #def setColor(self, color):
    #   self.color = color

    def setStatus(self, newStatus):
        self.status = newStatus

    #if point is inside shape, return true and change the color of the tile
    '''def checkClicked(self, point):
        if self.rect.collidepoint(point):
            return True
        else:
            return False'''

    def checkClicked(self, point):
        hit = False
        if self.rect.collidepoint(point):
            #if (hit == True):
            #    self.color = self.hitColor
            #else:
            #    self.color = self.missColor
            return True
        else:
            return False


