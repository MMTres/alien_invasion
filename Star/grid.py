import sys
import pygame
from settings import Settings
from createstar import Star


class StarGrid:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Grid")
        self.star = pygame.sprite.Group()
        self._create_grid()

    def _create_grid(self):
        """Create the fleet of aliens"""
        # create a star and find the number of stars in a row
        # spacing between each star is equal to one star width
        star = Star(self)
        star_width, star_height = star.rect.size
        print(star_width, star_height)
        #star_width = star_width * 0.1
        #star_height = star_height * 0.1
        print(star_width, star_height)
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fits on the screen
        available_space_y = (self.settings.screen_height - (star_height))
        number_rows = available_space_y // (2 * star_height)

        # create the full fleet of stars
        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                self._create_star(star_number, row_number)

    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        from random import randint
        random_number1 = randint(-15, 15)
        star.x = star_width + 2 * star_width * star_number + random_number1
        star.rect.x = star.x
        random_number2 = randint(-15, 15)
        star.rect.y = star_height + 2 * star.rect.height * row_number + random_number2
        self.stars.add(star)

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)
        # make the most recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._update_screen()


if __name__ == '__main__':
    # make a game instance, and run the game
    sg = StarGrid()
    sg.run_game()
