"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"dayXX/input.txt").read_text()

EXAMPLE_INPUT1 = """aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]"""
EXAMPLE_RESULT1 = 1514

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    solution = input_string

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROGBLEM_INPUT_TXT, 0)
print("\n")
