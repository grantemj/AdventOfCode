from ReadFile import *


def AccBeforeRepeat(lines):
    acc = 0
    idx = 0
    track = [0] * len(lines)
    while(idx < len(lines)):
        if(track[idx]):
            break
        track[idx] = 1
        inst = lines[idx].split()
        inst[1] = int(inst[1])
        if(inst[0] == "nop"):
            idx += 1
        elif(inst[0] == "acc"):
            acc += inst[1]
            idx += 1
        elif(inst[0] == "jmp"):
            idx += inst[1]
    return acc, idx

def FindNoRepeat(lines):
    origLines = lines[:]    # Copy contents
    repeating = True
    tried = [0] * len(lines)
    while(repeating):
        lines = origLines[:]    # Reset contents
        for idx in range(len(lines)):   # Find next one to try
            if(not tried[idx] and lines[idx].split()[0] != "acc"):
                tried[idx] = 1
                break
        if(lines[idx].split()[0] == "nop"):     # Swticheroos
            lines[idx] = lines[idx].replace("nop","jmp")
        else:
            lines[idx] = lines[idx].replace("jmp","nop")
        acc, idx = AccBeforeRepeat(lines)       # Testin'
        if(idx == len(lines)):      # Checkin'
            repeating = False
    return acc
        
    
# Idk why I commented this so much for once
lines = ReadInputFile()
# print(str(AccBeforeRepeat(lines)[0]))
print(str(FindNoRepeat(lines)))