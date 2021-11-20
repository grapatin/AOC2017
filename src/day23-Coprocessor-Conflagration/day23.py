"""
Template code
"""
from pathlib import Path
import logging
from assembler_class import AssemblyProcessor


PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2017/src/"\
    +"day23-Coprocessor-Conflagration/input.txt").read_text()

class CoProcessor(AssemblyProcessor):
    def __init__(self, code_array, intial_value_a):
        AssemblyProcessor.__init__(self, code_array)
        self.registry_dict['a'] = intial_value_a
        self.counter = 0
        logging.basicConfig(filename='advent_of_code.log', level=logging.INFO, filemode='w')


    def _mul(self, code_string):
        self.counter += 1
        AssemblyProcessor._mul(self, code_string)

    def print_state(self):
        logging_string = F'Reg: {self.registry_dict} PC: {self.program_counter} \
            {self._code_array[self.program_counter]}'
        logging.info(logging_string)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    code_array = input_string.split('\n')
    micro_controller = CoProcessor(code_array, 0)
    while (micro_controller.program_counter >= 0 and micro_controller.program_counter < len (code_array)):
        micro_controller.print_state()
        micro_controller.execute()

    solution = micro_controller.counter

    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

    #Problem B is to calculate how many non primes there are between 108400 and 125400 step 17
    #it was needed to figure out the assembler to do write this code...


problem_a(PROGBLEM_INPUT_TXT, 6724)
print("\n")


def prob_b(expected_result):
    non_prime = 0
    start_number = 108400
    stop_number = 125400
    for number in range(start_number, stop_number+1, 17):
        for i in range(2, int(number/2)+1):
            if (number % i) == 0:
                non_prime += 1
                break

    solution = non_prime

    if solution == expected_result:
        print("B: Correct solution found:", solution)
    else:
        print("B: Incorrect solution, we got:", solution, "expected:", expected_result)

prob_b(903)
