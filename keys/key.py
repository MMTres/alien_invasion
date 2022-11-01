import pygame
import sys



class Key:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((500,500))


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()

    def _check_events(self):
        """respond to keypresses and print the event key"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                print(event.key)



if __name__ == '__main__':
    # make a game instance, and run the game
    k = Key()
    k.run_game()