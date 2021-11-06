#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day05-A-Maze-Of-Twisty-Trampolines/input.txt").read_text()

exampleInput1 = """0
3
0
1
-3"""
exampleResult1 = 5

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0
    commandsLines = stringWorker(input)
    pc = 0
    count = 0
    length = len(commandsLines)
    while (pc > -1 and pc < length):
        jumpDelta = int(commandsLines[pc])
        commandsLines[pc] = str(int(commandsLines[pc])+1)
        pc = pc + jumpDelta
        count += 1

    solution = count 
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 388611)
print("\n")

def problemB(input, expectedResult):
    solution = 0
    commandsLines = stringWorker(input)
    pc = 0
    count = 0
    length = len(commandsLines)
    while (pc > -1 and pc < length):
        jumpDelta = int(commandsLines[pc])
        if jumpDelta > 2:
            commandsLines[pc] = str(int(commandsLines[pc])-1)
        else:
            commandsLines[pc] = str(int(commandsLines[pc])+1)
        pc = pc + jumpDelta
        count += 1

    solution = count 
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB(exampleInput1, 10)
problemB(problemInputTxt, 27763113)
print("\n")
