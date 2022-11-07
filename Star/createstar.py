import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single alien in the fleet"""
    def __init__(self, ai_game):
        """initialize the game and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the star image and set its rect attribute

        self.image = pygame.image.load('star.bmp')
        self.rect = self.image.get_rect()

        #start each new star near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height





