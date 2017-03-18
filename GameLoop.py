from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from PlacementGui import PlacementGui
import time

""" 
Add manual ship placement
"""

class GameLoop(object):

    def __init__(self):
        
        self.boardGui = PlacementGui()
        #self.placementGui = BoardGui()
        self.placementGui = PlacementGui()
        self.computer = ComputerPlayer("Player 2")
        #self.human = ComputerPlayer("Player 1")
        self.human = HumanPlayer("Player 1", self.boardGui, self.placementGui)

        self.shipLengths = [2, 3, 3, 4, 5]
        self.numberOfShips = len(self.shipLengths)
        self.run()

    def run(self):
        self.current = self.human
        self.other = self.computer
        
        self.current.placeShips(self.shipLengths)
        self.other.placeShips(self.shipLengths)

        self.boardGui.drawBoard(self.other.gameBoard.gameGrid, self.current.getName())
        
        keepGoing = True
        while (keepGoing):

            self.boardGui.checkEvents2()

            otherBoard = self.other.gameBoard

            self.boardGui.updateSquares(otherBoard.gameGrid)

            #self.boardGui.drawInfo(self.current.getName())
            #self.boardGui.drawGrid()
            #self.boardGui.drawSquares(otherBoard.gameGrid)
           
            move = self.current.getMove()

            if type(self.current) is ComputerPlayer:
                
                time.sleep(.75)
           
            if (otherBoard.checkPoint(move) == True):
                result = 2
            else:
                result = 1

            otherBoard.hitPoint(move, result)
            self.current.updateInfo(move, result)

            #self.boardGui.drawSquares(otherBoard.gameGrid)
            self.boardGui.updateSquares(otherBoard.gameGrid)

            for i in otherBoard.shipList:
                if (i.checkSunk() == True):
                    print("You sunk a ship at " + str( move))
                    self.current.updateInfo(move, 3)
                    ship = i
                    otherBoard.shipList.remove(i)
                    self.current.resolveSink(ship)

            time.sleep(1)
            

            if (otherBoard.checkWin() == True):
                print(self.current.name + " wins!")
                keepGoing = False
            else:
                
                self.swapPlayers()
                #pass

    def swapPlayers(self):
        self.current, self.other = self.other, self.current

g = GameLoop()
