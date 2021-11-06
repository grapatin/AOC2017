#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day03-Spiral-Memory/input.txt").read_text()

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0
    x = 0
    y = 0
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    phase = 'right'
    masterDict = {}
    for i in range(1,input+1):
        masterDict[str(x)+'X;Y'+str(y)] = i
        #Find next available acording to rule
        if phase == 'right':
            x += 1
            if x > maxX:
                # Time for next phase
                phase = 'up'
                maxX = x
        elif phase == 'up':
            y += 1
            if y > maxY:
                # Time for next phase
                phase = 'left'
                maxY = y
        elif phase == 'left':
            x -= 1
            if x < minX:
                # Time for next phase
                phase = 'down'
                minX = x
        elif phase == 'down':
            y -= 1
            if y < minY:
                # Time for next phase
                phase = 'right'
                minY = y

    for key, value in masterDict.items():
        if value == input:
            xy = key.split('X;Y')
            solution = abs(int(xy[0]))+abs(int(xy[1]))
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

def calculateSumOfThoseAround(x,y):
    total = 0
    deltaX = [1, 1, 0,-1,-1,-1, 0, 1]
    deltaY = [0, 1, 1, 1, 0,-1,-1,-1]
    for i in range(8):
        tX = x + deltaX[i]
        tY = y + deltaY[i]
        dStr = str(tX)+'X;Y'+str(tY)
        if dStr in masterDict:
            total +=  masterDict[dStr]

    return total

masterDict = {}

def problemB(input, expectedResult):
    solution = 0
    x = 0
    y = 0
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0
    phase = 'right'
    for i in range(1,input+1):
        if x == 0 and y == 0:
            masterDict[str(x)+'X;Y'+str(y)] = 1
        else:
            sum = calculateSumOfThoseAround(x,y)
            masterDict[str(x)+'X;Y'+str(y)] = sum
            if sum > input:
                solution = sum
                break
        #Find next available acording to rule
        if phase == 'right':
            x += 1
            if x > maxX:
                # Time for next phase
                phase = 'up'
                maxX = x
        elif phase == 'up':
            y += 1
            if y > maxY:
                # Time for next phase
                phase = 'left'
                maxY = y
        elif phase == 'left':
            x -= 1
            if x < minX:
                # Time for next phase
                phase = 'down'
                minX = x
        elif phase == 'down':
            y -= 1
            if y < minY:
                # Time for next phase
                phase = 'right'
                minY = y

    for key, value in masterDict.items():
        if value == input:
            xy = key.split('X;Y')
            solution = abs(int(xy[0]))+abs(int(xy[1]))
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)


problemA(1024, 31)
problemA(277678, 475)
print("\n")

problemB(1024, 1968)
masterDict = {}
problemB(277678, 279138)
print("\n")