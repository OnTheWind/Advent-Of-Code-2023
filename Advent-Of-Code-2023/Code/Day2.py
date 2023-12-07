from Load import LoadFile
from collections import namedtuple

GameObject = namedtuple("GameObject", "num cubes")

def main():
    input = LoadFile("Day2")
    part1(input)
    part2(input)

def part1(input):
    total = 0
    restrictions = { "red": 12, "green": 13, "blue": 14 }
    for game in input:
        gameInfo = parseGame(game)
        if (isGameValid(gameInfo, restrictions)):
            total+=gameInfo["num"]
    print(total)

def part2(input):
    total = 0
    for game in input:
        gameInfo = parseGame(game)
        total += getGamePower(gameInfo)
    print(total)

def parseGame(game: str):
    gameDef = {}
    [definition, sets] = game.split(': ')
    gameDef["num"] = int(definition.lstrip("Game "))
    gameDef["cubes"] = { "red": [], "blue": [], "green": []}
    for set in sets.split('; '):
        for cube in set.split(', '):
            [count, color] = cube.strip().split(' ')
            gameDef["cubes"][color].append(int(count))
    return gameDef

def isGameValid(gameInfo, rest):
    for color in rest:
        for count in gameInfo["cubes"][color]:
            if count > rest[color]:
                return False
    #print(gameInfo["num"])
    return True

def getGamePower(gameInfo):
    power = 1
    for color in gameInfo["cubes"]:
        power = power * max(gameInfo["cubes"][color])
    return power
if __name__ == "__main__":
    main()