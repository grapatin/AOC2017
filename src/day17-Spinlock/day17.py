"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
#from pathlib import Path


EXAMPLE_INPUT1 = 3
EXAMPLE_RESULT1 = 638

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_value, expected_result):
    """Problem A solved function
    """
    solution = input_value
    data_array = [0]
    current_index = 0
    rotate_number_of_times = input_value

    for loop in range(1,2018):
        length_data_array = len(data_array)
        current_index = current_index + rotate_number_of_times
        current_index = current_index % length_data_array
        current_index += 1
        data_array.insert(current_index, loop)

    solution = data_array[current_index + 1]

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(314, 355)
print("\n")



def problem_b(input_value, expected_result):
    """Problem A solved function
    """
    solution = input_value
    current_index = 0
    rotate_number_of_times = input_value
    current_index_for_zero = 0
    int_after_zero = -1

    for loop in range(1,50000001):
        length_data_array = loop
        current_index = current_index + rotate_number_of_times
        current_index = current_index % length_data_array
        current_index += 1
        if current_index == current_index_for_zero + 1:
            int_after_zero = loop
        if current_index_for_zero > current_index:
            current_index_for_zero += 1

    solution = int_after_zero

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(314, 6154117)
print("\n")
