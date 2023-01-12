from ReadFile import *

rules = {}

def GetNumOfContainees(bags):
    if(rules[bags[0]] == {}):
        return 0
    total = 0
    for containee in rules[bags[0]]:
        total += rules[bags[0]][containee] * (1 + GetNumOfContainees([containee]))
    return total
    
    
def GetNumOfContainers(bags, counted, searched):
    if(len(bags) == 0):
        return 0
    if(bags[0] in rules):
        total = 0
        nextToSearch = []
        for container in rules[bags[0]]:
            if(container not in counted):
                counted.append(container)
                total += 1
            if(container not in searched):
                searched.append(container)
                nextToSearch.append(container)
        return total + GetNumOfContainers(bags[1:]+nextToSearch,counted,searched)
    else:
        return GetNumOfContainers(bags[1:],counted,searched)


def StoreRules():      # bag : [contained by]
    lines = ReadInputFile()
    for line in lines:
        line = line.split(" contain ")
        if("no other bags" in line[1]):
            continue
        container = line[0].split(" bags")[0]
        containees = line[1].split(", ")
        containees = [" ".join(chunk.split()[1:3]) for chunk in containees]
        for bag in containees:
            if(bag in rules and container not in rules[bag]):
                rules[bag].append(container)
            elif(bag not in rules):
                rules[bag] = [container]
    # print(json.dumps(rules, indent=1))
    return GetNumOfContainers(["shiny gold"],[],[])

def StoreRulesReverse():      # bag : [containing]
    lines = ReadInputFile()
    for line in lines:
        line = line.split(" contain ")
        container = line[0].split(" bags")[0]
        if("no other bags" in line[1]):
            rules[container] = {}
        else:
            containees = line[1].split(", ")
            containees = {" ".join(chunk.split()[1:3]):int(chunk.split()[0]) for chunk in containees}
            print(containees)
            rules[container] = containees
    # print(json.dumps(rules, indent=1))
    return GetNumOfContainees(["shiny gold"])
        
        
# print(str(StoreRules()))
print(str(StoreRulesReverse()))     # Get on first try, hells yeah!