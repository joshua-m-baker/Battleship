from ComputerPlayer import ComputerPlayer
from HumanPlayer import HumanPlayer
from BoardGui import BoardGui

class GameLoop(object):

    def __init__(self):
        self.computer = ComputerPlayer()
        self.human = HumanPlayer()
        self.computerBoard = BoardGui()
        self.humanBoard = BoardGui()

        self.shipLengths = [2, 3, 3, 4, 5]
        self.numberOfShips = len(self.shipLengths)
        self.run()
        

    def run(self):
        self.current = self.computer
        self.other = self.human

        self.currentBoard = self.computerBoard
        self.otherBoard = self.humanBoard
        #self.computerBoard.drawBoard()
        for i in range(self.numberOfShips):
            self.current.gameBoard.placeShip(self.current.shipPlacement(self.shipLengths[i]))
            self.other.gameBoard.placeShip(self.other.shipPlacement(self.shipLengths[i]))
            
        for ship in self.current.gameBoard.shipList:
                print(ship.coordinates)

        keepGoing = True
        while (keepGoing):
            self.currentBoard.updateGrid()
            move = self.currentBoard.checkEvents()
            guessedPoint = [move[0], move[1]]
            if guessedPoint not in self.current.gameBoard.guessedPoints:
                self.makeMove(guessedPoint)
                self.current.gameBoard.guessedPoints.append(guessedPoint)
            for i in self.current.gameBoard.shipList:
                if (i.checkSunk() == True):
                    print("You sunk a ship")
                    self.current.gameBoard.shipList.remove(i)
            if (self.current.gameBoard.checkWin() == True):
                keepGoing = False

            self.current, self.other = self.other, self.current
            self.currentBoard, self.otherBoard = self.otherBoard, self.currentBoard

        print("You win")


    def makeMove(self, point):
        if (self.current.gameBoard.checkPoint(point) == True):
            self.current.gameBoard.hitPoint(point, 2)
            #self.currentBoard.updateTile(point, 2)
        else:
            self.current.gameBoard.hitPoint(point, 1)
            #self.currentBoard.updateTile(point, 1)

    def redrawBoard(self, board):
        for i in range(len(board.gameGrid)):
            if (gameGrid[i] == 2):
                pass

g = GameLoop()
