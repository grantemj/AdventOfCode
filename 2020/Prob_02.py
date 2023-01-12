from ReadFile import *

def ParseLine(line):
    chunks = line.split()
    occurances = chunks[0].split("-")
    mmin = occurances[0]
    mmax = occurances[1]
    letter = chunks[1][0]
    password = chunks[-1]
    return int(mmin),int(mmax),letter,password
    
def LetterCount(letter,pw):
    total = 0
    for dig in pw:
        total += (dig==letter)
    return total

def FindCorrupted():
    lines = ReadInputFile()
    total = 0
    for line in lines:
        mmin,mmax,letter,pw = ParseLine(line)
        count = LetterCount(letter, pw)
        total += (mmin <= count <= mmax)
    print(total)
    
def FindCorrupted2():
    lines = ReadInputFile()
    total = 0
    for line in lines:
        pos1,pos2,letter,pw = ParseLine(line)
        total += ((pw[pos1-1]==letter) ^ (pw[pos2-1]==letter))
    print(total)

FindCorrupted2()
    