"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day19-A-Series-Of-Tubes/input.txt").read_text()

EXAMPLE_INPUT1 = """     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ """
EXAMPLE_RESULT1 = 'ABCDEF'

class MazeWalker:
    """Maze walker class used in Advent of Code
        Input: string representing full map
    """
    def __init__(self, input_strings):
        rows = input_strings.split('\n')
        self._master_map_array = []
        for row in rows:
            this_level = []
            for char in row:
                this_level.append(char)
            self._master_map_array.append(this_level)
        self.set_start_position()
        self._direction = 'down'
        self.az_found = ''

    def set_start_position(self):
        """Sets the start position according to rules given
        """
        self._current_row = 0 #We start at top row
        for current_char in range(len(self._master_map_array[0])):
            if self._master_map_array[0][current_char] == '|':
                self._current_char = current_char

    def move_in_maze(self):
        """This is where we move around in the maze
        """
        if self._direction == 'down':
            self._current_row += 1
        elif self._direction == 'up':
            self._current_row -= 1
        elif self._direction == 'right':
            self._current_char += 1
        else: #left
            self._current_char -= 1
        next_char_is = self._master_map_array[self._current_row][self._current_char]
        if next_char_is in '-|':
            pass #just continue
        elif next_char_is == '+':
            if self._direction in 'up or down':
                if self._current_char > 0:
                    if self._master_map_array[self._current_row][self._current_char-1] in '-ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        self._direction = 'left'
                    else:
                        self._direction = 'right'
                else:
                    self._direction = 'right'
            else:
                if self._current_row > 0:
                    if self._master_map_array[self._current_row - 1][self._current_char] in '|ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        self._direction = 'up'
                    else:
                        self._direction = 'down'
                else:
                    self._direction = 'down'
        elif next_char_is == ' ':
            return False
        else:
            self.az_found += next_char_is #Alfanumeric found add to az string

        return True

def problem_a(input_string, expected_result, problem_b = False):
    """Problem A solved function
    """
    current_maze = MazeWalker(input_string)
    steps = 1
    while current_maze.move_in_maze():
        steps += 1

    if not problem_b:
        solution = current_maze.az_found
    else:
        solution = steps

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 'SXWAIBUZY')
print("\n")

problem_a(EXAMPLE_INPUT1, 38, True)
problem_a(PROGBLEM_INPUT_TXT, 16676, True)
