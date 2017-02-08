'''
Currently messy and not laid out super well. I play to reorganize and 
smooth everything a bit when I get the chance.

Just a gui for now, will be filled in with battleship stuff later. Tiles change color when clicked


'''

import pygame
from pygame.locals import *
import sys

pygame.init()

blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)



#class for the tiles in the grid
class Button(object):
    def __init__(self, rect, color, size, screen):
        
        self.unclickedColor = blue
        self.missColor = white
        self.hitColor = red
        self.color = self.unclickedColor

        self.size = size
        self.screen = screen

        self.rect = rect

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def setColor(self, color):
        self.color = color

    #if point is inside shape, return true and change the color of the tile
    def checkClicked(self, point):
        hit = False
        if self.rect.collidepoint(point):
            if (hit == True):
                self.color = self.hitColor
            else:
                self.color = self.missColor
            return True
        else:
            return False
            




class GameBoard(object):

    def __init__(self):
        self.blue = (0, 0, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        
        self.backgroundColor = blue

        self.height = 480
        self.width = 640


        self.drawBoard()
        self.mainLoop()


    #Draw the board then add everything
    def drawBoard(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)

        self.drawGrid()
        self.drawSquares()
        
    #Draw each of the tile objects
    def drawSquares(self):
        for i in self.tileList:
            i.draw()
            
    
    #This method will definitely be updated. First variables are a bunch of things for formatting

    def drawGrid(self):
        width = self.width
        height = self.height
        yMargin = 30
        yMargin = yMargin   
        xMargin = (width - height)/2 + yMargin
        numSquares = 10
        span = height - 2*yMargin
        squareSize = span/(numSquares)
        squareSizeInt = int(squareSize)
        print(squareSize)

        self.tileList = []


        #Draw the lines of the grid. start/endPoint draws vertical lines, start/endPoint1 draws horizontal
        for i in range(0, numSquares + 1):
            startX = xMargin + squareSize * i
            startY = yMargin 
            startPoint = (startX, startY)

            endX =  xMargin + squareSize * i
            endY = height - yMargin
            endPoint = (endX, endY)

            startX1 = xMargin
            startY1 = yMargin + squareSize * i
            startPoint1 = (startX1, startY1)

            endX1 =  width - xMargin
            endY1 = yMargin + squareSize * i 
            endPoint1 = (endX1, endY1)

            pygame.draw.line(self.screen, self.black, startPoint, endPoint, 1)
            pygame.draw.line(self.screen, self.black, startPoint1, endPoint1, 1)


        #Creates all the tiles for the grid
        for i in range(0, numSquares):
            startX = xMargin + squareSize * i + 1
            startY = yMargin + 1


            for j in range(0, numSquares):
                startX1 = startX
                
                startY1 = yMargin + squareSize * j + 1

                rect1 = Rect((startX1, startY1), (squareSize - 1, squareSize - 1))

                self.tileList.append(Button(rect1, blue, squareSize, self.screen))


    def mainLoop(self):
        loop = True
        while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                elif event.type == pygame.MOUSEBUTTONUP:
                    point = pygame.mouse.get_pos()
                    print(point)

                    #If the point was in one of the tiles, redraw everything. 
                    #Probably will be changed later to continuous fps
                    for i in self.tileList:
                        if i.checkClicked(point):
                            self.drawSquares()
                    #self.drawBoard()
                
            
            pygame.display.flip()
        pygame.quit()
        sys.exit()
    
def main():
    g = GameBoard()

if __name__ == "__main__":
    main()
  