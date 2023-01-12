from ReadFile import *

class Ship:
    def __init__(self,ver):
        self.version = ver
        self.east = 0
        self.north = 0
        self.face = 0
        self.weast = 10     # Waypoint distance relative to ship
        self.wnorth = 1
        self.turns = ['E','S','W','N']
    def TurnRight(self,deg):
        idx = int(deg/90)
        if(self.version == 1): 
            self.face = (self.face + idx) % 4
        else:
            we = self.weast
            wn = self.wnorth
            if(idx == 1):
                self.weast = wn
                self.wnorth = -we
            elif(idx == 2):
                self.weast = -we
                self.wnorth = -wn
            elif(idx == 3):
                self.weast = -wn
                self.wnorth = we
    def TurnLeft(self,deg):
        idx = int(deg/90)
        if(self.version == 1):
            self.face = (self.face - idx) % 4
        else:
            we = self.weast
            wn = self.wnorth
            if(idx == 3):
                self.weast = wn
                self.wnorth = -we
            elif(idx == 2):
                self.weast = -we
                self.wnorth = -wn
            elif(idx == 1):
                self.weast = -wn
                self.wnorth = we
    def Forward(self,units):
        if(self.version == 1):
            curDir = self.turns[self.face]
            if(curDir == "E"):
                self.east += units
            elif(curDir == "S"):
                self.north -= units
            elif(curDir == "W"):
                self.east -= units
            elif(curDir == "N"):
                self.north += units
        else:
            self.east += units * self.weast
            self.north += units * self.wnorth
    def East(self,units):
        if(self.version == 1):
            self.east += units
        else:
            self.weast += units
    def South(self,units):
        if(self.version == 1):
            self.north -= units
        else:
            self.wnorth -= units
    def West(self,units):
        if(self.version == 1):
            self.east -= units
        else:
            self.weast -= units
    def North(self,units):
        if(self.version == 1):
            self.north += units
        else:
            self.wnorth += units
    def ManDis(self):
        return abs(self.east) + abs(self.north)
    def Print(self):
        print("Ship loc: " + str(self.east) + " east, " + str(self.north) + " north")
        if(self.version != 1):
            print("   Waypoint loc: " + str(self.weast) + " east, " + str(self.wnorth) + " north")

def ParseSteps(steps,ver):
    ship = Ship(ver)
    for i in range(len(steps)):
        letter = steps[i][0]
        num = int(steps[i][1:])
        if(letter == "F"):
            ship.Forward(num)
        elif(letter == "R"):
            ship.TurnRight(num)
        elif(letter == "L"):
            ship.TurnLeft(num)
        elif(letter == "N"):
            ship.North(num)
        elif(letter == "E"):
            ship.East(num)
        elif(letter == "S"):
            ship.South(num)
        elif(letter == "W"):
            ship.West(num)
        ship.Print()
    return ship.ManDis()

steps = ReadInputFile()
steps = StripNewLines(steps)
# print(str(ParseSteps(steps,1)))
print(str(ParseSteps(steps,2)))

# Guesses:
# 18321 - too low
