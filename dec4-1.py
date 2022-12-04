import re
data = []


# Split text into list
with open('cleanup.txt') as f:
    for line in f.readlines():
        data.append(re.split('-|,',line.strip()))


# Find where one Elf's task FULLY CONTAINS the other Elf' tasks 
def fully_contained_pairs():
    sum=0
    for line in range(0,len(data)):
        elf_1_start=int(data[line][0])
        elf_1_end=int(data[line][1])
        elf_2_start=int(data[line][2])
        elf_2_end=int(data[line][3])
        if elf_1_start >= elf_2_start and elf_1_end <= elf_2_end:
            sum += 1
        elif elf_1_start <= elf_2_start and elf_1_end >= elf_2_end:
            sum += 1
    return sum


# Find where one Elf's task OVERLAP the other Elf' tasks 
def overlapping_pairs():
    sum=0
    for line in range(0,len(data)):
        elf_1_start=int(data[line][0])
        elf_1_end=int(data[line][1])
        elf_2_start=int(data[line][2])
        elf_2_end=int(data[line][3])
        if elf_1_start >= elf_2_start and elf_1_start <= elf_2_end:
            sum += 1
        elif elf_2_start >= elf_1_start and elf_2_start <= elf_1_end:
            sum += 1
    return sum


# Now, Do the math, and show me the result
print(fully_contained_pairs()," Elf's tasks fully contains the other Elf' task in the pair")
print(overlapping_pairs()," Elf's in total have overlaping tasks within the pair")