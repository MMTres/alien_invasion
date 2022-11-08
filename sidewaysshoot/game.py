import pygame
import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats


class SidewaysShoot:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stats = GameStats(self)
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()


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
        if event.key == pygame.K_UP:
            # move the ship to the right
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # move the ship to the left
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #update bullet positions
        self.bullets.update()
        #get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # make the most recently drawn screen visible
        pygame.display.flip()

    def _check_bullet_alien_collisions(self):
        """respond to bullet-alien collisions"""
        #check for any bullets that have hit aliens
        #if so get rid of the bullet and the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #destroy existing bullets and create new fleet

            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # make the most recently drawn screen visible
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens"""
        #create an alien and find the number of aliens in a row
        #spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        print(alien_width, alien_height)
        ship_height = self.ship.rect.height
        available_space_x = self.settings.screen_width - (2*alien_width) - ship_height
        available_space_y = self.settings.screen_height - 3*alien_height
        number_aliens_x = available_space_x // (2* alien_width)
        number_rows = available_space_y // (2*alien_height)

        #create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = self.settings.screen_width - (alien_width + 2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height +2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _ship_hit(self):
        """respond to the ship being hit by an alien"""
        #decrement ships left

        if self.stats.ships_left > 0:
            self.stats.ships_left -=1
            #get rid of any remaining bullets and aliens
            self.aliens.empty()
            self.bullets.empty()
            #create a new fleed and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #pause
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _update_aliens(self):
        """check if the fleet is at an edge then update the positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        #look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        #look for aliens hitting the left of the screen
        self._check_aliens_left()


    def _check_fleet_edges(self):
        """respond appropriately if any aliens have reached an edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_aliens_left(self):
        """check if any aliens have reached the left of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left >= screen_rect.left:
                self._ship_hit()
                break


if __name__ == '__main__':
    # make a game instance, and run the game
    ss = SidewaysShoot()
    ss.run_game()