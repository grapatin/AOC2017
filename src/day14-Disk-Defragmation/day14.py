"""Advent of code

"""
#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day10-Knot-Hash/input.txt").read_text()

EXAMPLE_INPUT1 = """3, 4, 1, 5"""
EXAMPLE_RESULT1 = 12

def string_worker(input_string):
    """Helper function for string handling
    """
    a_steps = input_string.split("\n")
    return a_steps


def knot_hash(input_string):
    """Implements the Knot Hash algorithm

    """
    seed = [17, 31, 73, 47, 23]
    command_array = []
    length = 256

    for char in input_string:
        command_array.append(ord(char))
    command_array += seed

    skip_size = 0
    curr_pos = 0
    list_to_hash = [num for num in range(length)]
    for _ in range(64):
        for instr in command_array:
            templist = list_to_hash + list_to_hash
            swith_list = templist[curr_pos:curr_pos+instr]
            swith_list.reverse()
            for i in range(instr):
                new = (curr_pos + i) % length
                list_to_hash[new] = swith_list[i]
            curr_pos = (curr_pos + instr + skip_size) % length
            skip_size += 1

    sparse_hash = list_to_hash
    dense_hash = []

    for loop_var in range(16):
        temp = sparse_hash[loop_var*16]
        for k in range(1,16):
            temp = temp ^ sparse_hash[loop_var*16 + k]
        dense_hash.append(temp)

    hex_string = ''
    for el_var in dense_hash:
        h_var = hex(el_var)
        if len(h_var) == 3:
            h_var = h_var[:2] + '0' + h_var[-1:]
        hex_string += h_var[2:]

    return hex_string

def problem_a(input_string, expected_result):
    """Function to solve problem A
    """
    count = 0
    for row in range(128):
        hash_this = input_string+'-'+str(row)
        hash_k = knot_hash(hash_this)
        #print(hashThis, 'has hash:', hash)
        integer = int('0x'+hash_k, 16)
        string_of_bin = bin(integer)
        count += string_of_bin.count('1')

    solution = count

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_a('flqrgnkx', 8108)
problem_a('jzgqcdpd', 8074)

def recursive_search(pos_row, pos_char, disk, count):
    """recursive function to search for groups
    """
    if pos_row >= 0 and pos_row < 128 and pos_char >= 0 and pos_char < 128:
        current_char = disk[pos_row][pos_char]
        if current_char == '#':
            disk[pos_row][pos_char] = count
            recursive_search(pos_row, pos_char + 1, disk, count)
            recursive_search(pos_row, pos_char - 1, disk, count)
            recursive_search(pos_row + 1, pos_char, disk, count)
            recursive_search(pos_row - 1, pos_char, disk, count)


def problem_b(input_string, expected_result):

    """problem B implementation

    #Parameters
    #   input_string (str): String used as problem input
    #   expected_result (any): Expected result for problem

    #Returns
    #   none
    """

    count = 0
    disk = []
    for row in range(128):
        hash_this = input_string+'-'+str(row)
        hash_calculated = knot_hash(hash_this)
        #print(hashThis, 'has hash:', hash)
        integer = int('0x'+hash_calculated, 16)
        string_of_bin = bin(integer)[2:].zfill(128).replace('1', '#').replace('0', '.')
        row_array = []
        for char in string_of_bin:
            row_array.append(char)
        disk.append(row_array)

    for row in range(128):
        for char in range(128):
            current_char = disk[row][char]
            if current_char == '#':
                count += 1
                recursive_search(row, char, disk, count)


    solution = count

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

problem_b('flqrgnkx', 1242)
problem_b('jzgqcdpd', 1212)
