import os, sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"../../"))
from ReadFile import *

content = ReadInputFile()
elf_cals = []
my_sum = 0
for line in content:
    if line != "\n":
        my_sum += int(line)
    else:
        elf_cals.append(my_sum)
        my_sum = 0
        # print(elf_cals)

my_maxes = [0,0,0]
for cal in elf_cals:
    if cal > my_maxes[0]:
        my_maxes[2] = my_maxes[1]
        my_maxes[1] = my_maxes[0]
        my_maxes[0] = cal
    elif cal > my_maxes[1]:
        my_maxes[2] = my_maxes[1]
        my_maxes[1] = cal
    elif cal > my_maxes[2]:
        my_maxes[2] = cal
        
        
print("Max three calories:\t" + str(my_maxes[0]) + "\t" + str(my_maxes[1]) + "\t" + str(my_maxes[2]))
print("Sum of three maxes: " + str(my_maxes[0] + my_maxes[1] + my_maxes[2]))

