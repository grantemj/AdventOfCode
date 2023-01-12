from ReadFile import *

def CountDifferences(order):
    ones = 0
    twos = 0
    threes = 0
    for idx in range(len(order)-1):
        dif = order[idx+1] - order[idx]
        if(dif == 1):
            ones += 1
        elif(dif == 2):
            twos += 1
        elif(dif == 3):
            threes += 1
        else:
            print("Should not happen")
    return ones, twos, threes

def FindMinimumOfList(nums):
    val, idx = min((val, idx) for (idx, val) in enumerate(nums))
    return val, idx

def FindAdapterOrder(lines):
    length = len(lines)
    order = [0]     # Wall output
    while(len(lines) > 0):
        val, idx = FindMinimumOfList(lines)
        order.append(lines.pop(idx))
    order.append(order[-1]+3)   # Internal adapter
    # print(order)
    # ones, twos, threes = CountDifferences(order)
    # return ones * threes
    return order

def FindPossibleDifs(order):
    if(len(order) < 3): # Not enough
        return 0
    total = 0
    for idx in range(len(order)-2):
        if(order[idx+2] - order[idx] < 4):
            # Can get rid of idx+1
            total += 1 + FindPossibleDifs(order[:idx+1]+order[idx+2:])
    return total

def FindPossibleDifs2(difs):
    total = 1
    count = 0
    one = False
    for dif in difs:
        if(dif == 1):
            if(one):
                count += 1
            else:
                one = True
        elif(dif != 1 and one):
            total *= (2**count)-(count == 3)
            count = 0
            one = False
    return total

def FindNumberOfOrders(lines):
    origOrder = FindAdapterOrder(lines)
    order = origOrder[:]
    difs = [j-i for i,j in zip(order[:-1],order[1:])]
    return FindPossibleDifs2(difs)
    # return FindPossibleDifs(order)

lines = ReadInputFile()
lines = [int(line) for line in lines]
# print(str(FindAdapterOrder(lines)))
print(str(FindNumberOfOrders(lines)))

# Part 1 Guessed:
# 2145  - Forgot to count the internal adapter
# 2210 (too low)    - Forgot to count the wall adapter