
class HitShip(object):
    def __init__(self, point):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #Make a list of the four adjacent points to the given one
        self.points = [(point[0] + i[0], point[1] + i[1]) for i in self.directions]
        self.pointsCopy = [(point[0] + i[0], point[1] + i[1]) for i in self.directions]
        self.history = []
        self.removeList = []
        self.originalPoint = point
        self.guessedPoints = []

        for i in range(len(self.points)):
            for j in range(len(self.points)):
                if self.checkValidPlacement(self.points[j]) == False:
                    self.remove(j)
                    break


    def remove(self, index):

        #Remove the point and direction at an index
        if index > (len(self.directions) - 1):
            print("index out of directions list " + str(self.directions))
        if index > (len(self.points) - 1):
            print("index out of points list: "+ str(self.points))
        self.directions.pop(index)
        self.points.pop(index)

        #self.history.append(pt)

        #self.pastMoves.append(pt)

    def updateGuesses(self, result):
        #If it was a hit (2), then move the first point to the next one in that direction
        #If the new point is out of bounds, remove it and the direction
        #If it wasn't, then remove that point and direction

        if (result == 1):
            self.remove(0)
        elif (result == 2):
            self.nextPoint()

    #Return the next guess
    def getNextGuess(self):
        self.guessedPoints.append(self.points[0])
        #print("Original point: " + str(self.originalPoint) + " Next point: " +  str(self.points[0]) + " Directions: " + str(self.directions[0]))
        return self.points[0]
            
    #Return the next direction
    def getDirection(self):
        return self.directions[0]

    def getOriginalPoint(self):
        return self.originalPoint

    #replace the first element of the points list with the next point in that direction
    def nextPoint(self):
        self.points[0] = (self.points[0][0] + self.directions[0][0], self.points[0][1] + self.directions[0][1])
        if (self.checkValidPlacement(self.points[0]) == False):
            self.remove(0)
        else:
            self.history.append(self.points[0])

    def checkValidPlacement(self, point):
        x = point[0]
        y = point[1]

        #Hardcoded Values
        if (x < 0) or (x > 9):
            return False
        if (y < 0) or (y > 9):
            return False
        #if ((x,y) in self.pastMoves):
        #    return False
        else:
            return True

        



