#import cmath for complex number operations

from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day11-Hex-Ed/input.txt").read_text()

exampleInput1 = """se,sw,se,sw,sw"""
exampleResult1 = 3

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problem(input, expectedResult, problemB = False):
    solution = 0
    input = input.replace(',', ' ')
    steps = input.split()
    x = 0
    y = 0
    maxD = 0

    for step in steps:
        if step == 'n':
            y += 2
        elif step == 's':
            y -= 2
        elif step == 'ne':
            x += 1
            y += 1
        elif step == 'se':
            x += 1
            y += -1
        elif step == 'nw':
            x -= 1
            y += 1
        elif step == 'sw':
            x -= 1
            y -= 1
        else:
            assert(False)
        distance = (abs(x)+abs(y)) / 2
        if distance > maxD:
            maxD = distance

    if problemB == False:
        solution = (abs(x)+abs(y)) / 2
    else:
        solution = maxD
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problem(exampleInput1, exampleResult1)
problem(problemInputTxt, 824)
print("\n")

problem(problemInputTxt, 0, True)

