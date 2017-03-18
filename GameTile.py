from AbstractButton import AbstractButton

class GameTile(AbstractButton):
    def __init__(self, rect, screen, x, y):
        super().__init__(rect, screen)

        self.unclickedColor = self.blue
        self.missColor = self.white
        self.hitColor = self.red

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
        elif status == 2 or 3:
            self.setColor(self.hitColor)

        self.draw()


