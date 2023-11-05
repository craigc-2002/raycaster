"""
Raycaster
Craig Cochrane 2022

A simple raycasting program to demonstrate basic 3D graphics in python.
"""

# Import modules used
import pygame
import math
import random as r

# Import the rest of the engine code
import environment
import player
import display_pg
import vector as v


class Raycaster:
    def __init__(self):
        self.display_initialised = False
        self.environment_initialised = False
        self.player_initialised = False

        self.n_rays = 100

        self.env = None

        self.player = None

        self.screen = None
        self.display = None
        self.clock = None
        self.ray_width = None

        self.done = False

    def display_init(self, screen, win_dims, clock):
        """
        Method to initialise the display method for the engine

        Parameters:
            - screen (pygame screen object)
            - win_dims (tuple) window width, window height
        """
        if self.display_initialised is False and self.environment_initialised and self.player_initialised:
            self.screen = screen
            self.display = display_pg.DisplayPG(screen, self.env, self.player)
            self.clock = clock
            self.ray_width = win_dims[0] / self.n_rays

            self.display_initialised = True

    def environment_init(self, env_map, grid_details):
        """
        Method to initalise the environment from a map passed in

        Parameters:
            - env_map (list of lists) represents the map of the environment
            - grid_details (list of lists) represents the grid of the level (number of grid squares(x,y), length and width of grid squares(x,y))
        """
        if not self.environment_initialised:
            self.env = environment.Environment(env_map, grid_details[0], grid_details[1])
            self.environment_initialised = True

    def player_init(self, init_pos):
        """
        Method to initialise the player in the environment

        Parameters:
            - init_pos (tuple) initial position of the player
        """
        if not self.player_initialised and self.environment_initialised:
            self.player = player.Player(self.env, init_pos)
            self.player_initialised = True

    def game_loop(self):
        if self.display_initialised and self.environment_initialised and self.player_initialised:
            while not self.done:
                # Process player inputs.
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        raise SystemExit

                    # Get a list of keys currently being pressed
                    key_input = pygame.key.get_pressed()
                    # If the w key is being pressed
                    if key_input[pygame.K_w]:
                        self.player.move_forward()
                    # If the d key is being pressed
                    if key_input[pygame.K_d]:
                        self.player.turn_clockwise()
                    # If the a key is being pressed
                    if key_input[pygame.K_a]:
                        self.player.turn_anticlockwise()
                    # If the z key is being pressed
                    if key_input[pygame.K_z]:
                        self.player.zoom_in()
                    # If the x key is being pressed
                    if key_input[pygame.K_x]:
                        self.player.zoom_out()

                # Display drawing loop
                self.screen.fill("white")

                rays = self.player.cast_rays(self.n_rays)
                self.display.draw_3d(rays, self.ray_width, self.player.height_scale)

                self.display.draw_2d_map()
                self.display.draw_player()

                # Add current FPS to the screen
                font = pygame.font.SysFont("Arial", 36)
                fps_text = str(round(self.clock.get_fps()))
                fps_text_img = font.render(fps_text, True, (0, 0, 0))
                self.screen.blit(fps_text_img, (1220, 20))

                pygame.display.flip()  # Refresh on-screen display
                self.clock.tick(60)  # wait until next frame (run at 60 FPS)
        else:
            print("Initialise the engine fully before calling the loop")
