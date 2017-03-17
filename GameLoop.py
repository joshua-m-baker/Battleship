from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from BoardGui import BoardGui
import time

""" 
Add manual ship placement
Ai should be able to handle finding adjacent ships


"""

class GameLoop(object):

    def __init__(self):
        self.boardGui = BoardGui()
        self.computer = ComputerPlayer("Player 2")
        self.human = ComputerPlayer("Player 1")
        #self.human = HumanPlayer("Player 1", self.boardGui)
        

        self.shipLengths = [2, 3, 3, 4, 5]
        self.numberOfShips = len(self.shipLengths)
        self.run()

    def run(self):
        self.current = self.human
        self.other = self.computer
        
        self.current.placeShips(self.shipLengths)
        self.other.placeShips(self.shipLengths)
        
        keepGoing = True
        while (keepGoing):

            self.boardGui.checkEvents2()

            otherBoard = self.other.gameBoard

            self.boardGui.drawInfo(self.current.getName())
            self.boardGui.drawGrid()
            self.boardGui.drawSquares(otherBoard.gameGrid)
           
            move = self.current.getMove()

            if type(self.current) is ComputerPlayer:
                pass
                #time.sleep(.25)
           
            if (otherBoard.checkPoint(move) == True):
                result = 2
            else:
                result = 1

            otherBoard.hitPoint(move, result)
            self.current.updateInfo(move, result)

            self.boardGui.drawSquares(otherBoard.gameGrid)

            for i in otherBoard.shipList:
                if (i.checkSunk() == True):
                    #print("You sunk a ship at " + str( move))
                    self.current.updateInfo(move, 3)
                    ship = i
                    otherBoard.shipList.remove(i)
                    self.current.resolveSink(ship)

            #time.sleep(2)
            

            if (otherBoard.checkWin() == True):
                print(self.current.name + " wins!")
                keepGoing = False
            else:
                
                self.swapPlayers()
                #pass

    def swapPlayers(self):
        self.current, self.other = self.other, self.current

g = GameLoop()
