from ComputerPlayer import ComputerPlayer

shipLengths = [2, 3, 3, 4, 5]

def check(point, index):
    if point in coordList[index + 1]:
        return False

for i in range(50):
    coordList = []
    c = ComputerPlayer()
    length = 0
    for i in range(5):
    
        c.gameBoard.placeShip(c.shipPlacement(shipLengths[i]))

    for ship in c.gameBoard.shipList:
        for j in ship.coordinates:
            coordList.append(j)
            length+=1

    for i in range(len(coordList) - 1):
        if (check(coordList[i], i)):
            print("FAIL")
            break
    
    print("pass", length)
    

    
