#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day08-I-Heard-You-Like-Registers/input.txt").read_text()

exampleInput1 = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10"""
exampleResult1 = 1

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problem(input, expectedResult, problemB = False):
    input = input.replace('if', '_if')
    rows = stringWorker(input)
    localsDict = {}
    tempMax = -99999999
    for row in rows:
        expressions = row.split('_')
        #get register in if case
        register = expressions[1].split()[1]
        if register not in localsDict:
            localsDict[register] = 0
        if eval(expressions[1][3:], {}, localsDict):
            commands = expressions[0].split()
            leftReg = commands[0]
            if leftReg not in localsDict:
                localsDict[leftReg] = 0
            if commands[1] == 'inc':
                localsDict[leftReg] += int(commands[2])
            else:
                localsDict[leftReg] -= int(commands[2])

        for reg in localsDict:
            if localsDict[reg] > tempMax:
                tempMax = localsDict[reg]

    max = -999999999
    for reg in localsDict:
        if localsDict[reg]> max:
            max = localsDict[reg]
    if problemB == False:
        solution = max
    else:
        solution = tempMax

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problem(exampleInput1, exampleResult1)
problem(problemInputTxt, 5966)
problem(problemInputTxt, 6347, True)
print("\n")

