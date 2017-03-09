class Ship(object):

    def __init__(self, length, point, direction):
        '''direction vector [0,1] is up, [0,-1] is down, [1,0] is right, [-1, 0] is left
        point = [x,y]
        Create a list of the coordinates of the ship. Start with the first point, and then add the direction vector
        until you get to the length of the ship'''
        self.coordinates = [[point[0] + i * direction[0], point[1]+ i * direction[1]] for i in range(length)]
        
        self.length = length
        self.hitList = []
        
    def checkHit(self, point):
        if point in self.coordinates:
            return True
        else:
            return False

    def setHit(self, point):
        self.hitList.append(point)

    def checkSunk(self):
        #if all the coordinates are on the hitList, that ship is sunk
        if len(self.coordinates) == len(self.hitList):
            return True
        else:
            return False

