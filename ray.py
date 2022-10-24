"""
Ray
Craig Cochrane 2022

Class to represent a ray used in raycasting
"""

class Ray:
    def __init__(self, env, start_pos, direction):
        self.env = env
        self.start_pos = start_pos
        self.dir_vec = direction
        self.position = start_pos

    def check_collision(self, pos, obstacles):
        """
        Method to check if the ray has collided with any obstacle in the environment
        Takes in a position and list of obstacles

        Parameters:
            - pos (vector) position of the ray to check for collision
            - obstacles (list of obstacle) list of obstacles present in the environment

        Returns:
            - collided (boolean) whether the ray has collided with an obstacle in the environment
        """
        collided = False

        # Check the x and y coordinates of the player and two opposite corners of each obstacle in the environment
        for obs in obstacles:
            if pos[0] < max(obs.corners[0][0],obs.corners[2][0]) and pos[0] > min(obs.corners[0][0],obs.corners[2][0]):
                if pos[1] < max(obs.corners[0][1],obs.corners[2][1]) and pos[1] > min(obs.corners[0][1],obs.corners[2][1]):
                    collided = True

        return collided

    def march(self):
        """
        Method to march the ray forward until it encounters an obstacle in the environment
        """
        moving = True
        
        while moving == True:
            if self.check_collision(self.position, self.env.obstacles):
                moving = False
            else:
                self.position += self.dir_vec * 5

        ray_path = self.start_pos - self.position
        distance = ray_path.mag
        height = 1/distance
                
        return height


