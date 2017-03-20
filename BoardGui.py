import pygame
from GameTile import GameTile

class BoardGui(object):
    def __init__(self, screen, domainRect, name, marginPercent = 20):
        pygame.font.init()
        self.font = pygame.font.Font(None, 30)

        self.blue = (0, 0, 255)

        self.screen = screen
        self.name = "{}'s Board".format(name)

        self.nameText = self.font.render(self.name, True, (0,0,0))
        self.nameSize = self.font.size(self.name)

        self.fullRect = domainRect

        self.leftBound = domainRect.left
        self.rightBound = domainRect.right
        self.topBound = domainRect.top
        self.bottomBound = domainRect.bottom

        self.numSquares = 10

        self.tileList = []

        widthSpan = abs(self.rightBound - self.leftBound)
        heightSpan = abs(self.bottomBound - self.topBound)
        dif = abs(widthSpan - heightSpan)

        if widthSpan > heightSpan:
            self.leftBound = self.leftBound + (dif/2)
            self.rightBound = self.rightBound - (dif/2)

        else:
            self.topBound = self.topBound + (dif/2)
            self.bottomBound = self.bottomBound - (dif/2)

        #the total margin is 10% of the total span, split accross both sides (*/2)
        self.margin = ((self.rightBound - self.leftBound)/2) * (marginPercent/100)
        self.span = self.rightBound - 2*self.margin - self.leftBound

        self.startingPoint = (self.leftBound + self.margin, self.topBound + self.margin)

        self.squareSize = self.span// self.numSquares

        self.makeSquares()


    def makeSquares(self):
    #Creates all the tiles for the grid
        for i in range(0, self.numSquares):

            x = self.startingPoint[0] + self.squareSize * i + 1
            
            for j in range(0, self.numSquares):
                
                y = self.startingPoint[1] + self.squareSize * j + 1

                rect1 = pygame.Rect((x, y), (self.squareSize - 1, self.squareSize - 1))

                self.tileList.append(GameTile(rect1, self.screen, i, j))

    def drawSquares(self, boardList):
        self.lastBoardList = boardList
        for i in range(len(self.tileList)): 
            self.tileList[i].tileDraw(boardList[int(i%10)][int(i//10)])

    def drawGrid(self):
        
        columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        rowList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

        backingSize = (self.squareSize * 10) + 1
        pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(self.startingPoint, (backingSize, backingSize)))
        
        for i in range(self.numSquares):
            charPos = self.squareSize * i + self.squareSize//4
            num = self.font.render(rowList[i], True, (0,0,0))
            letter = self.font.render(columnList[i], True, (0,0,0))

            self.screen.blit(num, (int(self.startingPoint[0] + charPos), int(self.startingPoint[1] - 20)))
            self.screen.blit(letter, (int(self.startingPoint[0] - 20), int(self.startingPoint[1] + charPos)))

        middle = (self.fullRect.right - self.fullRect.left)//2
        xPos = self.fullRect.left + middle - self.nameSize[0]//2
        #xPos = self.fullRect.right//2
        yPos = (self.bottomBound) - self.margin
        self.screen.blit(self.nameText, (xPos, yPos))

    def drawBoard(self, gameBoard):
        #self.screen.fill(self.blue)
        self.drawGrid()
        self.drawSquares(gameBoard)
        pygame.display.flip()







        