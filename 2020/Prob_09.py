from ReadFile import *

def CheckVailidity(num,prev):
    for i in range(len(prev)):
        for j in range(i+1,len(prev)):
            if(prev[i] + prev[j] == num):
                return True
    return False

def AddLargestAndSmallest(nums):
    maxx = -1
    minn = -1
    for num in nums:
        if(maxx == -1 or num > maxx):
            maxx = num
        if(minn == -1 or num < minn):
            minn = num
    print("Max: "+str(maxx)+", Min: "+str(minn))
    return minn + maxx

def GetFirstInvalid(lines,preamble):
    for idx in range(preamble,len(lines)):
        valid = CheckVailidity(lines[idx],lines[idx-preamble:idx])
        if(not valid):
            return lines[idx]
    return -1

def FindEncryptWeakness(lines,preamble):
    num = GetFirstInvalid(lines,preamble)
    print("Invalid number: "+str(num))
    for idx in range(len(lines)):
        total = lines[idx]
        if(total == num):
            continue
        for nidx in range(idx+1,len(lines)):
            if(total < num):
                total += lines[nidx]
            else:
                break
        if(total == num):
            return AddLargestAndSmallest(lines[idx:nidx])
    return -1

lines = ReadInputFile()
lines = [int(line) for line in lines]
# print(str(GetFirstInvalid(lines,25)))     # First try was golden!
print(str(FindEncryptWeakness(lines,25)))   # First try was golden!