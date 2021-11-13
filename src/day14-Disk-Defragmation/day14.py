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


def knotHash(input):
    seed = [17, 31, 73, 47, 23]
    commandArray = []
    length = 256

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

    return hexString

def problemA(input, expectedResult):
    count = 0
    for row in range(128):
        hashThis = input+'-'+str(row)
        hash = knotHash(hashThis)
        #print(hashThis, 'has hash:', hash)
        integer = int('0x'+hash, 16)
        stringOfBin = bin(integer)
        count += stringOfBin.count('1')

    solution = count

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

#problemA('flqrgnkx', 8108)
#problemA('jzgqcdpd', 8074)

def recursiveSearch(posRow, posChar, disk, count):
    if posRow >= 0 and posRow < 128 and posChar >= 0 and posChar < 128:
        currentChar = disk[posRow][posChar]
        if currentChar == '#':
            disk[posRow][posChar] = count
            recursiveSearch(posRow, posChar + 1, disk, count)
            recursiveSearch(posRow, posChar - 1, disk, count)
            recursiveSearch(posRow + 1, posChar, disk, count)
            recursiveSearch(posRow - 1, posChar, disk, count)


def problemB(input, expectedResult):
    count = 0
    disk = []
    for row in range(128):
        hashThis = input+'-'+str(row)
        hash = knotHash(hashThis)
        #print(hashThis, 'has hash:', hash)
        integer = int('0x'+hash, 16)
        stringOfBin = bin(integer)[2:].zfill(128).replace('1', '#').replace('0', '.')
        rowArray = []
        for char in stringOfBin:
            rowArray.append(char)
        disk.append(rowArray)

    for row in range(128):
        for char in range(128):
            currentChar = disk[row][char]
            if currentChar == '#':
                count += 1
                recursiveSearch(row, char, disk, count)


    solution = count

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

problemB('flqrgnkx', 1242)
problemB('jzgqcdpd', 1212)