#import cmath for complex number operations
from abc import abstractproperty
import cmath
#import Path for file operations
from pathlib import Path

problemInputTxt = Path("/Users/pergrapatin/Source/AOC2017/src/day07-Recursive-Circus/input.txt").read_text()

exampleInput1 = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""
exampleResult1 = 'tknk'

gTower = ''
gWeightChange = 0

def stringWorker(input):
    aSteps = input.split("\n")
    return aSteps

def problemA(input, expectedResult):
    solution = -1

    storageDict = {}
    input = input.replace(',','')
    rows = stringWorker(input)
    for row in rows:
        baseTower = row.split(' ')[0]
        if '->' in row:
            secondPart = row.split('->')[1]
            topTowers = secondPart.split()
            for topTower in topTowers:
                storageDict[topTower] = baseTower

    for row in rows:
        baseTower = row.split(' ')[0]
        if baseTower not in storageDict:
            solution = baseTower
            break


    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)

def recursiveDig(baseTower, storageWeightIndividual, storageBottomTop):
    global gTower
    global gWeightChange
    towerWeight = []
    totalWeight = 0
    if baseTower not in storageBottomTop:
        return storageWeightIndividual[baseTower]
    else:
        topTowers = storageBottomTop[baseTower]
        for tower in topTowers:
            weight = recursiveDig(tower, storageWeightIndividual, storageBottomTop)
            totalWeight += weight
            towerWeight.append(weight)
        
        for i in range(len(towerWeight)):
            if towerWeight.count(towerWeight[i]) == 1:
                #This is the failing version
                #print('Failing disk is:', topTowers[i])
                gTower = topTowers[i]
                if i > 0:
                    gWeightChange = towerWeight[i-1]-towerWeight[i]
                    #print('Disk size should be adjusted with:', gWeightChange)
                else:
                    gWeightChange = towerWeight[i+1]-towerWeight[i]
                    #print('Disk size should be adjusted with:', gWeightChange)
                storageWeightIndividual[gTower] = storageWeightIndividual[gTower] + gWeightChange
                totalWeight += gWeightChange


    totalWeight += storageWeightIndividual[baseTower]
    return totalWeight

def problemB(input, expectedResult):
    global gTower
    global gWeightChange
    solution = -1

    storageTopBottom = {}
    storageBottomTop = {}
    storageWeightIndividual = {}
    storageWeightAbove = {}
    input = input.replace(',','')
    input = input.replace('(','*')
    input = input.replace(')','*')
    rows = stringWorker(input)
    for row in rows:
        Tower = row.split(' ')[0]
        weight =int(row.split('*')[1])
        storageWeightIndividual[Tower] = weight
        if '->' in row:
            secondPart = row.split('->')[1]
            topTowers = secondPart.split()
            storageBottomTop[Tower] = topTowers
            for topTower in topTowers:
                storageTopBottom[topTower] = Tower

    for row in rows:
        baseTower = row.split(' ')[0]
        if baseTower not in storageTopBottom:
            solution = baseTower
            break
    
    #start at Base do recursive call to next level until no more levels
    recursiveDig(solution,storageWeightIndividual,storageBottomTop)
    solution = storageWeightIndividual[gTower]

    if solution == expectedResult:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expectedResult)
    
problemA(exampleInput1, exampleResult1)
problemA(problemInputTxt, 'vmpywg')
print("\n")
problemB(exampleInput1, 60)
problemB(problemInputTxt, 1674)