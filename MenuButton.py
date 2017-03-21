from AbstractButton import AbstractButton
import pygame

class MenuButton(AbstractButton):
    def __init__(self, rect, screen, action, text = ""):
        super().__init__(rect, screen)
        self.text = text
        self.action = action

        pygame.font.init()
        self.font = pygame.font.Font(None, 30)
        self.textRender = self.font.render(text, True, (0,0,0))

        textSize = self.font.size(text)

        textWidth = textSize[0]
        textHeight = textSize[1]

        rectX = rect.left
        rectY = rect.top
        rectWidth = rect.width
        rectHeight = rect.height

        textX = rectX + rectWidth//2 - textWidth//2
        textY = rectY + rectHeight//2 - textHeight//2

        self.textRect = pygame.Rect((textX, textY), (textWidth, textHeight))

    def getAction(self):
        return self.action

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.textRender, self.textRect)



    