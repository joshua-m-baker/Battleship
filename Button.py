import pygame

class Button(object):
    def __init__(self, rect, size, screen, x, y):
        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)
        
        self.unclickedColor = blue
        self.missColor = white
        self.hitColor = red

        self.gridX = x
        self.gridY = y

        self.size = size
        self.screen = screen

        self.rect = rect

    def draw(self, status):
        #print(status)
        if status == 1:
            color = self.missColor
        elif status == 2:
            color = self.hitColor
        else:
            color = self.unclickedColor
        pygame.draw.rect(self.screen, color, self.rect)

    def checkClicked(self, point):
        #hit = False
        if self.rect.collidepoint(point):
            return True
        else:
            return False


