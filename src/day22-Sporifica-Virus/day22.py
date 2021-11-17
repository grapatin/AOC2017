"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
import math
from pathlib import Path


PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day22-Sporifica-Virus/input.txt").read_text()

EXAMPLE_INPUT1 = """..#
#..
..."""
EXAMPLE_RESULT1 = 41

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

class VirusClass:
    def __init__(self, input_string):
        input_rows = string_worker(input_string)
        self.direction = 'up'
        mid_row = math.floor(len(input_rows)/2)
        mid_column = math.floor(len(input_rows[0])/2)
        self.grid_dict = {}
        self.infected = 0
        self.current_pos_y = mid_row
        self.current_pos_x = mid_column
        y_cord = 0
        for row in input_rows:
            x_cord = 0
            for current_char in row:
                yx_str = self.yx_string(y_cord, x_cord)
                self.grid_dict[yx_str] = current_char
                x_cord += 1
            y_cord += 1

    def do_burst(self):
        current_pos_str = self.yx_string(self.current_pos_y, self.current_pos_x)
        if current_pos_str in self.grid_dict:
            current_char = self.grid_dict[current_pos_str]
        else:
            current_char = '.'
        if current_char == '.':
            self.turn_left()
            current_char = '#'
            self.infected += 1
        else:
            self.turn_right()
            current_char = '.'
        self.grid_dict[current_pos_str] = current_char
        self.move_forward()
        
    def turn_left(self):
        if self.direction == 'up':
            self.direction = 'left'
        elif self.direction == 'left':
            self.direction = 'down'
        elif self.direction == 'down':
            self.direction = 'right'
        elif self.direction == 'right':
            self.direction = 'up'
    def turn_right(self):
        if self.direction == 'up':
            self.direction = 'right'
        elif self.direction == 'left':
            self.direction = 'up'
        elif self.direction == 'down':
            self.direction = 'left'
        elif self.direction == 'right':
            self.direction = 'down'

    def move_forward(self):
        if self.direction == 'up':
            self.current_pos_y -= 1
        elif self.direction == 'left':
            self.current_pos_x -= 1
        elif self.direction == 'down':
            self.current_pos_y += 1
        elif self.direction == 'right':
            self.current_pos_x += 1

    def yx_string(self, y_pos, x_pos):
        return str(y_pos)+';'+str(x_pos)

class VirusEvolved(VirusClass):
    def do_burst(self):
        current_pos_str = self.yx_string(self.current_pos_y, self.current_pos_x)
        if current_pos_str in self.grid_dict:
            current_char = self.grid_dict[current_pos_str]
        else:
            current_char = '.'
        if current_char == '.':
            self.turn_left()
            current_char = 'W'
        elif current_char == 'W':
            current_char = '#'
            self.infected += 1
        elif current_char == '#':
            current_char = 'F'
            self.turn_right()
        elif current_char == 'F':
            current_char = '.'
            self.turn_right()
            self.turn_right()
        self.grid_dict[current_pos_str] = current_char
        self.move_forward()

def problem(input_string, expected_result, no_bursts, problem_b = False):
    """Problem A solved function
    """
    if not problem_b:
        virus = VirusClass(input_string)
    else:
        virus = VirusEvolved(input_string)

    for _ in range(no_bursts):
        virus.do_burst()
    solution = virus.infected

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem(EXAMPLE_INPUT1, EXAMPLE_RESULT1, 70)
problem(EXAMPLE_INPUT1, 5587, 10000)

problem(PROGBLEM_INPUT_TXT, 5404, 10000)
print("\n")

problem(EXAMPLE_INPUT1, 26, 100, True)
problem(EXAMPLE_INPUT1, 2511944, 10000000, True)

problem(PROGBLEM_INPUT_TXT, 2511672, 10000000, True)
