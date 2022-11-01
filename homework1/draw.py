
import pygame
from ship import Ship
import sys


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))
        self.ship = Ship(self)

    def draw(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((230, 230, 230))
            self.ship.blitme()
            pygame.display.flip()


if __name__ == '__main__':
    w = Window()
    w.draw()