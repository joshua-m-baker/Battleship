from AbstractGui import AbstractGui
import pygame
from pygame.locals import *
from MenuButton import MenuButton
from GameTile import GameTile
from Menu import Menu
#from PauseMenu import PauseMenu

class PlacementGui(AbstractGui):
    def __init__(self):
        super().__init__()

        self.yMargin = 60
        self.xMargin = (self.width - self.height)/2 + self.yMargin
        self.numSquares = 10
        self.span = self.height - 2*(self.yMargin)
        self.squareSize = self.span/(self.numSquares)
        self.squareSizeInt = int(self.squareSize)

        self.lastBoardList = []
        self.lastInfo = ""

        self.menuButtons = []
        self.tileList = []

        menuButton = MenuButton(Rect((0,0), (30, 30)), self.screen, lambda : self.toggleMenu())
        self.menuButtons.append(menuButton)

        self.menuStatus = False

        self.makeSquares()

    def drawBoard(self, boardlist, info):
        self.screen.fill(self.blue)

        self.drawGrid()
        self.drawInfo(info)
        self.drawSquares(boardlist)
        pygame.display.flip()

    def updateSquares(self, boardlist):
        self.drawSquares(boardlist)
        pygame.display.flip()


    def drawGrid(self):
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

            pygame.draw.line(self.screen, self.black, startPoint1, endPoint1, 1)
            self.screen.blit(textSurface1, (int(startX1 + self.squareSize//4), int(startY1 + - 20)))
            pygame.draw.line(self.screen, self.black, startPoint2, endPoint2, 1)
            self.screen.blit(textSurface2, (int(startX2 - 20), int(startY2 + self.squareSize//4)))

    def drawSquares(self, boardList):
        self.lastBoardList = boardList
        for i in range(len(self.tileList)):
            self.tileList[i].tileDraw(boardList[int(i%10)][int(i//10)])
        for i in self.menuButtons:
            i.draw()
        #print(" ")

    def drawInfo(self, info):
        self.lastInfo = info
        #self.screen.fill(blue)
        textSurface1 = self.font.render(info, True, (0,0,0))
        self.screen.blit(textSurface1, (40,40))

    def makeSquares(self):
        #Creates all the tiles for the grid
        for i in range(0, self.numSquares):
            startX = self.xMargin + self.squareSize * i + 1
            startY = self.yMargin + 1
            for j in range(0, self.numSquares):
                startX1 = startX
                
                startY1 = self.yMargin + self.squareSize * j + 1

                rect1 = Rect((startX1, startY1), (self.squareSize - 1, self.squareSize - 1))

                self.tileList.append(GameTile(rect1, self.screen, i, j))

    def makeSquares(self):
        #Creates all the tiles for the grid
        for i in range(0, self.numSquares):
            startX = self.xMargin + self.squareSize * i + 1
            startY = self.yMargin + 1
            for j in range(0, self.numSquares):
                startX1 = startX
                
                startY1 = self.yMargin + self.squareSize * j + 1

                rect1 = Rect((startX1, startY1), (self.squareSize - 1, self.squareSize - 1))

                self.tileList.append(GameTile(rect1, self.screen, i, j))




    def toggleMenu(self):
        print("clicked menu")
        #p = PauseMenu()
        p = Menu(self.screen)
        self.performAction(p.main())
        self.clearScreen
        self.drawBoard(self.lastBoardList, self.lastInfo)

        ##Add the opaque background
        #s = pygame.Surface((self.screenWidth, self.screenHeight))
        #s.set_alpha(75)
        #s.fill((255,255,255))
        #self.screen.blit(s, (0,0))
        #self.menuButtons()

    def closeMenu(self):
        self.clearScreen()
        self.drawBoard(self.lastBoardList, self.lastInfo)

    def menuButtons(self):
        pass
        #buttonHeight = 50
        #buttonWidth = 200
        #buttonX = (self.screenWidth//2) - (buttonWidth // 2)
        #buttonY = (self.screenHeight//2) - (buttonHeight //2)
        #point = (buttonX, buttonY)
        #quitButton = MenuButton(pygame.Rect(point, (200, 50)), self.screen, lambda : self.quit())
        #self.menuButtons.append(quitButton)

    def performAction(self, f):
        f()

    def clearScreen(self):
        pygame.draw.rect(self.screen, blue, Rect((0,0), (self.width, self.height)))

    def checkEvents(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                
                elif event.type == pygame.K_UP:
                    if pygame.K_ESCAPE:
                        self.performAction(self.menuButtons[0].getAction())
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    point = pygame.mouse.get_pos()

                    for i in self.menuButtons:
                        if i.checkClicked(point):
                            self.performAction(i.getAction())
                            

                    for i in self.tileList:
                        if i.checkClicked(point):
                            return (i.gridX, i.gridY)
                            #self.drawSquares()

    def checkEvents2(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
