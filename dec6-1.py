
def check_dublet(text):
    num_of_char = 0
    for char in text:
        num_of_char += testtext.count(char)
    if num_of_char == len(testtext):
        return "no_dublet"
    else:
        return ""
        
    
char_nr = int(input("How many destingt char do you seek for? "))
with open('radiocode.txt') as f:
    for char in f:
        radiocode += char
    testtext = radiocode[0:char_nr]
    for char in radiocode:
        if check_dublet(testtext) == "no_dublet":
            print("last chareter was number " + str(char_nr))
            break
        else:
            testtext = testtext[1:]
            testtext += radiocode[char_nr]
            char_nr += 1

