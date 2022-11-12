import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ss):
        """initialize the game and set its starting position"""
        super().__init__()
        self.screen = ss.screen
        self.settings = ss.settings

        #load the alien image and set its rect attribute

        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def check_edges(self):
        """Return true if alien is at edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True
