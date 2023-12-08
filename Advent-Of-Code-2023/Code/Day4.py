from Load import LoadFile

def main():
    input = LoadFile("Day4")
    part1(input)
    part2(input)

def part1(input):
    print(sum(int(pow(2,getNumWins(parseLine(line))-1)) for line in input))
    
def part2(input):
    cards = [1 for k in input]
    for n,line in enumerate(input):
        wins = getNumWins(parseLine(line))
        #Add new cards to the next number of cards equal to the count of this card
        for i in range(n+1,n+wins+1):
            cards[i]+=cards[n]
    print(sum(cards))


def parseLine(line: str):
    [left, right] = line[line.index(':')+1:].strip().split(" | ")
    return { "winning": {k:1 for k in left.split(" ") if k.isnumeric()}, "nums": [k for k in right.split(" ") if k.isnumeric()]}

def getNumWins(scratchCard):
    return sum(1 for v in scratchCard["nums"] if v in scratchCard["winning"])

if __name__ == "__main__":
    main()