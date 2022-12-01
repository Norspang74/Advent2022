calories_list = []
with open('calories.txt') as f:
    sum=0
    for line in f.readlines():
        if not line =="\n":
            sum+= int(line)
        else:
            calories_list.append(sum)
            sum = 0
    calories_list.sort()
    print(calories_list[-1])