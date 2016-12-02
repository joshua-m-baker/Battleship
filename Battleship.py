'''Battleship 11/12/16

0,0    1,0    2,0    3,0

0,1    1,1    2,1    3,1

0,2    1,2    2,2    3,2

0,3    1,3    2,3    3,3

What's the best way to check all the object attributes and see if one is false?
Can you check all elements of a for loop without making a list?
getGuess in player
Debugging

Immediate to do list:
    [x]finish ship placement
        Replace making a list of possible directions with choosing a random direction and seeing if it works 
    [x]improve input function
    []look at grid system
'''
import random

class GameLoop(object):
    def __init__(self):
        computer = ComputerPlayer()
        human = HumanPlayer()
        shipInfo = computer.shipPlacement(3)
        computer.gameBoard.placeShip(shipInfo[0], shipInfo[1], shipInfo[2])

        while (computer.gameBoard.checkWin() == False):
            computer.gameBoard.display()
            guess = human.getGuess()
            computer.gameBoard.guessPoint(guess)
            if computer.gameBoard.checkWin() == True:
                break

class Player(object):
    def __init__(self):
        self.gameBoard = Gameboard()
        '''while True:
            self.turn()
        
    def turn(self):
        self.gameBoard.display()
        self.guess = self.getGuess()
        self.gameBoard.guessPoint(self.guess)
        self.gameBoard.checkWin()'''

    def getGuess(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        Player.__init__(self)

    def getInput(self):
        xAnswers = ["1", "2", "3", "4", "5"]
        yAnswers = ["A", "B", "C", "D", "E", "a", "b", "c", "d", "e"]
        yDict = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4}
        while True:
            x = input("Select a column (1 - 5): ")
            if x in xAnswers:
                x = int(x) - 1
                if 0 <= x <= (len(self.gameBoard.gameGrid[0])):
                    break
            else:
                print("Please choose a number between 1 and 5")

        while True:
            y = (input("Select a row (A - E): "))
            if y in yAnswers:
                y = y.upper()
                y = yDict[y]
                if 0 <= y <= (len(self.gameBoard.gameGrid[0])):
                    
                    return [x, y]
         

    #Take an x and y from the getInput function and make sure that spot hasn't been guessed
    def getGuess(self):
        while True:
            self.guess = self.getInput()
            print(self.guess)
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
            direction = random.choice(directionList)
            resultsList = [self.checkValidPlacement([point[0] + i * direction[0], point[1] + i * direction[1]]) for i in range(length)]
            if all(resultsList) == True:
                return direction
            else:
                directionList.remove(direction)

class Gameboard(object):
    def __init__(self):
        self.gameGrid = [[0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0]]
        self.shipList = []
        self.sunkenShips = []

    
    def placeShip(self, length, point, direction):
        self.ship = Ship(length, point, direction)
        self.shipList.append(self.ship)
        
    #length, point, direction
    '''def placeShip(self):
        self.destroyer = Ship(3, [0, 0], [0, 1])
        self.shipList.append(self.destroyer)'''


    #go through the list of ships and check each on to see if it's hit (is there a better way to do this?)
    def guessPoint(self, point):
        self.x = point[0]
        self.y = point[1]
        for self.ship in self.shipList:
            if (self.ship.checkHit(point) == True):
                self.gameGrid[self.y][self.x] = 2
                print("HIT")
                #print (self.ship.hitList)
                if (self.ship.checkSunk() == True):
                    print("SUNK")
                    self.sunkenShips.append(self.ship)
                return

        self.gameGrid[self.y][self.x] = 1

    def checkWin(self):
        if len(self.sunkenShips) == len(self.shipList):
            print("YOU WIN")
            return True
        else:
            return False
        



    def display(self):
        print('''
      1       2       3       4       5 

A |   {}   |   {}   |   {}   |   {}   |   {}   |


B |   {}   |   {}   |   {}   |   {}   |   {}   |


C |   {}   |   {}   |   {}   |   {}   |   {}   |


D |   {}   |   {}   |   {}   |   {}   |   {}   |
    
    
E |   {}   |   {}   |   {}   |   {}   |   {}   |

      

'''.format(self.gameGrid[0][0], self.gameGrid[0][1], self.gameGrid[0][2], self.gameGrid[0][3], self.gameGrid[0][4],
           self.gameGrid[1][0], self.gameGrid[1][1], self.gameGrid[1][2], self.gameGrid[1][3], self.gameGrid[1][4],
           self.gameGrid[2][0], self.gameGrid[2][1], self.gameGrid[2][2], self.gameGrid[2][3], self.gameGrid[2][4],
           self.gameGrid[3][0], self.gameGrid[3][1], self.gameGrid[3][2], self.gameGrid[3][3], self.gameGrid[3][4],
           self.gameGrid[4][0], self.gameGrid[4][1], self.gameGrid[4][2], self.gameGrid[4][3], self.gameGrid[4][4],
           ))

class Ship(object):

    def __init__(self, length, point, direction):
        '''direction vector [0,1] is up, [0,-1] is down, [1,0] is right, [-1, 0] is left
        point = [x,y]
        Create a list of the coordinates of the ship. Start with the first point, and then add the direction vector
        until you get to the length of the ship'''
        self.coordinates = [[point[0] + i * direction[0], point[1]+ i*direction[1]] for i in range(length)]
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

g = GameLoop()




