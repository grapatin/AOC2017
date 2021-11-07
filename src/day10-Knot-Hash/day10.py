#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day10-Knot-Hash/input.txt").read_text()

exampleInput1 = """3, 4, 1, 5"""
exampleResult1 = 12

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, length, expectedResult):
    solution = 0
    input = input.replace(',',' ')
    hashInstructions = [int(num) for num in input.split()]
    skipSize = 0
    currPos = 0
    listToHash = [num for num in range(length)]
    for instr in hashInstructions:
        templist = listToHash + listToHash
        swithList = templist[currPos:currPos+instr]
        swithList.reverse()
        for i in range(instr):
            new = (currPos + i) % length
            listToHash[new] = swithList[i]
        currPos = (currPos + instr + skipSize) % length
        skipSize += 1

    solution = listToHash[0]*listToHash[1]

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, 5, exampleResult1)
problemA(problemInputTxt, 256, 4480)
print("\n")

def problemB(input, length, expectedResult):
    solution = 0
    seed = [17, 31, 73, 47, 23]
    commandArray = []

    for char in input:
        commandArray.append(ord(char))
    commandArray += seed

    skipSize = 0
    currPos = 0
    listToHash = [num for num in range(length)]
    for t in range(64):
        for instr in commandArray:
            templist = listToHash + listToHash
            swithList = templist[currPos:currPos+instr]
            swithList.reverse()
            for i in range(instr):
                new = (currPos + i) % length
                listToHash[new] = swithList[i]
            currPos = (currPos + instr + skipSize) % length
            skipSize += 1

    sparseHash = listToHash
    denseHash = []
    
    for l in range(16):
        temp = sparseHash[l*16]
        for k in range(1,16):
            temp = temp ^ sparseHash[l*16 + k]
        denseHash.append(temp)

    hexString = ''
    for el in denseHash:
        h = hex(el)
        if len(h) == 3:
            h = h[:2] + '0' + h[-1:]
        hexString += h[2:]

    solution = hexString

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB('1,2,3', 256, '3efbe78a8d82f29979031a4aa0b16a9d')
problemB(problemInputTxt, 256, 'c500ffe015c83b60fad2e4b7d59dabc4')
