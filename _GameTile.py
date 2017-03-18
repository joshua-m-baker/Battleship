import pygame

class GameTile(object):
    def __init__(self, rect, screen, x, y):
        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)
        grey = (157, 157, 157)
        
        self.unclickedColor = blue
        self.missColor = white
        self.hitColor = red
        self.menuColor = grey

        self.gridX = x
        self.gridY = y

        #self.size = size
        self.screen = screen

        self.rect = rect

    def draw(self, status):
        #print(status)
        if status == 0:
            color = self.unclickedColor
        elif status == 1:
            color = self.missColor
        elif status == 2 or 3:
            color = self.hitColor
            
        pygame.draw.rect(self.screen, color, self.rect)

    def checkClicked(self, point):
        #hit = False
        if self.rect.collidepoint(point):
            return True
        else:
            return False


