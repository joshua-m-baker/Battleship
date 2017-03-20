from AbstractButton import AbstractButton

class GameTile(AbstractButton):
    def __init__(self, rect, screen, x, y):
        super().__init__(rect, screen)

        self.unclickedColor = self.blue
        self.missColor = self.white
        self.hitColor = self.red
        self.showShipColor = self.green

        self.gridX = x
        self.gridY = y

        #self.action = lambda : self.getPoint()

    def getPoint(self):
        return (self.gridX,self.gridY)

    def tileDraw(self, status):
        if status == 0:
            self.setColor(self.unclickedColor)
        elif status == 1:
            self.setColor(self.missColor)
        elif status == 2 or status == 3:
            self.setColor(self.hitColor)
        elif status == 4:
            self.setColor(self.showShipColor)

        self.draw()


