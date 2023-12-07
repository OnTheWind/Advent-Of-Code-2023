def LoadFile(filename):
    output = []
    f = open("./Resources/"+filename+".txt")
    for line in f:
        output.append(line)
    return output