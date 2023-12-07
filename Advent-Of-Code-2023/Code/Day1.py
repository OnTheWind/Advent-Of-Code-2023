from Load import LoadFile

WORD_TO_NUMBER_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def main():
    input = LoadFile("Day1")
    part1(input)
    part2(input)

def part1(input):
    total = 0
    for line in input:
        numStr = ""
        for char in line:
            if(char.isdigit()):
                numStr+=char
                break
        for char in reversed(line):
            if(char.isdigit()):
                numStr+=char
                break
        total = total + int(numStr)
    print(total)

def part2(input):
    total = 0
    for line in input:
        total+=getFirstNum(line)*10+getFirstNum(line, 1)
    print(total)

def getFirstNum(line, reverse = 0):
    string = line[::-1] if(reverse) else line
    for i, char in enumerate(string):
        if(char.isdigit()):
            return int(char)
        sub = string[i:]
        for word in WORD_TO_NUMBER_MAP:
            compare = word[::-1] if reverse else word
            if (sub.startswith(compare)):
                return WORD_TO_NUMBER_MAP[word]
 

if __name__ == "__main__":
    main()