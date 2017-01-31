'''Battleship 11/12/16

0,0    1,0    2,0    3,0

0,1    1,1    2,1    3,1

0,2    1,2    2,2    3,2

0,3    1,3    2,3    3,3

What's the best way to check all the object attributes and see if one is false?
Can you check all elements of a for loop without making a list?
getGuess in player
Debugging
'''
import random

class GameLoop(object):
    def __init__(self):
        computer = ComputerPlayer()
        human = HumanPlayer()
        shipLengths = [2, 3, 3, 4, 5]
        numberOfShips = len(shipLengths)
        for i in range(numberOfShips):
            computer.gameBoard.placeShip(computer.shipPlacement(shipLengths[i]))

        while (computer.gameBoard.checkWin() == False):
            computer.gameBoard.display()
            for ship in computer.gameBoard.shipList:
                print(ship.coordinates)
            #guess = human.getGuess()
            for i in range (10):
                for j in range(10):
                    point = [i, j]
                    computer.gameBoard.checkPoint(point)
            computer.gameBoard.display()
            #computer.gameBoard.checkPoint(guess)
            

class Player(object):
    def __init__(self):
        self.gameBoard = Gameboard()
        '''while True:
            self.turn()
        
    def turn(self):
        self.gameBoard.display()
        self.guess = self.getGuess()
        self.gameBoard.checkPoint(self.guess)
        self.gameBoard.checkWin()'''

    def getGuess(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def getInput(self):
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
                return [x, y]

class ComputerPlayer(Player):
    def __init__(self):
        Player.__init__(self)

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

class Gameboard(object):
    def __init__(self):
        length = 10
        width = 10
        self.gameGrid = self.makeGameGrid(length, width)
        self.shipList = []
        self.sunkenShips = []

    def makeGameGrid(self, length, width):

        '''x = []
        fullList = []
        for i in range(width):
            x.append(0)
        for j in range(length):
            fullList.append(x)'''

        fullList = [[0 for j in range(length)] for i in range(width)]
        
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


    def checkPoint(self, point): # maybe rename?
        self.x = point[0]
        self.y = point[1]
        for self.ship in self.shipList:
            if (self.ship.checkHit(point) == True):
                self.gameGrid[self.y][self.x] = 2
                print("HIT")
                if (self.ship.checkSunk() == True):
                    print("SUNK")
                    self.sunkenShips.append(self.ship)
                return

        print(self.x, self.y)
        self.gameGrid[self.y][self.x] = 1
        

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


class Ship(object):

    def __init__(self, length, point, direction):
        '''direction vector [0,1] is up, [0,-1] is down, [1,0] is right, [-1, 0] is left
        point = [x,y]
        Create a list of the coordinates of the ship. Start with the first point, and then add the direction vector
        until you get to the length of the ship'''
        self.coordinates = [[point[0] + i * direction[0], point[1]+ i*direction[1]] for i in range(length)]
        print(length)
        self.length = length
        self.hitList = []
        
    def checkHit(self, point):
        if point in self.coordinates:
            self.hitList.append(point)
            return True
        else:
            return False

    def checkSunk(self):
        #if all the coordinates are on the hitList, that ship is sunk
        
        if len(self.coordinates) == len(self.hitList):
            return True
        else:
            return False

def main():

    g = GameLoop()

if __name__ == "__main__":
    main()




