# raycaster
A very basic raycaster written in python

Modules:
-raycaster:
  the main raycaster class. Pulls the other modules together to one class that can be used in another program
-environment:
  represents the player's 3d environment. Stores a list of obstacles
-player:
  represents the player. Stores the location and direction and has methods to handle movement and rotation
 -ray:
  class for rays cast from the player. Has a method to move until it reaches an obstacle then returns the distance travelled
-display_pg:
  handles display of the environment, both from a 2d top down POV and a 3d representation from the player's POV
-main:
  a test implementaion of the raycaster with a simple envrionment
-vector:
  a vector class to represent vectors and perform vector maths on them
