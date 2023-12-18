import os, sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),"../../"))
from ReadFile import *

# Rock     = A, X = 1
# Paper    = B, Y = 2
# Scissors = C, Z = 3
# Win  = 6
# Draw = 3
# Loss = 0
xyz_code_1 = {"X":1, "Y":2, "Z":3}  # Rock, Paper, Scissors
xyz_code_2 = {"X":0, "Y":3, "Z":6}  # Lose, draw, win
winnings = {
    "A X":3, "A Y":6, "A Z":0,
    "B X":0, "B Y":3, "B Z":6,
    "C X":6, "C Y":0, "C Z":3,
}
how_to = {
    # "A X":3, "A Y":6, "A Z":0,
    # "B X":0, "B Y":3, "B Z":6,
    # "C X":6, "C Y":0, "C Z":3,
}

rounds = StripNewLines(ReadInputFile())
score1 = 0
for round in rounds:
    score1 += xyz_code_1[round[2]] + winnings[round]

score2 = 0
for round in rounds:
    score2 += 0
    
print("Total end score method 1: " + str(score1))
print("Total end score method 2: " + str(score2))



