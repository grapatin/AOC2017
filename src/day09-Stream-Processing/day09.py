#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day09-Stream-Processing/input.txt").read_text()

exampleInput1 = """{{<!!>},{<!!>},{<!!>},{<!!>}}"""
exampleResult1 = 9

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def recursiveCurlyBrackets(inStr, score):
    l = 0
    length = len(inStr)
    tempScore = 0
    while l < length:
        if (inStr[l] == '{'):
            [newScore, jumpForward] = recursiveCurlyBrackets(inStr[l+1:], score + 1)
            tempScore += newScore
            l += jumpForward
        elif (inStr[l] == '}'):
            return [tempScore + score, l+1]
        l += 1
    return [tempScore + score, 0]

def problem(input, expectedResult, problemB = False):
    solution = 0
    #1. Remove ! and following character
    withoutExclamation = ''
    l = 0
    length = len(input)
    while l < length:
        if input[l] == '!':
            l += 2 #skip next character
        else:
            withoutExclamation += input[l]
            l += 1
    #2. Remove garbage < and all following character until >
    withoutGarbage = ''
    length = len(withoutExclamation)
    state = 'Normal'
    l = 0
    garbageCount = 0
    while l < length:
        if withoutExclamation[l] == '<' and state == 'Normal':
            state = 'withinGarbage'
        elif withoutExclamation[l] != '>' and state == 'withinGarbage':
            garbageCount += 1
        elif withoutExclamation[l] == '>' and state == 'withinGarbage':
            state = 'Normal'
        else:
            withoutGarbage += withoutExclamation[l]
        l += 1
    
    temp = recursiveCurlyBrackets(withoutGarbage, 0)

    solution = temp[0]
    if problemB == True:
        solution = garbageCount
    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problem(exampleInput1, exampleResult1)
problem(problemInputTxt, 20530)
print("\n")

problem('<{o"i!a,<{i<a>', 10, True)
problem(problemInputTxt, 0, True)
