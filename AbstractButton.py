import pygame

class AbstractButton(object):
    def __init__(self, rect, screen):
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.grey = (157, 157, 157)

        self.color = self.grey
        self.rect = rect
        self.screen = screen

    def setColor(self, color):
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def checkClicked(self, point):
        #hit = False
        if self.rect.collidepoint(point):
            return True
        else:
            return False


