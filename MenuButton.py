from AbstractButton import AbstractButton

class MenuButton(AbstractButton):
    def __init__(self, rect, screen, action):
        super().__init__(rect, screen)

        self.action = action

    def getAction(self):
        return self.action

    