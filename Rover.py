""" 
This class represents a Rover and handles movement, initialization and reseting

atributes:
    -> x, y coordinates
    -> direction (N, W, E, S)
    -> it's start point and direction

actions:
    -> move forward
    -> rotate (given argument is -1 or 1, depending if rotation is left or right)
    -> return to start point (in case any error occurs while walking)
"""

coordinates = ["N", "E", "S", "W"]


class Rover:
    
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.start_pos = (x, y, direction)

    def move(self):
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "W":
            self.x -= 1
        else:
            self.y -= 1

    def rotate(self, direction):
        self.direction = coordinates[(coordinates.index(self.direction)+direction)%4]

    def get_position(self):
        return [self.x, self.y]

    def back_to_start(self):
        self.x, self.y, self.direction = self.start_pos
    
    def __str__(self):
        return "%d %d %s"%(self.x, self.y, self.direction)
