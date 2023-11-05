"""
    Class to represent the player

    Stores the player's position, direction and other properties
    """
import vector as v
import math
import ray


class Player:
    def __init__(self, env, init_pos):
        self.env = env
        self.position = v.vector(init_pos[0], init_pos[1])
        self.radius = 15

        self.direction = math.pi/2 # Direction with 0 being pointing towards the top of the screen (in radians)
        self.dir_vec = v.vector(math.sin(self.direction), math.cos(self.direction)) # Unit vector in direction the player is facing
        self.height_scale = 30000
        self.dof = 1
        # camera plane = dir_vec rotated by 90 degrees
        self.camera_plane = self.dir_vec.rotate(90) * self.dof

    def move_forward(self):
        """
        Method to move the player forward
        """
        next_pos = self.position + (self.dir_vec * 10)
        
        if not self.check_collision(next_pos, self.env.obstacles):
            self.position = next_pos

    def turn_clockwise(self):
        """
        Method to turn the player clockwise
        """
        self.direction -= (2*math.pi/180) * 5
        self.dir_vec = v.vector(math.sin(self.direction), math.cos(self.direction))
        self.camera_plane = self.dir_vec.rotate(90) * self.dof

    def turn_anticlockwise(self):
        """
        Method to turn the player clockwise
        """
        self.direction += (2*math.pi/180) * 5
        self.dir_vec = v.vector(math.sin(self.direction), math.cos(self.direction))
        self.camera_plane = self.dir_vec.rotate(90) * self.dof

    def zoom_in(self):
        self.dof -= (self.dof * 0.1)
        self.height_scale += (self.height_scale * 0.1)
        self.camera_plane = self.dir_vec.rotate(90) * self.dof

    def zoom_out(self):
        self.dof += (self.dof * 0.1)
        self.height_scale -= (self.height_scale * 0.1)
        self.camera_plane = self.dir_vec.rotate(90) * self.dof

    def check_collision(self, pos, obstacles):
        """
        Method to check if the object has collided with any obstacle in the environment
        Takes in a position and list of obstacles

        Parameters:
            - pos (vector) new position of the player to check for collision
            - obstacles (list of obstacle) list of obstacles present in the environment

        Returns:
            - collided (boolean) whether the ball's move will collide with an obstacle in the environment
        """
        collided = False

        # Check the x and y coordinates of the player and two opposite corners of each obstacle in the environment
        for obs in obstacles:
            if pos[0] < (max(obs.corners[0][0],obs.corners[2][0])+self.radius) and pos[0] > (min(obs.corners[0][0],obs.corners[2][0])-self.radius):
                if pos[1] < (max(obs.corners[0][1],obs.corners[2][1])+self.radius) and pos[1] > (min(obs.corners[0][1],obs.corners[2][1])-self.radius):
                    collided = True

        return collided

    def cast_rays(self, n):
        """
        Method to cast rays from the player within the fov, calculate the intersection with the environment obstacles and return this data
        Rays are cast from a plane perpendicular to the player's direction vector
        """
        view = []

        for i in range(n):
            # cast rays from camera plane
            camera_x = (2 * ((n - i) / n)) - 1
            ray_dir = self.dir_vec + (self.camera_plane * camera_x)

            new_ray = ray.Ray(self.env, self.position, ray_dir)
            strip_height = new_ray.march()

            view.append(strip_height)

        return view
