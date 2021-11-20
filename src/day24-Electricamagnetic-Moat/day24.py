"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day24-Electricamagnetic-Moat/input.txt").read_text()

EXAMPLE_INPUT1 = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10"""
EXAMPLE_RESULT1 = 31

class BridgeBuilder:
    def __init__(self, input_string):
        rows = input_string.split('\n')
        self.storage_dict = {}
        self.available_entries_dict = {}
        for row_number in range(1, len(rows)+1):
            numbers = [int(numb) for numb in rows[row_number-1].split('/')]
            self.storage_dict[row_number] = numbers
            self.storage_dict[row_number*-1] = numbers[::-1]
            self.available_entries_dict[row_number] = 1
            self.available_entries_dict[row_number*-1] = 1

    def traverse(self, find_match, available_dict):
        #first find_match
        #if none return 0
        #if multiple traverse
        max_so_far = 0
        for number in available_dict:
            if self.storage_dict[number][0] == find_match:
                new_available_dict = available_dict.copy()
                result = self.storage_dict[number][0] + self.storage_dict[number][1]
                del new_available_dict[number]
                del new_available_dict[number*-1]
                result += self.traverse(self.storage_dict[number][1], new_available_dict)
                if result > max_so_far:
                    max_so_far = result
        return max_so_far

    def traverse_b(self, find_match, available_dict):
        #first find_match
        #if none return 0
        #if multiple traverse
        max_so_far = 0
        max_length = 0
        for number in available_dict:
            if self.storage_dict[number][0] == find_match:
                new_available_dict = available_dict.copy()
                result = self.storage_dict[number][0] + self.storage_dict[number][1]
                length = 1
                del new_available_dict[number]
                del new_available_dict[number*-1]
                [t_result, t_length] = self.traverse_b(self.storage_dict[number][1], new_available_dict)
                result += t_result
                length += t_length
                if length >= max_length:
                    if result > max_so_far and length == max_length:
                        max_so_far = result
                    elif length > max_length:
                        max_so_far = result
                    max_length = length
        return [max_so_far, max_length]

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    bridge = BridgeBuilder(input_string)
    solution = bridge.traverse(0, bridge.available_entries_dict)

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
problem_a(PROBLEM_INPUT_TXT, 1940)
print("\n")

def problem_b(input_string, expected_result):
    """Problem B solved function
    """
    bridge = BridgeBuilder(input_string)
    solution = bridge.traverse_b(0, bridge.available_entries_dict)

    if solution[0] == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(PROBLEM_INPUT_TXT, 1928)