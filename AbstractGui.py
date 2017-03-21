import pygame
from pygame.locals import *
import sys

class AbstractGui(object):
    def __init__(self):
        pygame.init()

        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)

        self.backgroundColor = self.blue

        info = pygame.display.Info()
        #self.width = info.current_w
        #self.height = info.current_h
        self.width = 640
        self.height = 480
        #self.width = 1280
        #self.height = 720

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()

    def drawText(self, text):

        textSize = self.font.size(text)

        textWidth = textSize[0]
        textHeight = textSize[1]

        boxWidth = self.screen.get_width()//2
        boxHeight = self.height//10

        rect = pygame.Rect(((self.screen.get_width()//2) - boxWidth//2, 10), (boxWidth, boxHeight))

        rectX = rect.left
        rectY = rect.top

        rectWidth = rect.width
        rectHeight = rect.height

        textX = rectX + rectWidth//2 - textWidth//2
        textY = rectY + rectHeight//2 - textHeight//2

        textRender = self.font.render(text, True, (0,0,0))
        pygame.draw.rect(self.screen, self.black, pygame.Rect((rectX-1, rectY - 1), (rectWidth + 2, rectHeight + 2)))
        pygame.draw.rect(self.screen, self.blue, rect)
        self.screen.blit(textRender, (textX, textY))

        pygame.display.flip()

        '''center = (self.screen.get_width())//2
        maxWidth = (self.screen.get_width())//2

        yPoint = 0

        nameText = self.font.render(text, True, (0,0,0))
        nameSize = self.font.size(text)

        textWidth = nameSize[0]
        textHeight = nameSize[1]'''