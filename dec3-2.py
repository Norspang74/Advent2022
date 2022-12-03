elf_1_items = []
elf_2_items = []
elf_3_items = []
sum=0
elf=0
with open('rucksack.txt') as f:
    line_number = 0
    for line in f.readlines():
        line_number += 1
        num_of_items = int((len(line) - (len(line)%2)))
        elf += 1
        for item in range(0, num_of_items):
            elf_1_items.append(line[item]) if elf == 1 else False
            elf_2_items.append(line[item]) if elf == 2 else False
            elf_3_items.append(line[item]) if elf == 3 else False
        if elf == 3:
            for letter in elf_1_items:
                if letter in elf_2_items and letter in elf_3_items:
                    add = ord(letter)
                    if add > 95:
                        sum += (add-96)
                        break
                    elif add <91:
                        sum += (add-38)
                        break
            elf = 0
            print("you are on line", line_number)
            print("the letter is ",letter,"ASCII number ", ord(letter))
            print("Total sum is ",sum)
            elf_1_items = []
            elf_2_items = []
            elf_3_items = []
            
        

                