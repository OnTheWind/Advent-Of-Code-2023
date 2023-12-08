import math
from Load import LoadFile

TIME=0
DIST=1

def main():
    #input = LoadFile("Test6")
    input= LoadFile("Day6")
    part1(input)
    part2(input)

def part1(input):
    wins = []
    for race in parseInput(input):
        wins.append(winCounts(race))
    print(wins)
    print(math.prod(wins))
    
def part2(input):
    race=(collapseLine(input[0]),collapseLine(input[1]))
    print(winCounts(race))

def collapseLine(line: str):
    return int(line[line.index(':')+1:].replace(" ","").strip())

def winCounts(race: tuple):
    return maxHold(race)-minHold(race)+1

def maxHold(race: tuple):
    return math.floor((race[TIME]+math.sqrt(pow(race[TIME],2)-4*(race[DIST]+1)))/2)

def minHold(race: tuple):
    return math.ceil((race[TIME]-math.sqrt(pow(race[TIME],2)-4*(race[DIST]+1)))/2)

def parseInput(input):
    return list(zip(parseLine(input[0]), parseLine(input[1])))

def parseLine(line):
    return [int(k) for k in line.strip().split(" ") if k.isnumeric()]

if __name__ == "__main__":
    main()