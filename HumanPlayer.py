from GameBoard import GameBoard
import random
class HumanPlayer(object):
    def __init__(self, name):
        self.gameBoard = GameBoard(10,10)
        self.name = name

    def getName(self):
        return self.name

    def shipPlacement(self, length):
        while True:
            x = random.randint(0, len(self.gameBoard.gameGrid[1]) - 1)
            y = random.randint(0, len(self.gameBoard.gameGrid[0]) - 1)
            point = [x, y]
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
        directionList = [[1, 0], [0, 1], [-1, 0], [0,-1]]

        while True:
            if len(directionList) == 0:
                print("EMPTY")
                return False
            direction = random.choice(directionList)
            resultsList = [self.checkValidPlacement([point[0] + i * direction[0], point[1] + i * direction[1]]) for i in range(length)]        
            if all(resultsList) == True:
                return direction
            else:
                directionList.remove(direction)


    '''def getInput(self):
        xAnswers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        yAnswers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        yDict = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9}
        while True:
            x = input("Select a column (1 - 10): ")
            if x in xAnswers:
                x = int(x) - 1
                if 0 <= x <= (len(self.gameBoard.gameGrid[0])):
                    break
            else:
                print("Please choose a number between 1 and 10")

        while True:
            y = (input("Select a row (A - J): "))
            if y in yAnswers:
                y = y.upper()
                y = yDict[y]
                if 0 <= y <= (len(self.gameBoard.gameGrid[0])):
                    
                    return [x, y]
         

    #Take an x and y from the getInput function and make sure that spot hasn't been guessed
    def getGuess(self):
        while True:
            self.guess = self.getInput()
            x = self.guess[0]
            y = self.guess[1]

            if (self.gameBoard.gameGrid[y][x] == 0):
                return [x, y]'''