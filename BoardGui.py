import pygame
from pygame.locals import *
import sys
import Button as bt

class BoardGui(object):

    def __init__(self):

        blue = (0, 0, 255)
        black = (0, 0, 0)
        red = (255, 0, 0)
        white = (255, 255, 255)

       
        self.backgroundColor = blue

        self.height = 480
        self.width = 640

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        #self.yMargin = 30   
        self.yMargin = 60
        self.xMargin = (self.width - self.height)/2 + self.yMargin
        self.numSquares = 10
        self.span = self.height - 2*(self.yMargin)
        self.squareSize = self.span/(self.numSquares)
        self.squareSizeInt = int(self.squareSize)

        self.tileList = []

        self.drawBoard()
        self.makeSquares()
        self.drawSquares()
        pygame.display.flip()

        #self.mainLoop()



    #Draw the board
    def drawBoard(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.backgroundColor)

        self.drawGrid()
        
    #Draw each of the tile objects
    def drawSquares(self):
        for i in self.tileList:
            i.draw()
            
    
    #This method will definitely be updated. First variables are a bunch of things for formatting

    def drawGrid(self):
        #Draw the lines of the grid. start/endPoint draws vertical lines, start/endPoint1 draws horizontal

        columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', '']
        rowList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '']

        for i in range(0, self.numSquares + 1):
            startX1 = self.xMargin + self.squareSize * i
            startY1 = self.yMargin 
            startPoint1 = (startX1, startY1)

            endX1 =  self.xMargin + self.squareSize * i
            endY1 = self.height - self.yMargin
            endPoint1 = (endX1, endY1)

            startX2 = self.xMargin
            startY2 = self.yMargin + self.squareSize * i
            startPoint2 = (startX2, startY2)

            endX2 =  self.width - self.xMargin
            endY2 = self.yMargin + self.squareSize * i 
            endPoint2 = (endX2, endY2)

            textSurface1 = self.font.render(rowList[i], True, (0,0,0))
            textSurface2 = self.font.render(columnList[i], True, (0,0,0))

            pygame.draw.line(self.screen, black, startPoint1, endPoint1, 1)
            self.screen.blit(textSurface1, (int(startX1 + self.squareSize//4), int(startY1 + - 20)))
            pygame.draw.line(self.screen, black, startPoint2, endPoint2, 1)
            self.screen.blit(textSurface2, (int(startX2 - 20), int(startY2 + self.squareSize//4)))

            

#++++++++++++++++++++++++++++++++++++++++++
    def makeSquares(self):
        #Creates all the tiles for the grid
        for i in range(0, self.numSquares):
            startX = self.xMargin + self.squareSize * i + 1
            startY = self.yMargin + 1
            for j in range(0, self.numSquares):
                startX1 = startX
                
                startY1 = self.yMargin + self.squareSize * j + 1

                rect1 = Rect((startX1, startY1), (self.squareSize - 1, self.squareSize - 1))

                self.tileList.append(bt.Button(rect1, blue, self.squareSize, self.screen, i, j))
#+++++++++++++++++++++++++++++++++++++++++++

    #def updateTile(self, point, color, status):
    def updateTile(self, point, status):
        x = point[0]
        y = point[1]
        index = x*10 + y
        self.tileList[index].setStatus(status)
        #self.tileList[index].setColor(color)

        #self.tileList[index].draw()

    def updateGrid(self):
        for i in self.tileList:
            i.draw
        

    def checkEvents(self):
        while True:
            pygame.display.flip()
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:
                        point = pygame.mouse.get_pos()

                        for i in self.tileList:
                            if i.checkClicked(point):
                                return (i.gridX, i.gridY)
                                #self.drawSquares()
                
          