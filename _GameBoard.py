from Ship import Ship

class GameBoard(object):
    def __init__(self):
        length = 10
        width = 10
        self.gameGrid = self.makeGameGrid(length, width)
        self.shipList = []
        self.sunkenShips = []

    def makeGameGrid(self, length, width):

        fullList = [[0 for j in range(width)] for i in range(length)]
        
        return fullList

    
    def placeShip(self, shipInfo):
        length = shipInfo[0]
        point = shipInfo[1]
        direction = shipInfo[2]
        self.ship = Ship(length, point, direction)
        self.shipList.append(self.ship)
        
    #length, point, direction
    '''def placeShip(self):
        self.destroyer = Ship(3, [0, 0], [0, 1])
        self.shipList.append(self.destroyer)'''


    def checkPoint(self, point):
        self.x = point[0]
        self.y = point[1]
        for self.ship in self.shipList:
            if (self.ship.checkHit(point) == True):
                self.gameGrid[self.y][self.x] = 2
                print("HIT")
                if (self.ship.checkSunk() == True):
                    print("SUNK")
                    self.sunkenShips.append(self.ship)
                return True

        #print(self.x, self.y)
        self.gameGrid[self.y][self.x] = 1
        return False
        

    def checkWin(self):
        if len(self.sunkenShips) == len(self.shipList):
            print("YOU WIN")
            return True
        else:
            return False

    def display(self):
        print('''
      1       2       3       4       5       6       7       8       9       10 

A |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


B |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


C |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


D |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |
    
    
E |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


F |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


G |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


H |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


I |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


J |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |   {}   |


      

'''.format(self.gameGrid[0][0], self.gameGrid[0][1], self.gameGrid[0][2], self.gameGrid[0][3], self.gameGrid[0][4], self.gameGrid[0][5], self.gameGrid[0][6], self.gameGrid[0][7], self.gameGrid[0][8], self.gameGrid[0][9], 
           self.gameGrid[1][0], self.gameGrid[1][1], self.gameGrid[1][2], self.gameGrid[1][3], self.gameGrid[1][4], self.gameGrid[1][5], self.gameGrid[1][6], self.gameGrid[1][7], self.gameGrid[1][8], self.gameGrid[1][9], 
           self.gameGrid[2][0], self.gameGrid[2][1], self.gameGrid[2][2], self.gameGrid[2][3], self.gameGrid[2][4], self.gameGrid[2][5], self.gameGrid[2][6], self.gameGrid[2][7], self.gameGrid[2][8], self.gameGrid[2][9], 
           self.gameGrid[3][0], self.gameGrid[3][1], self.gameGrid[3][2], self.gameGrid[3][3], self.gameGrid[3][4], self.gameGrid[3][5], self.gameGrid[3][6], self.gameGrid[3][7], self.gameGrid[3][8], self.gameGrid[3][9], 
           self.gameGrid[4][0], self.gameGrid[4][1], self.gameGrid[4][2], self.gameGrid[4][3], self.gameGrid[4][4], self.gameGrid[4][5], self.gameGrid[4][6], self.gameGrid[4][7], self.gameGrid[4][8], self.gameGrid[4][9], 
           self.gameGrid[5][0], self.gameGrid[5][1], self.gameGrid[5][2], self.gameGrid[5][3], self.gameGrid[5][4], self.gameGrid[5][5], self.gameGrid[5][6], self.gameGrid[5][7], self.gameGrid[5][8], self.gameGrid[5][9], 
           self.gameGrid[6][0], self.gameGrid[6][1], self.gameGrid[6][2], self.gameGrid[6][3], self.gameGrid[6][4], self.gameGrid[6][5], self.gameGrid[6][6], self.gameGrid[6][7], self.gameGrid[6][8], self.gameGrid[6][9], 
           self.gameGrid[7][0], self.gameGrid[7][1], self.gameGrid[7][2], self.gameGrid[7][3], self.gameGrid[7][4], self.gameGrid[7][5], self.gameGrid[7][6], self.gameGrid[7][7], self.gameGrid[7][8], self.gameGrid[7][9], 
           self.gameGrid[8][0], self.gameGrid[8][1], self.gameGrid[8][2], self.gameGrid[8][3], self.gameGrid[8][4], self.gameGrid[8][5], self.gameGrid[8][6], self.gameGrid[8][7], self.gameGrid[8][8], self.gameGrid[8][9], 
           self.gameGrid[9][0], self.gameGrid[9][1], self.gameGrid[9][2], self.gameGrid[9][3], self.gameGrid[9][4], self.gameGrid[9][5], self.gameGrid[9][6], self.gameGrid[9][7], self.gameGrid[9][8], self.gameGrid[9][9]
           ))


