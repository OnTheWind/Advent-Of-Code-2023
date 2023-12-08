from Load import LoadFile

def main():
    input = LoadFile("Day3")
    part1(input)
    part2(input)

def part1(input):
    findNumber(input)
    
def part2(grid):
    gears = []
    numbers = {}
    for y,line in enumerate(grid):
        numbers[y] = []
        numStr = ""
        lastMatchX = 0
        for x,char in enumerate(line):
            if char.isdigit():
                if numStr == "":
                    lastMatchX = x
                numStr+=char
            elif numStr != "":
                numbers[y].append({"num": numStr, "left": lastMatchX, "right": lastMatchX + len(numStr) - 1})
                numStr = ""
            if char == "*":
                gears.append({ "x": x, "y": y })
        if numStr == "":
            lastMatchX = x
            numStr+=char
        elif numStr != "":
            numbers[y].append({"num": numStr, "left": lastMatchX, "right": lastMatchX + len(numStr) - 1})
            numStr = ""
    total=0
    for gear in gears:
        total+=getGearRatio(gear,numbers)
    print(total)
        
def getGearRatio(gear,numbers):
    matches = []
    y = gear["y"]
    x = gear["x"]
    if y > 0:
        matches.extend(getAdjacentNums(x,numbers[y-1]))
    matches.extend(getAdjacentNums(x,numbers[y]))
    if y+1 < len(numbers):
        matches.extend(getAdjacentNums(x,numbers[y+1]))
    if len(matches)==2:
        return matches[0]*matches[1]
    return 0

def getAdjacentNums(x, numbers):
    result = []
    for number in numbers:
        if number["left"] <= x+1 and number["right"] >= x-1:
            result.append(int(number["num"]))
    return result


def findNumber(grid):
    all = {}
    #numbers = {}
    count = 0
    for y,line in enumerate(grid):
        numStr = ""
        lastMatchX = 0
        for x,char in enumerate(line):
            if char.isdigit():
                if numStr == "":
                    lastMatchX = x
                numStr+=char
            elif numStr != "":
                if checkIfNearSymbol(lastMatchX, y, len(numStr), grid):
                    count+=int(numStr)
                    #numbers[int(numStr)]=1
                else:
                    all[int(numStr)]=1
                numStr = ""
        if numStr != "" and checkIfNearSymbol(lastMatchX, y, len(numStr), grid):
             #numbers[int(numStr)]=1
             count+=int(numStr)
    print("dups:",count)

def checkIfNearSymbol(x,y,length,grid):
    left=max(x-1,0)
    right=min(x+length, len(grid[y]))+1
    #Check above
    str=""
    if y > 0:
        for char in grid[y-1][left:right]:
            if isSymbol(char):
                #print(grid[y][left+1:right-1],"^",grid[y-1][left:right])
                return True

    #Check adjacent
    if x > 0 and isSymbol(grid[y][x-1]):
        #print(grid[y][left+1:right-1],"<",grid[y][x-1])
        return True
    if x + length < len(grid[y]) and isSymbol(grid[y][x+length]):
        #print(grid[y][left+1:right-1],">",grid[y][x+length])
        return True

    #Check below
    if y < len(grid) - 1:
        for char in grid[y+1][left:right]:
            if isSymbol(char):
                #print(grid[y][left+1:right-1],"v",grid[y+1][left:right])
                return True
    
    return False

def isSymbol(char):
    return not char.isdigit() and char != '.' and char !='\n'

if __name__ == "__main__":
    main()

#bad: 520625
#     331209
