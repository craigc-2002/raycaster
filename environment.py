"""
Environment
Craig Cochrane 2022

Creates an envrionment full of objects defined by a nested list passed in
"""
class Obstacle:
    """
    Class to represent each object in the environment
    """
    def __init__(self, pos, length, width):
        self.coord = (pos[0], pos[1]) # Position of top left corner
        self.length = length
        self.width = width
        self.height = width

        # Calculate the position of each corner of the object
        c1 = self.coord[0], self.coord[1]
        c2 = self.coord[0]+self.length, self.coord[1]
        c3 = self.coord[0]+self.length, self.coord[1]+self.width
        c4 = self.coord[0], self.coord[1]+self.width

        # List of object's corners, starting from top left moving clockwise
        self.corners = (c1, c2, c3, c4)


class Environment:
    """
    Class to hold the game environment
    """
    def __init__(self, map_array, grid, grid_dims):
        self.map_array = map_array
        self.grid = grid
        self.grid_dims = grid_dims
        
        self.obstacles = []
        self.process_array()

    def process_array(self):
        """
        Method to process the map_array and produce a list of obstacle objects
        """
        for row in range(len(self.map_array)):
            for i in range(len(self.map_array[row])):
                if self.map_array[row][i]:
                    pos = (self.grid_dims[0]*(i % self.grid[0]), self.grid_dims[1]*(row  % self.grid_dims[1]))
                    new_obs = Obstacle(pos, self.grid_dims[0], self.grid_dims[1])
                    self.obstacles.append(new_obs)

    def get_2d(self):
        """
        Method to return a list of the obstscles that need to be drawn for the 2d map
        """
        return self.obstacles
        
