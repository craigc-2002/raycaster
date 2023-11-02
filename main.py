"""
main.py is a test implementation of the raycaster with a very simple environment map to demonstrate the raycasting
"""

# Import modules used
import pygame

import raycaster

pygame.init()

window_width = 1280
window_height = 720

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
screen.fill("white")  # Fill the display with a solid color

_ = False
env_map = [[1, 1, 1, 1, 1],
           [1, _, _, _, 1],
           [1, 1, 1, _, 1],
           [1, _, _, _, 1],
           [1, 1, 1, 1, 1]]

grid_details = ((5, 5), (100, 100))

engine = raycaster.Raycaster()
engine.environment_init(env_map, grid_details)
engine.player_init((150, 150))
engine.display_init(screen, (window_width, window_height), clock)

engine.game_loop()
