#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day12-Digital-Plummer/input.txt").read_text()

exampleInput1 = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""
exampleResult1 = 6

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def recursive(program, stDict, visitedString, findProgram = '0'):
    found = 0
    if program in stDict:
        for subProgram in stDict[program].split():
            if subProgram == findProgram:
                found = 1
            else:
                if ('a' + subProgram) not in visitedString:
                    if recursive(subProgram, stDict, visitedString + 'a' + subProgram) == 1:
                        found = 1
    return found

def problemA(input, expectedResult):
    solution = 0

    stDict = {}
    input = input.replace(',', '')
    pipelines = stringWorker(input)
    for pipe in pipelines:
        parts = pipe.split(' <-> ')
        stDict[parts[0]] = parts[1]

    count = 0
    for program in stDict:
        if (program != 0):            
            count += recursive(program, stDict, 'a' + program)
    solution = count
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 130)
print("\n")


def recursiveB(program, stDict, foundDict):
    if program in stDict:
        for subProgram in stDict[program].split():
            if subProgram not in foundDict:
                foundDict[subProgram] = 1
                recursiveB(subProgram, stDict, foundDict)

 
def problemB(input, expectedResult):
    solution = 0

    foundDict = {}
    stDict = {}
    dictOfGroups = {}
    input = input.replace(',', '')
    pipelines = stringWorker(input)
    for pipe in pipelines:
        parts = pipe.split(' <-> ')
        stDict[parts[0]] = parts[1]
        dictOfGroups[parts[0]] = parts[1]
    
    count = 0
    for program in stDict:
        if program not in foundDict:
            #Go through all branches and store all found branches but don't visit already visited branches
            recursiveB(program, stDict, foundDict)
            count += 1
    
    
    solution = count
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB(exampleInput1, 2)
problemB(problemInputTxt, 189)
print("\n")
