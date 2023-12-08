from Load import LoadFile

START = 0
END = 1
OFFSET = 2

def main():
    #input = LoadFile("Test5")
    input= LoadFile("Day5")
    part1(input)
    part2(input)

def part1(input):
    output = { "seeds": parseSeeds(input[0]), "mapping": parseMapping(input)}
    locations = []
    for seed in output["seeds"]:
        curNum = seed
        for mapping in output["mapping"]:
            curNum = mapOne(curNum, mapping)
        locations.append(curNum)
    print(min(locations))
    
def part2(input):
    output = { "seeds": parseSeeds(input[0]), "mapping": parseMapping(input)}
    ranges = []
    for x,start in enumerate(output["seeds"][::2]):
        count = output["seeds"][2*x+1]
        ranges.append((start, start+count+1))
    
    for mapping in output["mapping"]:
        ranges=mapRanges(ranges,mapping)
    print(ranges[0][START])

def mapRanges(seedRanges, mapping):
    outputRanges = []
    for range in seedRanges:
        tempRange = range
        for map in mapping:
            #save off any of the temp range that falls before the map starts
            if tempRange[START]<map[START]:
                end=min(tempRange[END],map[START]-1)
                outputRanges.append((tempRange[START],end))
                tempRange=(end+1, tempRange[END])
            #break if tempRange consumed
            if tempRange[START]>tempRange[END]:
                break
            #transform and save off any of the temp range that falls during the map
            if tempRange[START]<=map[END]:
                end=min(tempRange[END],map[END])
                outputRanges.append((tempRange[START]+map[OFFSET],end+map[OFFSET]))
                tempRange=(end+1, tempRange[END])
            #break if tempRange consumed
            if tempRange[START]>tempRange[END]:
                break
        #save off any temp range that is left over after exhausting maps
        if tempRange[START]<=tempRange[END]:
            outputRanges.append(tempRange)
    outputRanges.sort(key=lambda a : a[START])
    return outputRanges


def parseSeeds(line):
    return [int(k) for k in line.strip().split(" ") if k.isnumeric()]

def parseMapping(input):
    allMappings = []
    mapping = []
    for line in input[1:]:
        if len(line.strip()) == 0: continue
        if "map:" in line:
            if len(mapping) > 0:
                mapping.sort(key=lambda a : a[START])
                allMappings.append(mapping)
                mapping = []
        else:
            mapping.append(parseMappingLine(line))
    #append the last mapping
    if len(mapping) > 0:
        mapping.sort(key=lambda a : a[START])
        allMappings.append(mapping)
    return allMappings

def parseMappingLine(line):
    [dest, source, length] = line.strip().split(" ")
    return (int(source), int(source) + int(length) - 1, int(dest) - int(source))

def mapOne(sourceNum, mapping):
    for map in mapping:
        if sourceNum < map[START]: return sourceNum
        if sourceNum <= map[END]: return sourceNum + map[OFFSET]
    return sourceNum

if __name__ == "__main__":
    main()