""" Mars Rover problem
	py version: Python 2.7.15

	this is where I started coding just to solve the problem and see that all works fine
	just for test purposes
"""

import sys


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

class Plateau:	
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.occupied = []

	def walk_path(self, rover, path):
		""" this function starts given rover movement based on given path.
			If there's any mistake into path (wrong move | non existing next coordinate)
			or there's some collissions with other rovers (if any previous one/s)
			function ends and stops rover in his last coordinate
		"""
		
		for move in path:
			try:
				if move == "M":
					rover.move()
				elif move == "R":
					rover.rotate(1)
				else:
					rover.rotate(-1)

				# checking if rover goes to an existing and valid coordinate
				if not self.valid_position(rover.get_position()):
					raise Exception
				
			except Exception:
				print("Invalid Path: this paths leads rover to an inexisting or occupied point "+str(rover.get_position()))
				rover.back_to_start()
				print("rover retured to it's initial position "+str(rover.get_position()))
				break

		self.occupied.append(rover.get_position())  # rover now is stopped

	def valid_position(self, pos):
		""" returns True if given position is valid or False if not, based
			in Plateau size and other existing rovers's (if any) positions
		"""
		return pos[0] in range(self.width) and\
			   pos[1] in range(self.height) and\
			   pos not in self.occupied


# those functions are used to validate all three kinds of inputs (plateau size, rover pos and path)
def valid_input_plateau_size(line):
	return len(line) == 2 and\
		   line[0].isdigit() and line[1].isdigit()
		   
def valid_input_rover_position(line):
	return len(line) == 3 and\
		   line[0].isdigit() and line[1].isdigit() and\
		   line[2] in coordinates

def valid_input_rover_path(line):
	return all(isinstance(e, str) and\
		   not str(e).isdigit() and\
		   e in ["L","R","M"] for e in line)


if __name__ == "__main__":
	coordinates = ["N", "E", "S", "W"]

	if len(sys.argv) != 2:
		print("You can use this .py two ways: ")
		print(".txt file input: .py <.txt>")
		print("console input: .py -c")
		
	elif len(sys.argv) == 2:
		if sys.argv[1] == "-c":
			# console input mode
			pass
		else:
			# .txt file mode

			f = open(sys.argv[1])

			content = f.read().split("\n")
			try:
				plateau_size = content[0].split(" ")
				if not valid_input_plateau_size(plateau_size):
					raise TypeError
			except TypeError:
				print("plateau_size input invalid format. e.g. 4 4")

			plateau = Plateau(int(plateau_size[0])+1, int(plateau_size[1])+1)

			for c in range(1, len(content), 2):
				try:
					x, y, direction = content[c].split(" ")
					if not valid_input_rover_position([x,y,direction]):
						raise TypeError
				except:
					print("rover_position input invalid format ("+str([x,y,direction])+") . e.g. 1 2 N")
					continue

				try:
					rover_path = content[c+1].strip()
					if not valid_input_rover_path(rover_path):
						raise TypeError
				except:
					print("rover_path input invalid format ("+str(rover_path)+") . e.g. MMRLMR (only M R or L)")
					continue

				rover = Rover(int(x), int(y), str(direction))
				plateau.walk_path(rover, rover_path)
				
				print(rover)
