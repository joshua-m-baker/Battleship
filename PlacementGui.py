from AbstractGui import AbstractGui
import pygame
#from pygame.locals import *
from MenuButton import MenuButton
from GameTile import GameTile
from Menu import Menu
from BoardGui import BoardGui
#from PauseMenu import PauseMenu

class PlacementGui(AbstractGui):
    def __init__(self):
        super().__init__()

        self.lastBoardList = []
        self.lastInfo = ""

        self.menuButtons = []

        self.menuButton = MenuButton(pygame.Rect((0,0), (30, 30)), self.screen, lambda : self.toggleMenu())
        self.menuButtons.append(self.menuButton)

        self.boardGui = BoardGui(self.screen, pygame.Rect((0,0), (self.screen.get_width(), self.screen.get_height())), "Player 1")
        #self.board2 = BoardGui(self.screen, pygame.Rect((320,0), (320, 480)))

        #self.makeSquares()

    def drawBoard(self, boardlist):
        self.clearScreen()
        self.lastBoardList = boardlist
        self.boardGui.drawBoard(boardlist)
        self.menuButton.draw()
        pygame.display.flip()

    def updateSquares(self, boardlist):
        self.boardGui.drawSquares(boardlist)
        pygame.display.flip()

    def drawInfo(self, info):
        self.lastInfo = info
        #self.screen.fill(blue)

    def toggleMenu(self):
        #print("clicked menu")
        #p = PauseMenu()
        p = Menu(self.screen)
        self.performAction(p.main())
        
        self.closeMenu()

        ##Add the opaque background
        #s = pygame.Surface((self.screenWidth, self.screenHeight))
        #s.set_alpha(75)
        #s.fill((255,255,255))
        #self.screen.blit(s, (0,0))
        #self.menuButtons()

    def closeMenu(self):
        self.clearScreen()
        self.drawBoard(self.lastBoardList)

    def performAction(self, f):
        f()

    def clearScreen(self):
        pygame.draw.rect(self.screen, self.blue, pygame.Rect((0,0), (self.width, self.height)))

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
                            

                    for i in self.boardGui.tileList:
                        if i.checkClicked(point):
                            return (i.gridX, i.gridY)
                            #self.drawSquares()

    def checkEvents2(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
