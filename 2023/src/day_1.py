import os, sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"../../"))
from ReadFile import *
        
def GetFirstAndLastDigitDigit(line):
    first_dig = ('',-1)
    last_dig = ('',-1)
    for i in range(len(line)):
        if line[i].isdigit():
            if first_dig[0] == '':
                first_dig = (line[i], i)
            else:
                last_dig = (line[i], i)
    return first_dig, last_dig

def GetFirstAndLastStringDigit(line):
    digits = {"one":'1', "two":'2', "three":'3', "four":'4', "five":'5',
              "six":'6', "seven":'7', "eight":'8', "nine":'9'}
    first_dig = ('',-1)
    last_dig = ('',-1)
    for key in digits.keys():
        ind = line.find(key)
        if ind == -1:
            continue
        if ind < first_dig[1] or first_dig[1] == -1:
            first_dig = (digits[key], ind)
        ind = line.rfind(key)
        if ind > last_dig[1]:
            last_dig = (digits[key], ind)        
    return first_dig, last_dig

def GetListOfCalibrationValues_1(lines):
    cal_vals = []
    for line in lines:
        new_entry = ''
        first_dig, last_dig = GetFirstAndLastDigitDigit(line)
        if last_dig[0] == '':
            new_entry = first_dig[0] + first_dig[0]
        else:
            new_entry = first_dig[0] + last_dig[0]
        cal_vals += [int(new_entry)]
    return cal_vals

def GetListOfCalibrationValues_2(lines):
    cal_vals = []
    for line in lines:
        new_entry = ''
        first_dig_dig, last_dig_dig = GetFirstAndLastDigitDigit(line)
        first_str_dig, last_str_dig = GetFirstAndLastStringDigit(line)
        if last_dig_dig[0] == '':
            last_dig_dig = first_dig_dig
        if last_str_dig[0] == '':
            last_str_dig = first_str_dig
        # Check which one is earlier
        if (first_dig_dig[1] < first_str_dig[1] and first_dig_dig[1] != -1) or first_str_dig[1] == -1:
            new_entry = first_dig_dig[0]
        else:
            new_entry = first_str_dig[0]
        # Check which one is latest
        if last_dig_dig[1] > last_str_dig[1] and last_dig_dig[1] != -1:
            new_entry += last_dig_dig[0]
        else:
            new_entry += last_str_dig[0]
        cal_vals += [int(new_entry)]
    return cal_vals

def GetListSum(vals):
    sum = 0
    for val in vals:
        sum += val
    return sum
        
# ================================================================== #

lines = StripNewLines(ReadInputFile())
cal_vals_1 = GetListOfCalibrationValues_1(lines)
cal_vals_2 = GetListOfCalibrationValues_2(lines)
print("Answer of Day 1 Part 1 = ", GetListSum(cal_vals_1))
print("Answer of Day 1 Part 2 = ", GetListSum(cal_vals_2))