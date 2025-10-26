import pygame
"""
Main module for the Asteroids game.

This module initializes the Pygame window and runs the main game loop.
The game currently only displays a black window that can be closed.

Functions:
    main(): Initializes pygame and runs the main game loop.

Constants (imported from constants.py):
    SCREEN_WIDTH: Width of the game window
    SCREEN_HEIGHT: Height of the game window
"""
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
if __name__ == "__main__":
    main()