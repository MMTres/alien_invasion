import pygame

class Ship:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.bottomleft = self.screen_rect.bottomleft

        #store a decimal value for the ship's horizontal position
        self.y = float(self.rect.y)

        #movement flags
        self.moving_up = False
        self.moving_down = False


    def update(self):
        """Update the ships position based on the movement flags"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        #update rect object from self.x
        self.rect.y = self.y

    def center_ship(self):
        """center the ship on the screen"""
        self.rect.left = self.screen_rect.left
        self.x = float(self.rect.x)


    def blitme(self):
        """Draw the ship at its current location"""

        self.screen.blit(self.image, self.rect)