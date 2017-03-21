from GameBoard import GameBoard
import random
from PlacementGui import PlacementGui
import pygame

class HumanPlayer(object):
    def __init__(self, num, gui):
        self.gameBoard = GameBoard(10,10)
        self.name = "Player {}".format(num)
        self.guessedPoints = []
        self.gui = gui
        self.placementGui = PlacementGui()
        self.num = num
       
    def getName(self):
        return self.name

    def placeShips(self, shipLengths):
        gui = self.placementGui
        #gui.drawInfo(self.getName())
        #gui.drawGrid()
        #gui.drawSquares(self.gameBoard.gameGrid)
        gui.drawBoard(self.gameBoard.gameGrid)

        for i in shipLengths:
            keepGoing1 = True
            while (keepGoing1):
                keepGoing2 = True
                #gui.drawSquares(self.gameBoard.gameGrid)

                gui.updateSquares(self.gameBoard.gameGrid)
                gui.drawInfo(i)
                #print("place a ship of length: " + str(i))
                point1 = self.getPlacement()
                if (self.checkValidPlacement(point1) == True):
                    self.gameBoard.changePoint(point1 , 2)
                else:
                    keepGoing2 = False
                #self.gui.drawSquares(self.gameBoard.gameGrid)
                
                while (keepGoing2 == True):
                    #self.gui.drawSquares(self.gameBoard.gameGrid)
                    gui.updateSquares(self.gameBoard.gameGrid)
                    point2 = self.getPlacement()
                
                    if (self.checkValidPlacement(point2) == True) and (point1 != point2):
                
                        dif = (point1[0] - point2[0], point1[1] - point2[1])
                
                        if ((abs(dif[0]) == i-1) and (dif[1] == 0)): 
                            dir = ((-1 * dif[0])//abs(dif[0]), 0)
                            
                            
                        elif ((dif[0] == 0) and (abs(dif[1]) == i-1)):
                            dir = (0, (-1 * dif[1])//abs(dif[1]))

                        else:
                            dir = (10,10)
                         
                        validPlacement = True   
                        for j in range(i):
                            if (self.checkValidPlacement((point1[0] + dir[0]*j, point1[1] + dir[1]*j)) == True):
                                validPlacement = True
                            else:
                                validPlacement = False    
                                break 
                        
                        if validPlacement == True:                
                           self.gameBoard.placeShip([i, point1, dir])
                           for k in self.gameBoard.shipList:
                               for j in k.coordinates:
                                   self.gameBoard.changePoint(j, 2)
                           keepGoing1 = False
                           keepGoing2 = False
                        else:
                            self.gameBoard.changePoint(point1, 0)
                            keepGoing2 = False
                        

                    else:
                        self.gameBoard.changePoint(point1, 0)
                        keepGoing2 = False

                #self.gameBoard.placeShip(self.shipPlacement(shipLengths[i]))

        #self.gameBoard.gameGrid = self.gameBoard.makeGameGrid(10,10)
        for k in self.gameBoard.shipList:
            for j in k.coordinates:
                self.gameBoard.changePoint(j, 4)

    def updateInfo(self, move, result):
        pass

    def getMove(self):
        validInput = False
        while (validInput == False):
            move = self.gui.checkEvents(self.num)
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

    def checkValidPlacement(self, point):
        x = point[0]
        y = point[1]
        #print(x, y)
        
        #check if point is outside bounds
        if (x < 0) or (x > (len(self.gameBoard.gameGrid[0]) - 1)):
            return False
        if (y < 0) or (y > (len(self.gameBoard.gameGrid[0]) - 1)):
            return False

        
        if (self.gameBoard.checkPoint(point) != False):
            return False
        else:
            return True

    def resolveSink(self, ship):
        pass



