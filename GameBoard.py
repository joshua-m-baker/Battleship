#Ship info [length, point, direction]

from Ship import Ship

class GameBoard(object):
    def __init__(self, length, width):
        self.gameGrid = self.makeGameGrid(length, width)
        self.shipList = []
        self.sunkenShips = []
        self.guessedPoints = []

    def makeGameGrid(self, length, width):

        fullList = [[0 for j in range(width)] for i in range(length)] 

        return fullList

    def placeShip(self, shipInfo):
        length = shipInfo[0]
        point = shipInfo[1]
        direction = shipInfo[2]
        self.shipList.append(Ship(length, point, direction))

    def changePoint(self, point, value = 2):
        self.gameGrid[point[1]][point[0]] = value

    def checkPoint(self, point):
        for ship in self.shipList:
            if (ship.checkPoint(point) == True):
                return True
        return False

    #Add hitting a ship under this method
    def hitPoint(self, point, value):
        x = point[0]
        y = point[1]

        for ship in self.shipList:
            if point in ship.coordinates:
                ship.hitShip(point)

        self.gameGrid[y][x] = value
       
    def checkWin(self):
        if len(self.shipList) == 0:
            return True
        else:
            return False
