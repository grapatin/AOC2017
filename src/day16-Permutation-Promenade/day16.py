"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day16-Permutation-Promenade/input.txt").read_text()

EXAMPLE_INPUT1 = """s1,x3/4,pe/b"""
EXAMPLE_RESULT1 = 'baedc'

def string_worker(input_string):
    """Helper string worker function
    """
    a_steps = input_string.split("\n")
    return a_steps

def problem_a(input_string, expected_result, dancing_chars):
    """Problem A solved function
    """
    solution = input_string
    commands = input_string.replace(',', ' ').split()

    dancing_chars = dance_routine(dancing_chars, commands)

    solution = dancing_chars
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def dance_routine(dancing_chars, commands):
    """Dance dance dance
    """
    for command in commands:
        if command[0] == 's':
            number_chars = int(command[1:])
            dancing_chars = dancing_chars[-number_chars:] + dancing_chars[:-number_chars]
        elif command[0] == 'x':
            command = command[1:].replace('/', ' ').split()
            char_1 = int(command[0])
            char_2 = int(command[1])
            if char_1 > char_2:
                char_1, char_2 = char_2, char_1
            dancing_chars = dancing_chars[:char_1] + dancing_chars[char_2] + \
                dancing_chars[char_1 + 1:char_2] + dancing_chars[char_1] + \
                dancing_chars[char_2 + 1:]
        elif command[0] == 'p':
            swap1 = command[1]
            swap2 = command[-1]
            temp_char = 'z'
            dancing_chars = dancing_chars.replace(swap1, temp_char)
            dancing_chars = dancing_chars.replace(swap2, swap1)
            dancing_chars = dancing_chars.replace(temp_char, swap2)
        else:
            assert False #Unexpected
    return dancing_chars

problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1, 'abcde')
problem_a(PROGBLEM_INPUT_TXT, 'dcmlhejnifpokgba', 'abcdefghijklmnop')
print("\n")

def problem_b(input_string, expected_result, dancing_chars):
    """Problem B solver function
    """
    solution = input_string
    commands = input_string.replace(',', ' ').split()
    count = 0
    storage_dict = {}
    billion_times = 1000000000
    while count < billion_times:
        if dancing_chars in storage_dict:
            #we have a repeat
            print("We have a repeat at", count, "from:", storage_dict[dancing_chars])
            dance_is_repeating_after = count - storage_dict[dancing_chars]
            dance_steps_left = billion_times % dance_is_repeating_after
            count = billion_times - dance_steps_left
            storage_dict = {}
        else:
            storage_dict[dancing_chars] = count
        dancing_chars = dance_routine(dancing_chars, commands)
        count += 1
        

    solution = dancing_chars
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b(PROGBLEM_INPUT_TXT, 'ifocbejpdnklamhg', 'abcdefghijklmnop')
