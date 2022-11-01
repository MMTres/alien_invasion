import pygame

class Rocket:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('../character/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the center of the screen
        self.rect.center = self.screen_rect.center

        #store a decimal value for the rockets's horizontal position
        self.x = float(self.rect.x)

        #store a decimal value for the rocket's vertical position
        self.y = float(self.rect.y)

        #movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ships position based on the movement flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > 0:
            self.x -= 1
        #update rect object from self.x
        self.rect.x = self.x
        if self.moving_up and self.rect.top > 0:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1
        #update rect object from self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)