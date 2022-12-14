import pygame
import sys
from rocket import Rocket


class Window:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.rocket = Rocket(self)


    def _check_events(self):
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to keypresses"""
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the ship to the left
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            # move the ship up
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            # move the ship down
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()


    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def draw(self):
        while True:
            self._check_events()
            self.screen.fill((230, 230, 230))
            self.rocket.update()
            self.rocket.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    w = Window()
    w.draw()