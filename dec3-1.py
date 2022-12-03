rucksack_first_compartment_items = []
rucksack_second_compartment_items = []
mistake_item =[]
sum=0
with open('rucksack.txt') as f:
    line_number = 0
    for line in f.readlines():
        num_of_items = int((len(line) - (len(line)%2)))
        num_of_items_in_compartment = int(num_of_items / 2) 
        for item in range(0, num_of_items_in_compartment):
            rucksack_first_compartment_items.append(line[item])
        
        for item in range(num_of_items_in_compartment, num_of_items):
            rucksack_second_compartment_items.append(line[item])
        
        for item in rucksack_first_compartment_items:
            if item in rucksack_second_compartment_items:
                mistake_item.append(item)
                add = ord(item)
                if add > 95:
                    sum += (add-96)
                else:
                    sum += (add-38)
                break
        
        rucksack_first_compartment_items = []
        rucksack_second_compartment_items = []
        print(sum)
        