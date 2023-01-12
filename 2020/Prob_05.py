from ReadFile import *

def Split(line, row, col):
    if(len(line) == 0):
        return row[0], col[0]
    rdif = row[1] - row[0]
    cdif = col[1] - col[0]
    if(line[0] == "B"):
        row[0] = row[0] + int(rdif/2) + 1
    elif(line[0] == "F"):
        row[1] = row[0] + int(rdif/2)
    elif(line[0] == "L"):
        col[1] = col[0] + int(cdif/2)
    elif(line[0] == "R"):
        col[0] = col[0] + int(cdif/2) + 1
    return Split(line[1:],row,col)
    

def GetHighestSeatID(lines = None):
    if(not lines):
        lines = ReadInputFile()
    mmax = 0
    for line in lines:
        row,col = Split(line, [0,127], [0,7])
        num = row * 8 + col
        mmax = max(mmax, num)
    return mmax

def FindSeatID():
    lines = ReadInputFile()
    mmax = GetHighestSeatID(lines)
    seats = [0] * mmax
    for line in lines:
        row,col = Split(line, [0,127], [0,7])
        seats[row*8+col-1] = 1
    for i in range(1,mmax):
        if(seats[i] == 0 and seats[i-1] == 1 and seats[i+1] == 1):
            return i+1
    return -1
    

print(str(FindSeatID()))