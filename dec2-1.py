with open('RPS.txt') as f:
    sum=0
    sum2=0
    for line in f.readlines():
        if line[0] == "A" and line[2] == "X":
            sum += 4
            sum2 += 3
        elif line[0] == "A" and line[2] == "Y":
            sum += 8
            sum2 += 4
        elif line[0] == "A" and line[2] == "Z":
            sum += 3
            sum2 += 8
        elif line[0] == "B" and line[2] == "X":
            sum += 1
            sum2 += 1
        elif line[0] == "B" and line[2] == "Y":
            sum += 5
            sum2 += 5
        elif line[0] == "B" and line[2] == "Z":
            sum += 9
            sum2 += 9
        elif line[0] == "C" and line[2] == "X":
            sum += 7
            sum2 += 2
        elif line[0] == "C" and line[2] == "Y":
            sum += 2
            sum2 += 6
        elif line[0] == "C" and line[2] == "Z":
            sum += 6
            sum2 += 7
        else:
            sum += 0
print(sum)
print(sum2)
           