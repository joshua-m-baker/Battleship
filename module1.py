import pygame
from pygame.locals import *
import sys

pygame.init()

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
backgroundColor = blue

height = 480
width = 640

yMargin = 30
yMargin = yMargin
xMargin = (width - height)/2 + yMargin

gameBoard = [[0 for j in range(10)] for i in range(10)]
tileList = []

numSquares = 10
#gridLineLength = width - 2*xMargin
#span = width - 2*xMargin 
span = height - 2*yMargin
squareSize = span/(numSquares)
squareSizeInt = int(squareSize)
print(squareSize)

screen = pygame.display.set_mode((width, height))
screen.fill(backgroundColor)

class Tile(object):

    def __init__(self, x = 0, y = 0, index = (0,0)):
        print(type(int(squareSize)))
        self.surface = pygame.Surface((int(squareSize), int(squareSize)))
        #self.color = blue
        self.color = red
        self.rect = pygame.Rect(x, y, squareSize, squareSize)
        self.draw()

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, width = 0)



    def update(self):
        if gameBoard[IndexError[1]][IndexError[0]] == 1:
            self.color = black
        elif gameBoard[IndexError[1]][IndexError[0]] == 2:
            self.color = red
        else:
            self.color = blue
        self.draw()

     

for i in range(0, numSquares + 1):
    startX = xMargin + squareSize * i
    startY = yMargin 
    startPoint = (startX, startY)

    endX =  xMargin + squareSize * i
    endY = height - yMargin
    endPoint = (endX, endY)
    print(startPoint)

    
    tileList.append(Tile(startX, startY, (0, i)))
    pygame.draw.line(screen, white, startPoint, endPoint, 1)

for i in range(0, numSquares + 1):
    startX = xMargin
    startY = yMargin + squareSize * i
    startPoint = (startX, startY)

    endX =  width - xMargin
    endY = yMargin + squareSize * i 
    endPoint = (endX, endY)

    tileList.append(Tile(startX, startY, (i, 0)))
    pygame.draw.line(screen, white, startPoint, endPoint, 1)

loop = True
while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
            


    pygame.display.flip()
    
pygame.quit()
sys.exit()
            



