from unusefull_def import clear
from time import sleep
import re
data = []
index_line_number = 0
move =  ""
cratemover9000_stack = ""
cratemover9001_stack = ""


def CrateMover9000(crates,from_stack,to_stack):
    while crates:
        exec("stack" + str(to_stack) +".extend(stack" + str(from_stack) +"[-1:])")
        exec("del stack" + str(from_stack) +"[-1:]")
        crates -= 1
        

def CrateMover9001(crates,from_stack,to_stack):
    crates_to_move = crates
    exec("stack" + str(to_stack) +".extend(stack" + str(from_stack) +"[-" + str(crates_to_move) + ":])")
    exec("del stack" + str(from_stack) +"[-" + str(crates_to_move) + ":]")


# Split text into list
with open('crates.txt') as f:
    file_data = f.readlines()
    line_number = 0
    
    for line in file_data:
        line_length = len(line)
        if line[1]=="1":
            index_line_number=line_number -1 
            number_of_stacks = int((line[len(line)-3]))
            stack_number = number_of_stacks
            line_number -= 1
            max_crates_in_stack = line_number
            while stack_number:
                exec("stack" + str(stack_number) + " = []")
                crate_to_put = "x"
                while not crate_to_put == " " and line_number >=0 :
                    crate_to_put = file_data[int(line_number)][(stack_number*4)-3]
                    if not crate_to_put == " ":
                        exec("stack" + str(stack_number) + ".append('" + crate_to_put + "')")
                    line_number -= 1
                #exec( "print(stack" + str(stack_number) + ")")
                
                stack_number -= 1
                line_number = max_crates_in_stack
            break
        line_number +=1
    
with open('crates.txt') as f:
    crates_to_move = f.readlines()[index_line_number+3:]
#print("***************************")
for line in crates_to_move:
    line = line.strip()
    line = line.strip("move")
    line = line.replace("from", ",")
    line = line.replace("to", ",")
    exec("CrateMover9001(" + line + ")")

stack = 0
while stack < number_of_stacks:
    stack+=1
    exec("cratemover9001_stack += (stack" + str(stack) + "[-1])")
print("with the cratemover9001, the top crates are " + cratemover9001_stack)
    








    