from AbstractGui import AbstractGui
import pygame
from MenuButton import MenuButton
from GameTile import GameTile
from Menu import Menu
from BoardGui import BoardGui

class PlacementGui(AbstractGui):
    def __init__(self):
        super().__init__()

        self.lastBoardList = []
        self.lastInfo = ""

        self.menuButtons = []
     
        #self.boardGui = BoardGui(self.screen, pygame.Rect((0,0), (self.screen.get_width(), self.screen.get_height())), "Player 1", 35)
        self.boardGui = BoardGui(self.screen, pygame.Rect((0,20), (self.screen.get_width(), self.screen.get_height())), "Player 1", 35)
        

        #self.makeSquares()
        self.addMenuButtons()
    
    def addMenuButtons(self):
        self.menuButton = MenuButton(pygame.Rect((0,0), (30, 30)), self.screen, lambda : self.toggleMenu())
        self.menuButtons.append(self.menuButton)
    

    def drawBoard(self, boardlist):
        self.clearScreen()
        if (boardlist != []):
            self.lastBoardList = boardlist
        else:
            print("Empty boardlist")
        self.boardGui.drawBoard(boardlist)
        self.menuButton.draw()
        self.drawInfo(self.lastInfo)
        pygame.display.flip()

    def updateSquares(self, boardlist):
        if (boardlist != []):
            self.lastBoardList = boardlist
        else:
            print("Empty boardlist")
        self.boardGui.drawSquares(boardlist)
        self.drawInfo(self.lastInfo)
        pygame.display.flip()

    def drawInfo(self, info):
        self.lastInfo = info
        self.drawText("Place a ship of length {}".format(info))

        #self.screen.fill(blue)

    def toggleMenu(self):
        #print("clicked menu")
        #p = PauseMenu()
        p = Menu(self.screen)
        p.drawButtons()
        action = p.main()
        
        self.performAction(action)
        
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
        self.updateSquares(self.lastBoardList)

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
