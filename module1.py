import pygame
from pygame.locals import *
import sys

pygame.init()

blue = (0, 0, 255)
white = (255, 255, 255)
backgroundColor = blue

yOffset = 200
xOffset = 0

height = 480
width = 640

yMargin = 30
xMargin = (width - height)/2 + yMargin

gridWidth = 10
#gridLineLength = width - 2*xMargin
span = width - 2*xMargin
squareSize = span/(gridWidth - 1)
print(squareSize)

screen = pygame.display.set_mode((width, height))
screen.fill(backgroundColor)

for i in range(0, gridWidth):
    startX = xMargin + squareSize * i 
    startY = yMargin
    startPoint = (startX, startY)

    endX =  xMargin + squareSize * i
    endY = height - yMargin
    endPoint = (endX, endY)
    print(startPoint)
    pygame.draw.line(screen, white, startPoint, endPoint, 1)

for i in range(0, gridWidth):
    startX = xMargin
    startY = yMargin + squareSize * i
    startPoint = (startX, startY)

    endX =  width - xMargin
    endY = yMargin + squareSize * i
    endPoint = (endX, endY)

    pygame.draw.line(screen, white, startPoint, endPoint, 1)


loop = True
while loop:

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
            sys.exit()


    pygame.display.flip()
    


