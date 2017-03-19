from GameBoard import GameBoard
import random
from HitShip import HitShip

class ComputerPlayer(object):
    def __init__(self, num):
        self.gameBoard = GameBoard(10, 10)

        self.guessedPoints = []
        self.hitGuesses = []
        #Possibly track sunk points also

        self.name = "Player {}".format(num)
        self.hitShips = []
        self.mode = "seek"
        self.goodGuesses = [(2, 2), (2, 4), (2, 6), (3, 3), (3, 5), (3, 7), (4, 2), (4, 4), (4, 6), (5, 3), (5, 5), (5, 7), (6, 2), (6, 4), (6, 6), (7, 3), (7, 5), (7, 7)]
        self.edgeGuesses = [(0,0), (0,2), (0,4), (0,6), (0,8), (1,1), (1,3), (1,5), (1,7), (1,9), (2,0), (2,8), (3,1), (3,9), (4, 0), (4, 8), (5, 1), (5, 9), (6, 0), (6, 8), (7, 1), (7, 9), (8, 0), (8, 2), (8, 4), (8, 6), (8, 8), (9, 1), (9, 3), (9, 5), (9, 7), (9, 9)]

    def getName(self):
        return self.name

#++++++++++++++++++++++++++++++++++++
#PLACING SHIPS
    
    def placeShips(self, shipLengths):
        #self.gameBoard.placeShip([5, (0,0), (0,1)])
        for i in range(len(shipLengths)):
            self.gameBoard.placeShip(self.shipPlacement(shipLengths[i]))

            

    #length, point, direction
    def shipPlacement(self, length):
        while True:
            x = random.randint(0, len(self.gameBoard.gameGrid[1]) - 1)
            y = random.randint(0, len(self.gameBoard.gameGrid[0]) - 1)
            point = (x, y)
            direction = self.getDirection(point, length)
            if direction != False:
                return [length, point, direction]

    def checkValidPlacement(self, point):
        x = point[0]
        y = point[1]
        #print(x, y)
        
        #check if point is outside bounds
        if (x < 0) or (x > (len(self.gameBoard.gameGrid[0]) - 1)):
            return False
        if (y < 0) or (y > (len(self.gameBoard.gameGrid[0]) - 1)):
            return False

        #What's the best way to check all the elements and see if one is false?
        for ship in self.gameBoard.shipList:
            if point in ship.coordinates:
                return False
        return True

    def getDirection(self, point, length):
        directionList = [(1, 0), (0, 1), (-1, 0), (0,-1)]

        while True:
            if len(directionList) == 0:
                #print("EMPTY")
                return False
            direction = random.choice(directionList)
            resultsList = [self.checkValidPlacement((point[0] + i * direction[0], point[1] + i * direction[1])) for i in range(length)]        
            if all(resultsList) == True:
                return direction
            else:
                directionList.remove(direction)

#+++++++++++++++++++++++++++

#GUESSING

    def getMove(self):

        while(True):

            if self.mode == "destroy":
                guess = self.destroyGuess()
            else:
                guess = self.seekGuess()

            if guess not in self.guessedPoints:
                self.guessedPoints.append(guess)
                if guess in self.goodGuesses:
                    self.goodGuesses.remove(guess)
                if guess in self.edgeGuesses:
                    self.edgeGuesses.remove(guess)
                return guess
            else:
                if guess in self.hitGuesses:
                    self.hitShips[0].updateGuesses(2)
                else:
                    self.hitShips[0].updateGuesses(1)


    def seekGuess(self):
        while(True):       
            if len(self.goodGuesses) != 0:
                list = self.goodGuesses
            else:
                list = self.edgeGuesses

            guess = random.choice(list)

            return guess
                

    def destroyGuess(self):

        return self.hitShips[0].getNextGuess()

        '''while (True):

            guess = self.hitShips[0].getNextGuess()

            if guess not in self.guessedPoints:
                return guess
            else:
                #self.hitShips[0].updateGuesses(2)
                print("Trying to guess an already guessed point " + str(guess) )
                #If the point has already been hit, update it
                self.updateInfo(guess, 2)
                
            #else:
                #self.hitShips[0].updateGuesses(1)'''

    def updateInfo(self, move, result):
        if result == 2 or 3:
            self.hitGuesses.append(move)

        if self.mode == "destroy":
            self.destroyUpdate(move, result)
        else:
            self.seekUpdate(move, result)


    def seekUpdate(self, move, result):
        if result == 1: #miss
            pass
        elif result == 2: #hit
            self.hitShips.append(HitShip(move))
            self.mode = "destroy"
        elif result == 3: #sink
            print("you somehow sunk a ship while seeking") 

    def destroyUpdate(self, move, result):

        self.hitShips[0].updateGuesses(result)

    def resolveSink(self, ship):
        for i in ship.hitList:
            if i in self.hitGuesses:
                self.hitGuesses.remove(i)
        self.hitShips.pop(0)
        self.mode = "seek"
        #if len(self.hitGuesses) != 0:
        #    for i in self.hitGuesses:
        #        self.hitShips.append(HitShip(i))
       
            

    def nextPoint(self, point, direction):
        #print(point, direction)
        nextPoint = (point[0] + direction[0], point[1] + direction[1])
        return nextPoint

    def checkAdjacent(self, point, directionList):
        point1 = (point[0] + directionList[0][0], point[1] + directionList[0][1])
        point2 = (point[0] + directionList[1][0], point[1] + directionList[1][1])
        if ((point1 in self.hitGuesses) or (point2 in self.hitGuesses)):
            return True
        else:
            return False



