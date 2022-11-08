import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """A class to represent a single drop"""
    def __init__(self, sg):
        """initialize the game and set its starting position"""
        super().__init__()
        self.screen = sg.screen
        self.settings = sg.settings

        #load the rain image and set its rect attribute

        self.image = pygame.image.load('raindrop.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()

        #start each new drop near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the rain's exact horizontal position
        self.x = float(self.rect.x)








