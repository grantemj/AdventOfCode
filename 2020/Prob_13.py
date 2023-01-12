from ReadFile import *
import math
import numpy as np

def GetIDs(line):
    ids = []
    difs = []
    lastNum = 0
    nums = line.split(",")
    for idx in range(len(nums)):
        if(str.isnumeric(nums[idx])):
            ids.append(int(nums[idx]))
            difs.append(idx-lastNum)
            lastNum = idx
    return ids, difs

def FindOrder(ids):
    order = []
    curMax = math.inf
    tempMax = -1
    tempMaxIdx = -1
    for j in ids:
        for i in range(len(ids)):
            if(ids[i] > tempMax and ids[i] < curMax):
                tempMax = ids[i]
                tempMaxIdx = i
        order.append(tempMaxIdx)
        curMax = tempMax
        tempMax = -1
    return order

def TestIDs1(lines):
    goal = int(lines[0])
    ids, difs = GetIDs(lines[1])
    minn = -1
    busId = -1
    for idd in ids:
        num = idd
        while(num < goal):
            num += idd
        if(minn == -1 or num < minn):
            minn = num
            busId = idd
            print("Bus: " + str(busId) + " \tTime: " + str(num))
    return busId * (minn - goal)

def TestIDs2(lines):
    ids, difs = GetIDs(lines[1])
    order = FindOrder(ids)
    difsCumulative = [0] * len(difs)
    for i in range(1,len(difs)):
        difsCumulative[i] = difsCumulative[i-1] + difs[i]
    print(ids)
    print(difs)
    print(order)
    print(difsCumulative)
    
    A = []
    B = []
    for i in range(1,len(difs)):
        row = [0] * len(difs)
        row[0] = -1 * ids[0]
        row[i] = ids[i]
        A.append(row)
        B.append(difsCumulative[i])
    # row = [0] * len(difs)
    # row[-2] = -1 * ids[-2]
    # row[-1] = ids[-1]
    # A.append(row)
    # B.append(difs[-1])
    print(A)
    print(B)
    A = np.array(A)
    B = np.array(B)
    C = np.linalg.lstsq(A,B)
    print(C)
    
    
    
    # difToMax = 0
    # for i in range(order[0]+1):
    #     difToMax += difs[i]
    # # print(difToMax)
    # toBeat = 0
    # while(1):
    #     toBeat += ids[order[0]]          # Have to be in intervals of the largest number
    #     # print(toBeat)
    #     soFar = [0] * len(ids)
    #     # while(soFar[0] < (toBeat - difToMax)):
    #     #     soFar[0] += ids[0]
    #     # if(soFar[0] != (toBeat - difToMax)):                # Try again
    #     #     continue
    #     if((toBeat - difToMax) % ids[0] != 0):                # Try again
    #         continue
    #     soFar[0] = toBeat - difToMax
    #     for idx in range(1,len(ids)):
    #         # while(soFar[idx] < (soFar[idx-1] + difs[idx])):
    #         #     soFar[idx] += ids[idx]
    #         # if(soFar[idx] != (soFar[idx-1] + difs[idx])):   # Try again
    #         #     break
    #         if((soFar[idx-1] + difs[idx]) % ids[idx] != 0): # Try again
    #             break
    #         soFar[idx] = soFar[idx-1] + difs[idx]
    #     for i in order:
    #         if((soFar[0] + difsCumulative[i]) % ids[i] != 0):
    #             break
    #         soFar[i] = soFar[0] + difsCumulative[i]
    #     # allGood = True
    #     # for idx in range(1,len(ids)):
    #     #     if(soFar[idx] != soFar[idx-1] + difs[idx]):
    #     #         allGood = False
    #     #         break
    #     # if(allGood):
    #     if(soFar[-1] != 0):
    #         return soFar[0]
    #     if(soFar[6] != 0):
    #         print(soFar)





lines = ReadInputFile()
lines = StripNewLines(lines)
# print(str(TestIDs1(lines)))
print(str(TestIDs2(lines)))

# Guesses
# 449 - too low - didn't include the last number; forgot to multiply mins waiting
# 407 - too low - used idd instead of busId like a dodo -_-