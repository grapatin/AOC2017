#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day06-Memory-Reallocation/input.txt").read_text()

exampleInput1 = """0 2 7 0"""
exampleResult1 = 5

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problem(input, expectedResult, problemB = False):
    solution = 0
    numbers = [int(word) for word in input.split()]
    count = 0
    length = len(numbers)
    storageDict = {}

    while (solution == 0):
        max = 0
        maxIndex = 0
        #find max
        stringOfNumbers = ''
        for i in range(length):
            number = numbers[i]
            stringOfNumbers += str(number)
            if  number > max:
                max = number
                maxIndex = i
        if stringOfNumbers in storageDict:
            #repeat found
            if problemB == False:
                solution = count
            else:
                solution = count - storageDict[stringOfNumbers]
        else:
            storageDict[stringOfNumbers] = count
        numberToDevide = max
        numbers[maxIndex] = 0
        for k in range(1,numberToDevide+1):
            i = (maxIndex + k) % length 
            numbers[i] = numbers[i] + 1
        count += 1
        
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problem(exampleInput1, exampleResult1)
problem(problemInputTxt, 7864)
print("\n")
problem(exampleInput1, 4, True)
problem(problemInputTxt, 0, True)
print("\n")

