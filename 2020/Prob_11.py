from ReadFile import *

def PrintPortion(seats,rows):
    for i in range(rows):
        s = ""
        for j in range(rows):
            s += " " + seats[i][j]
        print(s)
    print("")
    
def PrintAdjacent(seats,rows,part):
    for i in range(rows):
        s = ""
        for j in range(rows):
            if part == 1:
                s += " " + str(SeatsAdjacent(seats,i,j))
            else:
                s += " " + str(SeatsInView(seats,i,j))
        print(s)
    print("")

def SeatsAdjacent(seats,row,col):
    count = 0
    irange = [-1,0,1]
    jrange = [-1,0,1]
    if(row == 0):
        irange = irange[1:]
    elif(row == len(seats)-1):
        irange = irange[:-1]
    if(col == 0):
        jrange = jrange[1:]
    elif(col == len(seats[0])-1):
        jrange = jrange[:-1]
    for i in irange:
        for j in jrange:
            if(i != 0 or j != 0):
                count += (seats[row+i][col+j] == "#")
    return count

def SeatsInView(seats,row,col):
    count = 0
    for i in range(1,row+1):                                  # N
        if(seats[row-i][col] == "#"):
            count += 1
            break
        elif(seats[row-i][col] == "L"):
            break
    for i in range(1,len(seats)-row):                         # S
        if(seats[row+i][col] == "#"):
            count += 1
            break
        elif(seats[row+i][col] == "L"):
            break
    for i in range(1,col+1):                                  # W
        if(seats[row][col-i] == "#"):
            count += 1
            break
        elif(seats[row][col-i] == "L"):
            break
    for i in range(1,len(seats[0])-col):                      # E
        if(seats[row][col+i] == "#"):
            count += 1
            break
        elif(seats[row][col+i] == "L"):
            break
    for i in range(1,min(row+1,col+1)):                       # NW
        if(seats[row-i][col-i] == "#"):
            count += 1
            break
        elif(seats[row-i][col-i] == "L"):
            break
    for i in range(1,min(len(seats)-row,len(seats[0])-col)):  # SE
        if(seats[row+i][col+i] == "#"):
            count += 1
            break
        elif(seats[row+i][col+i] == "L"):
            break
    for i in range(1,min(row+1,len(seats[0])-col)):           # SW
        if(seats[row-i][col+i] == "#"):
            count += 1
            break
        elif(seats[row-i][col+i] == "L"):
            break
    for i in range(1,min(len(seats)-row,col+1)):              # NE
        if(seats[row+i][col-i] == "#"):
            count += 1
            break
        elif(seats[row+i][col-i] == "L"):
            break
    return count

def ApplyRules(seats,changed,limit,part):
    if(changed > 4):
        return seats
    changed += 1
    nseats = [row[:] for row in seats]
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            if part == 1:
                sa = SeatsAdjacent(seats,row,col)
            else:
                sa = SeatsInView(seats,row,col)
            if(seats[row][col] == "#" and sa >= limit):
                nseats[row][col] = "L"
                changed = 0
            elif(seats[row][col] == "L" and sa == 0):
                nseats[row][col] = "#"
                changed = 0
    # if(changed == 0):
    #     PrintPortion(seats,10)
    #     PrintAdjacent(seats,10,part)
    return ApplyRules(nseats,changed,limit,part)
    
def PartOne(seats):
    endSeats = ApplyRules(seats,0,4,1)
    count = 0
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            count += (endSeats[row][col] == "#")
    return count
    
def PartTwo(seats):
    endSeats = ApplyRules(seats,0,5,2)
    count = 0
    for row in range(len(seats)):
        for col in range(len(seats[0])):
            count += (endSeats[row][col] == "#")
    return count

seats = SplitToList(StripNewLines(ReadInputFile()))
# print(str(PartOne(seats)))
print(str(PartTwo(seats)))


# Guesses
# 2278 - Too low
