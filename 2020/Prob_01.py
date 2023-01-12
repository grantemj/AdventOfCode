from ReadFile import *

def Sum2_FindIndexes(lines):
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            total = int(lines[i]) + int(lines[j])
            if (total == 2020):
                return (i,j,total)
            
def Sum3_FindIndexes(lines):
    for i in range(len(lines)-2):
        for j in range(i+1, len(lines)-1):
            for k in range(j+1, len(lines)):
                total = int(lines[i]) + int(lines[j]) + int(lines[k])
                if (total == 2020):
                    return (i,j,k,total)
            
def Find2020Sum():
    lines = ReadInputFile()
    i,j,total = Sum2_FindIndexes(lines)
    product = int(lines[i]) * int(lines[j])
    print ("Two numbers were: "+lines[i]+" and "+lines[j])
    print (lines[i] + " + " + lines[j] + " = " + str(total))
    print (lines[i] + " * " + lines[j] + " = " + str(product))
    
def Find2020Sum_3():
    lines = ReadInputFile()
    i,j,k,total = Sum3_FindIndexes(lines)
    product = int(lines[i]) * int(lines[j]) * int(lines[k])
    print ("Three numbers were: "+lines[i]+", "+lines[j]+", and "+lines[k])
    print (lines[i] + " + " + lines[j] + " + " + lines[k] + " = " + str(total))
    print (lines[i] + " * " + lines[j] + " * " + lines[k] + " = " + str(product))
    
Find2020Sum_3()
