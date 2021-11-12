#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day13-Packet-Scanners/input.txt").read_text()

exampleInput1 = """0: 3
1: 2
4: 4
6: 4"""
exampleResult1 = 24

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = 0
    input = input.replace(':', '')
    rows = stringWorker(input)
    firewall_dict = {}
    start = 0
    max = 94+1

    for row in rows:
        firewall_dict[int(row.split()[0])] = int(row.split()[1])

    penality = 0
    #move forward each pico second from 0 -> 94
    #each firewall starts at top and have a dept listed in the firewall_dict 
    #if time % ((dept -1)*2) == 0 then we have a hit
    for time in range(max):
        if time in firewall_dict:
            dept = firewall_dict[time]
            hit = time % ((dept - 1)* 2)
            if hit == 0: #yes we have a hit
                penality += dept*time

    solution = penality

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 1528)
print("\n")

def problemB(input, expectedResult):
    solution = 0
    input = input.replace(':', '')
    rows = stringWorker(input)
    firewall_dict = {}
    max = 94

    for row in rows:
        firewall_dict[int(row.split()[0])] = int(row.split()[1])

    startTime = 0
    failing = True
    while failing:
        step = 0
        failing = False
        for time in range(startTime, max+startTime+1):
            if step in firewall_dict:
                dept = firewall_dict[step]
                hit = time % ((dept - 1)* 2)
                if hit == 0: #yes we have a hit
                    failing = True
                    startTime += 1
                    break
            step += 1

    solution = startTime

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)


problemB(exampleInput1, 10)
problemB(problemInputTxt, 3896406)
print("\n")

