"""
Class to represent the 2d map display

This is a seperate class from the environment itself so that the program's mechanics are independent of the program used for display
"""
"""
nice colours:
(252, 232, 97) yellow
(7, 146, 255) blue
"""
import pygame
import math
import random as r


class DisplayPG:

    def __init__(self, screen, env, player):
        self.screen = screen
        self.env = env
        self.player = player
        self.colour = (r.randint(0, 255), r.randint(0, 255), r.randint(0, 255))
        # print(self.colour)

    def draw_3d(self, view, ray_width, height_scale):
        """
        Method to draw the 3d scene using rays cast from the player object.

        Parameters:
            - view (list of objects to be drawn to the screen) the scene is displayed as a series of very thin rectangles of height given by the raycasting algorithm
            - ray_length (integer) number of pixels wide each ray is
        """
        for i in range(len(view)):
            x_coord = 1280 - (i * ray_width)
            y_coord = 360 - (height_scale*view[i]/2)
            
            new_wall = pygame.Rect(x_coord, y_coord, ray_width, height_scale*view[i])
            pygame.draw.rect(self.screen, self.colour, new_wall)

    def draw_2d_map(self):
        """
        Method to draw the 2d map of the level
        """
        walls = self.env.get_2d()
        for i in walls:
            self.draw_wall(i)

    def draw_wall(self, wall):
        """
        Method to draw each wall as a square on the screen
        """
        # Create the wall as a Rect object and display to the screen
        new_wall = pygame.Rect(wall.coord[0]*0.1, wall.coord[1]*0.1, wall.length*0.1, wall.width*0.1)
        pygame.draw.rect(self.screen, self.colour, new_wall)

    def draw_player(self):
        """
        Method to draw the player on a 2d map
        """
        # self.draw_fov()
        # Draw  line representing player's direction
        pos = pygame.math.Vector2(self.player.position[0],self.player.position[1])
        dir_vec = pygame.math.Vector2(self.player.dir_vec[0], self.player.dir_vec[1])
        pygame.draw.line(self.screen, (255, 255, 0), pos*0.1, (pos*0.1)+(dir_vec*7), 4)
        # Draw circle to represent player
        pygame.draw.circle(self.screen, (255, 0, 0), pos*0.1, self.player.radius*0.1)

    """
    def draw_fov(self):
        
        #Method to draw the limits of the player's field of view
        
        for i in range(0,3):
            d_theta = (self.fov/2) - (i*self.fov/2)
            dest_vector = self.position + v.vector(math.sin(self.direction+d_theta), math.cos(self.direction+d_theta))*70
            pygame.draw.line(self.screen, (0, 0, 255), self.position, dest_vector, 4)

    def draw_full_fov(self):
        
        #Method to draw the player's field of view as a solid arc
        
        for i in range(75):
            d_theta = (self.fov/2) - (i*self.fov/75)
            dest_vector = self.position + v.vector(math.sin(self.direction+d_theta), math.cos(self.direction+d_theta))*70
            pygame.draw.line(self.screen, (0, 0, 255), self.position, dest_vector, 5)"""
