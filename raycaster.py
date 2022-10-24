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
        
        self.done = False

    def display_init(self, screen, win_dims, clock):
        """
        Method to initialise the display method for the engine

        Parameters:
            - screen (pygame screen object)
            - win_dims (tuple) window width, window height
        """
        if self.display_initialised == False and self.environment_initialised == True and self.player_initialised == True:
            self.screen = screen
            self.display = display_pg.Display_pg(screen, self.env, self.player)
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
        if self.environment_initialised == False:
            self.env = environment.Environment(env_map, grid_details[0], grid_details[1])
            self.environment_initialised = True

    def player_init(self, init_pos):
        """
        Method to initialise the player in the environment

        Parameters:
            - init_pos (tuple) initial position of the player
        """
        if self.player_initialised == False and self.environment_initialised == True:
            self.player = player.Player(self.env, init_pos)
            self.player_initialised = True
            
    def game_loop(self):
        if self.display_initialised == True and self.environment_initialised == True and self.player_initialised == True:
            while self.done == False:
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

                # Display drawing loop
                self.screen.fill("white")

                rays = self.player.cast_rays(self.n_rays)
                self.display.draw_3d(rays, self.ray_width)

                #display.draw_2d_map()
                #display.draw_player()

                pygame.display.flip()  # Refresh on-screen display
                self.clock.tick(60)         # wait until next frame (run at 60 FPS)
        else:
            print("Initialise the engine fully before calling the loop")
