from ReadFile import *

def CheckGroupOneYes(lines):
    yeses = []
    for line in lines:
        line = line.split()[0]
        for letter in line:
            if(letter not in yeses):
                yeses.append(letter)
    return len(yeses)

def CheckGroupAllYes(lines):
    yeses = {}
    peopleCount = 0
    for line in lines:
        peopleCount += 1
        line = line.split()[0]
        for letter in line:
            if(letter in yeses):
                yeses[letter] += 1
            else:
                yeses[letter] = 1
    total = 0
    for key in yeses:
        if(yeses[key] == peopleCount):
            total += 1
    return total            

def CheckQuestions():
    total = 0
    lines = ReadInputFile()
    curLines = []
    for line in lines:
        if(line != "\n"):
            curLines.append(line)
        else:
            total += CheckGroupAllYes(curLines)
            curLines = []
    total += CheckGroupAllYes(curLines)
    return total

print(str(CheckQuestions()))