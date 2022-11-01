# code
import pygame
import sys


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 200))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill((0, 0, 150))
            pygame.display.flip()


if __name__ == '__main__':
    w = Window()
    w.run()