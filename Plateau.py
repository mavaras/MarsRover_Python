
""" 
This Class represents the rectangle where rovers are landed
atributes:
	-> Plateau size
	-> occupied array storing occupied coordinates (if any)

actions:
	-> starts rover's exploring process
	-> for each rover position, checks if this position is valid or not based on:
		- rover cant be outside of Plateau
		- two or more rovers cant be in the same position inside Plateau
		In case this new position isn't valid, current rover returns to it's initial position
		and stays there stopped. 
		That means that that rover occupie it's initial position inside Plateau
	

	Note: I've decided to include this last behaviour here, in Plateau class, because I conceive
	Plateau like an object that can have the power to control what happens inside him and to have 
	responsability about the Rovers he "contains", deciding when one of this is moving right or not.
	That's why i think Plateau can starts Rover's walk and have the power to send Rover to it's 
	start point if Rover did something wrong.
"""

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
					print(rover.get_position())
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

