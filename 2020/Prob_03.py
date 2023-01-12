from ReadFile import *

def TraverseMap(pattern):
    treeMap = ReadInputFile()
    height = len(treeMap)
    width = len(treeMap[0])
    index = (0,0)
    totalTrees = 0
    while(index[0] < height-pattern[1]):
        index = ((index[0]+pattern[1]), (index[1]+pattern[0])%(width-1))
        # print(index)
        totalTrees += (treeMap[index[0]][index[1]]=='#')
    return totalTrees

def TraverseEachMap(treeMap,pattern):
    height = len(treeMap)
    width = len(treeMap[0])
    index = (0,0)
    totalTrees = 0
    while(index[0] < height-pattern[1]):
        index = ((index[0]+pattern[1]), (index[1]+pattern[0])%(width-1))
        # print(index)
        totalTrees += (treeMap[index[0]][index[1]]=='#')
    print(totalTrees)
    return totalTrees
    
def TraverseMultipleMaps(patterns):
    treeMap = ReadInputFile()
    total = 1
    for pattern in patterns:
        total *= TraverseEachMap(treeMap,pattern)
        print(total)
    
# TraverseMap((3,1))
TraverseMultipleMaps([(1,1),(3,1),(5,1),(7,1),(1,2)])