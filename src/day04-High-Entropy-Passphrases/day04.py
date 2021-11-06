#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day04-High-Entropy-Passphrases/input.txt").read_text()

exampleInput1 = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""
exampleResult1 = 2

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0

    rows = stringWorker(input)
    for row in rows:
        valid = True
        dictCheck = {}
        words = row.split()
        for word in words:
            if word in dictCheck:
                valid = False
            else:
                dictCheck[word] = 1
        if valid == True:
            solution += 1

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 466)
print("\n")

def problemB(input, expectedResult):
    solution = 0

    rows = stringWorker(input)
    for row in rows:
        valid = True
        dictCheck = {}
        words = row.split()
        for word in words:
            chars = list(word)
            chars.sort()
            anagramWord = ''.join(chars)
            if anagramWord in dictCheck:
                valid = False
                break
            else:
                dictCheck[anagramWord] = 1
        if valid == True:
            solution += 1

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB("""abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio""", 3)
problemB(problemInputTxt, 251)