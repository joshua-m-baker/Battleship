from GameBoard import GameBoard
import random
class HumanPlayer(object):
    def __init__(self, name, gui, placementGui):
        self.gameBoard = GameBoard(10,10)
        self.name = name
        self.guessedPoints = []
        self.gui = gui
        self.placementGui = placementGui
       
    def getName(self):
        return self.name

    def placeShips(self, shipLengths):

        gui = self.placementGui
        #gui.drawInfo(self.getName())
        #gui.drawGrid()
        #gui.drawSquares(self.gameBoard.gameGrid)
        gui.drawBoard(self.gameBoard.gameGrid, self.getName())

        for i in shipLengths:
            #gui.drawSquares(self.gameBoard.gameGrid)
            gui.updateSquares(self.gameBoard.gameGrid)
            print("place a ship of length: " + str(i))
            point1 = self.getPlacement()
            self.gameBoard.changePoint(point1)
            #self.gui.drawSquares(self.gameBoard.gameGrid)
            keepGoing = True
            while (keepGoing == True):
                #self.gui.drawSquares(self.gameBoard.gameGrid)
                self.gui.updateSquares(self.gameBoard.gameGrid)
                point2 = self.getPlacement()
                
                
                dif = (point1[0] - point2[0], point1[1] - point2[1])
                
                if ((abs(dif[0]) == i-1) and (dif[1] == 0)): 
                    dir = (dif[0]//dif[0], 0)
                    
                    self.gameBoard.placeShip([i, point1, dir])
                    keepGoing = False
                elif ((dif[0] == 0) and (abs(dif[1]) == i-1)):
                    dir = (0, dif[1]//dif[1])
                    
                    self.gameBoard.placeShip([i, point1, dir])
                    keepGoing = False
                
                for k in self.gameBoard.shipList:
                    for j in k.coordinates:
                        self.gameBoard.changePoint(j)

            #self.gameBoard.placeShip(self.shipPlacement(shipLengths[i]))

        self.gameBoard.gameGrid = self.gameBoard.makeGameGrid(10,10)

    def updateInfo(self, move, result):
        pass

    def getMove(self):
        validInput = False
        while (validInput == False):
            move = self.gui.checkEvents()
            if move not in self.guessedPoints:
                self.guessedPoints.append(move)
                validInput = True
        return move

    def getPlacement(self):
        validInput = False
        while (validInput == False):
            move = self.placementGui.checkEvents()
            validInput = True
        return move

    def resolveSink(self, ship):
        pass



