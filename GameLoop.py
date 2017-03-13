from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from BoardGui import BoardGui
import time

class GameLoop(object):

    def __init__(self):
        self.computer = ComputerPlayer("Player 2")
        self.human = HumanPlayer("Player 1")
        self.boardGui = BoardGui()

        self.shipLengths = [2, 3, 3, 4, 5]
        self.numberOfShips = len(self.shipLengths)
        self.run()

    def run(self):
        self.current = self.human
        self.other = self.computer
        
        self.computerPlaceShips()
        self.humanPlaceShips()
        
        keepGoing = True
        while (keepGoing):

            otherBoard = self.other.gameBoard

            self.boardGui.drawInfo(self.current.getName())
            self.boardGui.drawGrid()
            self.boardGui.drawSquares(otherBoard.gameGrid)
           
            if type(self.current) is HumanPlayer:
                validInput = False
                while (validInput == False):
                    move = self.boardGui.checkEvents()
                    if move not in otherBoard.guessedPoints:
                        otherBoard.guessedPoints.append(move)
                        validInput = True
            else:
                time.sleep(1)
                move = self.current.makeGuess()
           
            if (otherBoard.checkPoint(move) == True):
                otherBoard.hitPoint(move, 2)
            else:
                otherBoard.hitPoint(move, 1)

            self.boardGui.drawSquares(otherBoard.gameGrid)

            for i in otherBoard.shipList:
                if (i.checkSunk() == True):
                    print("You sunk a ship")
                    otherBoard.shipList.remove(i)

            time.sleep(2)

            if (otherBoard.checkWin() == True):
                print("You win")
                keepGoing = False
            else:
                self.swapPlayers()

            #self.current, self.other = self.other, self.current
            #self.currentBoard, self.otherBoard = self.otherBoard, self.currentBoard

        

    def computerPlaceShips(self):
        for i in range(self.numberOfShips):
            self.computer.gameBoard.placeShip(self.computer.shipPlacement(self.shipLengths[i]))
            
        #for ship in self.computer.gameBoard.shipList:
        #        print(ship.coordinates)

    def humanPlaceShips(self):
        for i in range(self.numberOfShips):
            self.human.gameBoard.placeShip(self.human.shipPlacement(self.shipLengths[i]))

    def swapPlayers(self):
        self.current, self.other = self.other, self.current

g = GameLoop()
