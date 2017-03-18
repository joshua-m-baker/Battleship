import pygame
from MenuButton import MenuButton
import sys

class Menu(object):
    def __init__(self, screen):
        self.screen = screen
        self.menuButtons = []

        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()

        s = pygame.Surface((self.screenWidth, self.screenHeight))
        s.set_alpha(75)
        s.fill((255,255,255))
        self.screen.blit(s, (0,0))

        menuButton = MenuButton(pygame.Rect((0,0), (30, 30)), self.screen, lambda : self.closeMenu())
        self.menuButtons.append(menuButton)

        self.addQuitButton()

    def addQuitButton(self):
        buttonHeight = 50
        buttonWidth = 200
        buttonX = (self.screenWidth//2) - (buttonWidth // 2)
        buttonY = (self.screenHeight//2) - (buttonHeight //2)
        point = (buttonX, buttonY)
        quitButton = MenuButton(pygame.Rect(point, (200, 50)), self.screen, lambda : self.quit())
        self.menuButtons.append(quitButton)

    def drawButtons(self):
        for i in self.menuButtons:
            i.draw()
        pygame.display.flip()

    def closeMenu(self):
        pass

    def quit(self):
        pygame.quit()
        sys.exit()

    def main(self):
        while (True):
            self.drawButtons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                
                elif event.type == pygame.K_UP:
                    if pygame.K_ESCAPE:
                        self.performAction(self.menuButtons[0].getAction())
                    
                elif event.type == pygame.MOUSEBUTTONUP:
                    point = pygame.mouse.get_pos()

                    for i in self.menuButtons:
                        if i.checkClicked(point):
                            return i.getAction()

        
