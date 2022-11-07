



    def _create_fleet(self):
        """Create the fleet of aliens"""
        # create a star and find the number of stars in a row
        # spacing between each star is equal to one star width
        star = star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.settings.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        # Determine the number of rows of stars that fits on the screen
        available_space_y = (self.settings.screen_height - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        # create the full fleet of stars
        for row_number in range(number_rows):
            for star_number in range(number_star_x):
                self._create_star(star_number, row_number)


    def _create_star(self, star_number, row_number):
        """Create a star and place it in the row"""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * alien_width * alien_number
        star.rect.x = star.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    