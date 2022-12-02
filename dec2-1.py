with open('RPS.txt') as f:
    sum=0
    for line in f.readlines():
        if line[0] == "A" and line[2] == "X":
            sum += 4
        elif line[0] == "A" and line[2] == "Y":
            sum += 8
        elif line[0] == "A" and line[2] == "Z":
            sum += 3
        elif line[0] == "B" and line[2] == "X":
            sum += 1
        elif line[0] == "B" and line[2] == "Y":
            sum += 5
        elif line[0] == "B" and line[2] == "Z":
            sum += 9
        elif line[0] == "C" and line[2] == "X":
            sum += 7
        elif line[0] == "C" and line[2] == "Y":
            sum += 2
        elif line[0] == "C" and line[2] == "Z":
            sum += 6
        else:
            sum += 0
        print(line)
print(line)
print(sum)
           