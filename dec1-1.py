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
    print(f"The Elf carying most calories is carying {calories_list[-1]} calories")
    print(f"The top 3 Elf's carying {calories_list[-1] + calories_list[-2] + calories_list[-3]} calories")