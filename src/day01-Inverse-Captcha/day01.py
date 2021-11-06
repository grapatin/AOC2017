#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day01-Inverse-Captcha/input.txt").read_text()

exampleInput1 = """91212129"""
exampleResult1 = 1

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def reverseCaptcha(stringToCheck):
    #Since circular add first also as last character
    stringToCheckN = stringToCheck + stringToCheck
    count = 0

    for l in range(len(stringToCheck)):
        if stringToCheckN[l] == stringToCheckN[l+int(len(stringToCheck)/2)]:
            count += int(stringToCheckN[l])
    return count


def reverseCaptchaA(stringToCheck):
    #Since circular add first also as last character
    stringToCheckN = stringToCheck + stringToCheck
    count = 0

    for l in range(len(stringToCheck)):
        if stringToCheckN[l] == stringToCheckN[l+1]:
            count += int(stringToCheckN[l])
    return count

def problemA(input, expectedResult):
    solution = reverseCaptchaA(input)
    if expectedResult == solution:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)


def problemB(input, expectedResult):
    solution = reverseCaptcha(input)
    if expectedResult == solution:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 1049)
print("\n")
problemB(problemInputTxt, 1508)

