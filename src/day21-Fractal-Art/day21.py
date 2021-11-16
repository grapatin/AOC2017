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

EXAMPLE_INPUT1 = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day21-Fractal-Art/input_ex.txt").read_text()
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
    #Build translation table, rotate 3 times and swap both left-right and up-down
    trnsltn_table_dict = {}
    rows = string_worker(input_string)
    for row in rows:
        [left_part, right_part] = row.split(' => ')
        find_pattern_ar = create_array_from_string(left_part)
        new_pattern_array = create_array_from_string(right_part)
        for _ in range(8):
            store_ar_dict_in_str(trnsltn_table_dict, find_pattern_ar, new_pattern_array)
            store_ar_dict_in_str(trnsltn_table_dict, np.flipud(find_pattern_ar), new_pattern_array)
            store_ar_dict_in_str(trnsltn_table_dict, np.fliplr(find_pattern_ar), new_pattern_array)
            find_pattern_ar  = np.rot90(find_pattern_ar)

    solution = fractal_away(number_of_turns, current_array, trnsltn_table_dict)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def fractal_away(number_of_turns_left, current_array, translation_table_dict):
    if number_of_turns_left > 0:
        length_of_current_array = len(current_array)
        if length_of_current_array % 2 == 0:
            factor = 2
        else:
            factor = 3

        number_sub_arrays = int(length_of_current_array / factor)
        new_shiny_array = np.empty(((factor+1)*number_sub_arrays,(factor+1)*number_sub_arrays), dtype='str')
        for row in range(number_sub_arrays):
            for column in range(number_sub_arrays):
                temp_array = current_array[row*factor:(row+1)*factor,\
                    column*factor:(column+1)*factor]
                resulting_array = grow_array(temp_array, translation_table_dict)
                r_r = 0
                for n_row in resulting_array:
                    c_c = 0
                    for n_char in n_row:
                        new_shiny_array[row*(factor+1) + r_r][column*(factor+1) + c_c] = n_char
                        c_c +=1
                    r_r += 1

        count = fractal_away(number_of_turns_left -1, new_shiny_array, translation_table_dict)
    else:
        count = 0
        for dim_1 in current_array:
            for char in dim_1:
                if char == '#':
                    count += 1
    return count

def grow_array(current_array, translation_table_dict):
    look_up_string = np.array_repr(current_array)
    if look_up_string in translation_table_dict:
        new_array = translation_table_dict[look_up_string]
    else:
        print('Unexpected error string not found in dict', look_up_string)
    return new_array

def store_ar_dict_in_str(translation_table_dict, find_pattern_array, new_pattern_array):
    look_up_string = np.array_repr(find_pattern_array)
    translation_table_dict[look_up_string] = new_pattern_array

def create_array_from_string(left_part):
    return np.array([list(inner_part) for inner_part in left_part.split('/')])

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1, 2)
problem_a(PROGBLEM_INPUT_TXT, 0, 5)  #136, 144 is too low 258 too high
print("\n")
