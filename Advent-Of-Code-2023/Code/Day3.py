from Load import LoadFile

def main():
    input = LoadFile("Test3")
    part1(input)
    part2(input)

def part1(input):
    findNumber(input)
    print()
    
def part2(input):
    print()

def findNumber(grid):
    total = 0
    for y,line in enumerate(grid):
        numStr = ""
        for x,char in enumerate(line):
            if char.isdigit():
                numStr+=char
            elif numStr.count > 0:
                if checkIfNearSymbol(x, y, numStr.count, grid):
                    total+=int(numStr)
                numStr = ""
    print(total)

def checkIfNearSymbol(x,y,len,grid):
    #Check above
    str=""
    if y > 0:
        for char in grid[y-1][x-1:x+len]:
            if isSymbol(char): return True

    #Check adjacent
    if isSymbol(grid[y][x-1]): return True
    if isSymbol(grid[y][x+len]): return True

    #Check below
    for char in grid[y+1][x-1:x+len]:
        if isSymbol(char): return True
    
    return False

def isSymbol(char):
    return char.isSymbol() and char != '.'

if __name__ == "__main__":
    main()