import pygame
from AbstractGui import AbstractGui
from BoardGui import BoardGui
from Menu import Menu
from MenuButton import MenuButton

class GameGui(AbstractGui):
    def __init__(self):
        super().__init__()

        self.gameBoards = []
        self.menuButtons = []

        self.lastInfo = ""

        width = self.screen.get_width()
        height = self.screen.get_height()

        self.menuButton = MenuButton(pygame.Rect((0,0), (30, 30)), self.screen, lambda : self.toggleMenu())
        self.menuButtons.append(self.menuButton)

        
        self.player1Board = BoardGui(self.screen, pygame.Rect((0,20), (width//2, height)), "Player 1")
        self.player2Board = BoardGui(self.screen, pygame.Rect((width//2, 20), (width//2, height)), "Player 2")
        self.gameBoards.append(self.player1Board)
        self.gameBoards.append(self.player2Board)

        self.currentBoard = self.player2Board

        self.lastP1Boardlist = []
        self.lastP2Boardlist = []


    def drawBoard(self, p1Boardlist, p2Boardlist):
        self.clearScreen()
        self.lastP1Boardlist = p1Boardlist
        self.lastP2Boardlist = p2Boardlist
        self.player1Board.drawBoard(p1Boardlist)
        self.player2Board.drawBoard(p2Boardlist)
        self.menuButton.draw()
        self.drawInfo(self.lastInfo)
        pygame.display.flip()

    def updateSquares(self, p1Boardlist, p2Boardlist):
        self.lastP1Boardlist = p1Boardlist
        self.lastP2Boardlist = p2Boardlist
        self.player1Board.drawSquares(p1Boardlist)
        self.player2Board.drawSquares(p2Boardlist)
        self.drawInfo(self.lastInfo)
        pygame.display.flip()
    
    def toggleMenu(self):
        p = Menu(self.screen)
        p.drawButtons()
        self.performAction(p.main())
        self.closeMenu()

    def closeMenu(self):
        self.clearScreen()
        self.drawBoard(self.lastP1Boardlist, self.lastP2Boardlist)

    def drawInfo(self, info):
        self.lastInfo = info
        self.drawText(info)

    def performAction(self, f):
        f()

    def clearScreen(self):
        pygame.draw.rect(self.screen, self.blue, pygame.Rect((0,0), (self.width, self.height)))

    def checkEvents(self, player):
        if (player == 2):
            self.currentBoard = self.player1Board
        elif (player == 1):
            self.currentBoard = self.player2Board

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
                            

                    for i in self.currentBoard.tileList:
                        if i.checkClicked(point):
                            return (i.gridX, i.gridY)
                            #self.drawSquares()

    def checkEvents2(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


