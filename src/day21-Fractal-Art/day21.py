"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import numpy as np

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day21-Fractal-Art/input.txt").read_text()

EXAMPLE_INPUT1 = """../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#"""
EXAMPLE_RESULT1 = 12

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result, number_of_turns):
    """Problem A solved function
    """
    start_state = """.#./..#/###"""
    current_array = create_array_from_string(start_state)
    #Build translation table, rotate 3 times and swap both left to right and up to buttom
    translation_table_dict = {}
    rows = string_worker(input_string)
    for row in rows:
        [left_part, right_part] = row.split(' => ')
        find_pattern_array = create_array_from_string(left_part)
        new_pattern_array = create_array_from_string(right_part)
        for _ in range(4):
            store_array_dict_in_str(translation_table_dict, find_pattern_array, new_pattern_array)
            find_pattern_array  = np.rot90(find_pattern_array)
        store_array_dict_in_str(translation_table_dict, np.flipud(find_pattern_array), new_pattern_array)
        store_array_dict_in_str(translation_table_dict, np.fliplr(find_pattern_array), new_pattern_array)

    solution = recursive_magic(number_of_turns, current_array, translation_table_dict)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def recursive_magic(number_of_turns_left, current_array, translation_table_dict):
    count = 0
    if number_of_turns_left > 0:
        length_of_current_array = len(current_array)
        if length_of_current_array % 2 == 0:
            number_of_2_length_squares = int(length_of_current_array / 2)
            if number_of_2_length_squares > 1:
                for row in range(number_of_2_length_squares):
                    for collumn in range(number_of_2_length_squares):
                        count += recursive_magic(number_of_turns_left, current_array[row*2:(row+1)*2, collumn*2:(collumn+1)*2], translation_table_dict)
        if length_of_current_array == 2 or length_of_current_array == 3:
            look_up_string = np.array_repr(current_array)
            if look_up_string in translation_table_dict:
                new_array = translation_table_dict[look_up_string]
                count += recursive_magic(number_of_turns_left-1, new_array, translation_table_dict)
            else:
                print('Unexpected error string not found in dict', look_up_string)
    else:
        for dim_1 in current_array:
            for char in dim_1:
                if char == '#':
                    count += 1
    return count

def store_array_dict_in_str(translation_table_dict, find_pattern_array, new_pattern_array):
    look_up_string = np.array_repr(find_pattern_array)
    translation_table_dict[look_up_string] = new_pattern_array

def create_array_from_string(left_part):
    return np.array([list(inner_part) for inner_part in left_part.split('/')])

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1, 2)
problem_a(PROGBLEM_INPUT_TXT, 0, 5)
print("\n")
