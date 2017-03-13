
class HitShip():
    def __init__(self, point):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.nextPoints = [(point[0] + i[0], point[1] + i[1]) for i in directions]
        for i in range(len(self.nextPoints)):
            if self.checkValidPlacement(self.nextPoints[i]) == False:
                removeList.append(i)
        for i in removeList:
            self.remove(i)

    def updateGuesses(self, result):
        if result == 1:
            self.remove(0)
        else:
            self.nextPoint()
            if self.checkValidPlacement(self.nextPoints[0]) == False:
                self.remove(0)

    def nextPoint(self):
        self.nextPoints[0] = (self.nextPoints[0][0] + self.directions[0][0], self.nextPoints[0][1] + self.directions[0][1])


    def getNextGuess(self):
        return self.nextPoints[0]

    def remove(self, index):
        self.directions.pop(index)
        self.nextPoints.pop(index)

    def checkValidPlacement(self, point):
        x = point[0]
        y = point[1]

        #Hardcoded Values
        if (x < 0) or (x > 9):
            return False
        if (y < 0) or (y > 9):
            return False

        return True
        



