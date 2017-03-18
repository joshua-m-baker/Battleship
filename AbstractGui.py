import pygame
from pygame.locals import *
import sys

class AbstractGui(object):
    def __init__(self):

        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)

        self.backgroundColor = self.blue

        self.width = 640
        self.height = 480

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)
        pygame.display.flip()

    def quit(self):
        pygame.quit()
        sys.exit()