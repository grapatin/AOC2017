"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/day15-Dueling-Generators/input.txt").read_text()

EXAMPLE_INPUT1 = """Generator A starts with 65
Generator B starts with 8921"""
EXAMPLE_RESULT1 = 588

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def calculator_f(factor, in_value):
    """calculator
    """
    division_r = in_value*factor % 2147483647
    return division_r

def calculator_for_b(factor, in_value, even_with):
    """calculator
    """
    division_r = -1
    while division_r % even_with:
        division_r = in_value*factor % 2147483647
        in_value = division_r
    return division_r

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    generator_a = 16807
    generator_b = 48271
    solution = 0
    rows = string_worker(input_string)
    gen_1_start_value = int(rows[0].split()[-1])
    gen_2_start_value = int(rows[1].split()[-1])
    next_value_1 = gen_1_start_value
    next_value_2 = gen_2_start_value
    for _ in range(40000000):
        next_value_1 = calculator_f(generator_a, next_value_1)
        next_value_2 = calculator_f(generator_b, next_value_2)
        if next_value_1 & 0xffff == next_value_2 & 0xffff:
            solution += 1
            #print('Found:', solution, next_value_1, '  ', next_value_2)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

#problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
#problem_a(PROGBLEM_INPUT_TXT, 573)
#print("\n")

def problem_b(input_string, expected_result):
    """Problem B solver function
    """
    generator_a = 16807
    generator_b = 48271
    solution = 0
    rows = string_worker(input_string)
    gen_1_start_value = int(rows[0].split()[-1])
    gen_2_start_value = int(rows[1].split()[-1])
    next_value_1 = gen_1_start_value
    next_value_2 = gen_2_start_value

    for _ in range(5000000):
        next_value_1 = calculator_for_b(generator_a, next_value_1, 4)
        next_value_2 = calculator_for_b(generator_b, next_value_2, 8)
        if next_value_1 & 0xffff == next_value_2 & 0xffff:
            solution += 1
            print('Found:', solution, next_value_1, '  ', next_value_2)


    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(EXAMPLE_INPUT1, 309)
problem_b(PROGBLEM_INPUT_TXT, 294)
print("\n")
