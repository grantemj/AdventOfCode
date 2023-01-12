from ReadFile import *
import re

mustHave = ["eyr","hcl","hgt","pid","byr","iyr","ecl"]

def IsAPassport(lines):
    total = 0
    cid = 0
    for line in lines:
        line = line.split()
        for chunk in line:
            chunk = chunk.split(":")
            # print(chunk)
            if(chunk[0] in mustHave):
                total += CheckEachField(chunk[0],chunk[1])
    #         print(chunk[0] + ":" + chunk[1] + "  \t" + str(total))
    # print(total == len(mustHave))
    return (total == len(mustHave))

def CheckEachField(field, value):
    if(field == "eyr"):
        s = re.match("\d{4}",value)
        return (s != None) and (len(s.group()) == 4) and (2020 <= int(value) <= 2030)
    elif(field == "hcl"):
        s = re.match("#[0-9a-fA-F]{6}",value)
        return (s != None) and (len(s.group()) == 7)
    elif(field == "hgt"):
        if(value[-2:] == "cm"):
            return (150 <= int(value[:-2]) <= 193)
        elif(value[-2:] == "in"):
            return (59 <= int(value[:-2]) <= 76)
        return False
    elif(field == "pid"):
        s = re.match("\d{9}",value)
        return (s != None) and (len(s.group()) == 9)
    elif(field == "byr"):
        return (len(value) == 4) and (1920 <= int(value) <= 2002)
    elif(field == "iyr"):
        s = re.match("\d{4}",value)
        return (s != None) and (len(s.group()) == 4) and (2010 <= int(value) <= 2020)
    elif(field == "ecl"):
        colors = ["amb","blu","brn","gry","grn","hzl","oth"]
        return value in colors

def CheckPassports():
    total = 0
    lines = ReadInputFile()
    curLines = []
    for line in lines:
        if(line != "\n"):
            curLines.append(line)
        else:
            total += IsAPassport(curLines)
            curLines = []
    total += IsAPassport(curLines)
    return total

    
print (str(CheckPassports()))

