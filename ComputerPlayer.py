from GameBoard import GameBoard
import random
class ComputerPlayer(object):
    def __init__(self):
        self.gameBoard = GameBoard(10, 10)
    #length, point, direction
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