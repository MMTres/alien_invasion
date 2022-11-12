import sys
import pygame
from settings import Settings
from createrain import Rain


class RainGrid:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain Grid")
        self.drops = pygame.sprite.Group()
        self._create_grid()
        self.number_rows=0
        self.number_drops_x =0

    def _create_grid(self):
        """Create the fleet of aliens"""
        # create a star and find the number of stars in a row
        # spacing between each star is equal to one star width
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)
        self.number_drops_x = available_space_x // (2 * rain_width)

        # Determine the number of rows of stars that fits on the screen
        available_space_y = (self.settings.screen_height)
        self.number_rows = available_space_y // (rain_height)

        # create the full fleet of stars
        for row_number in range(self.number_rows):
            for rain_number in range(self.number_drops_x):
                self._create_rain(rain_number, row_number)

    def _create_rain(self, rain_number, row_number):
        """Create a drop and place it in the row"""
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        rain.x = rain_width + 2 * rain_width * rain_number
        rain.rect.x = rain.x

        rain.rect.y = rain_height + 2 * rain.rect.height * row_number
        self.drops.add(rain)

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.drops.draw(self.screen)
        # make the most recently drawn screen visible
        pygame.display.flip()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self._rain_fall()
            self._update_screen()

    def _rain_fall(self):
        """drop the entire fleet and change the fleet's direction"""
        dropped = 0
        for drop in self.drops.sprites():
            drop.rect.y += self.settings.fleet_drop_speed
            if drop.rect.bottom > self.settings.screen_height:
                dropped += 1
                self.drops.remove(drop)
        if dropped != 0:
            self._new_row()


    def _new_row(self):
        rain = Rain(self)
        rain_width, rain_height = rain.rect.size
        available_space_x = self.settings.screen_width - (2 * rain_width)
        self.number_drops_x = available_space_x // (2 * rain_width)
        for x in range(self.number_drops_x):
            self._create_rain(x, -1)


if __name__ == '__main__':
    # make a game instance, and run the game
    sg = RainGrid()
    sg.run_game()
