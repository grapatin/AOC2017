#import cmath for complex number operations
from abc import abstractproperty
import cmath
import itertools
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day02-Corruption-Checksum/input.txt").read_text()

exampleInput1 = """5 1 9 5
7 5 3
2 4 6 8"""
exampleResult1 = 18

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0
    rows = stringWorker(input)
    for row in rows:
        low = 99999999
        high = 0
        values = row.split()
        for value in values:
            if int(value) < low:
                low = int(value)
            if int(value) > high:
                high = int(value)
        solution += (high - low)

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 54426)
print("\n")

def problemB(input, expectedResult):
    solution = 0
    rows = stringWorker(input)
    for row in rows:
        low = 99999999
        high = 0
        values = row.split()
        combinations = list(itertools.combinations(values, 2))
        for comb in combinations:
            value1 = int(comb[0])
            value2 = int(comb[1])

            if value2 > value1:
                if value2 % value1 == 0:
                    solution += value2 / value1
            else:
                if value1 % value2 == 0:
                    solution += value1 / value2
                

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB("""5 9 2 8
9 4 7 3
3 8 6 5""", 9)
problemB(problemInputTxt, 333)