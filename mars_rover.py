import sys


class Rover:
	""" This class represents a Rover
		atributes:
			-> x, y coordinates
			-> direction (N, W, E, S)

		actions:
			-> move forward
			-> rotate
			-> start path
	"""
	
	def __init__(self, x, y, direction):
		self.x = x
		self.y = y
		self.direction = direction

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
			
	def walk_path(self, path):
		for move in path:
			if move == "M":
				self.move()
				
			elif move == "R":
				self.rotate(1)
				
			else:
				self.rotate(-1)

	def __str__(self):
		return "%d %d %s"%(self.x, self.y, self.direction)

class Plateau:
	""" This class represents the rectangle
		just storing width and height
		just created for future posible addons
	"""
	def __init__(self, width, height):
		self.width = width
		self.height = height

if __name__ == "__main__":
	coordinates = ["N", "E", "S", "W"]
	
	if len(sys.argv) == 2:
		# .txt file mode
		
		f = open(sys.argv[1])

		content = f.read().split("\n")
		square_size = content[0].split(" ")
		plateau = Plateau(int(square_size[0])+1, int(square_size[1])+1)
		#square = [["X" for j in range(int(square_size[0])+1)] for c in range(int(square_size[1])+1)]

		for c in range(1, len(content), 2):
			x, y, direction = content[c].replace("\n","").split(" ")
			rover_path = content[c+1].strip()

			rover = Rover(int(x), int(y), str(direction))
			rover.walk_path(rover_path)
			print(rover)

	else:
		# console input mode
		pass
