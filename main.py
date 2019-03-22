""" Mars Rover problem
    py version: Python 2.7.15
"""

import sys
from Rover import Rover, coordinates
from Plateau import Plateau


# this functions are used to validate all three kinds of inputs (plateau size, rover pos and path)
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

def main():
    if len(sys.argv) != 2:
        print("Usage: ")
        print("    -> txt file input: main.py <.txt>")
        print("    -> console input: main.py -c")
        
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-c":
            # console input mode
            try:
                plateau_size = raw_input("Plateau upper right coordinate: ").split(" ")
                if not valid_input_plateau_size(plateau_size):
                    raise TypeError
            except TypeError:
                print("plateau_size input invalid format. e.g. 4 4")

            plateau = Plateau(int(plateau_size[0])+1, int(plateau_size[1])+1)
            
            while True:
                try:
                    rover_pos = raw_input("Rover initial position and direction: (q to finish)")
                    if rover_pos == "q":
                        break
                        
                    x, y, direction = rover_pos.split(" ")                  
                    if not valid_input_rover_position([x,y,direction]):
                        raise TypeError
                except:
                    print("rover_position input invalid format ("+str([x,y,direction])+") . e.g. 1 2 N")
                    continue

                try:
                    rover_path = raw_input("Rover path: ").strip()
                    if not valid_input_rover_path(rover_path):
                        raise TypeError
                except:
                    print("rover_path input invalid format ("+str(rover_path)+") . e.g. MMRLMR (only M R or L)")
                    continue

                rover = Rover(int(x), int(y), str(direction))
                plateau.walk_path(rover, rover_path)
                
                print(rover)

        else:
            # .txt file input mode

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

if __name__ == "__main__":
    main()
