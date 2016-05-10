
##########################################################################
##### This script expects a txt file to save to and load from. ###########
##########################################################################

my_file = 'todo.txt'

##########################################################################
###### File operations to load/save/clear the existing work ##############
##########################################################################

def load():
    with open(my_file) as myfile:
        lines =  [line.rstrip('\n') for line in open(my_file)]
        for i in lines:
            to_do.append(i)
        return to_do

def write(line):
    with open(my_file, mode='a') as myfile:
        myfile.write(line +'\n')

def save():
    for i in range (0,len(to_do)):
        lines = str(to_do[i])
        write(lines)

def clear():
    with open(my_file, 'w'): pass

###########################################################################
###### In-app operations to update the current to do list #################
###########################################################################

def add():
    answer = input(" Add an item: ")
    to_do.append("[ ]" + answer)
    print( " Item added.")

def lista():
    print (" You saved the following to-do items: ")
    line = 1
    for i in to_do:
        print (line,'.',i)
        line += 1

def mark():
    lista()
    print('\n')
    try:
        answer = input(" Which one you want to mark as completed?:")
        index = int(answer)-1
        word_to_edit = to_do[index]
        updated_word = word_to_edit[:1] + "x" + word_to_edit[2:]
        to_do[index] = updated_word
        print(updated_word[3:] + " is completed.")
    except  ValueError:
        return mark()


def archive():
    for i in to_do:
        if i[1] == 'x':
            to_do.remove(i)
    print (" All completed tasks got deleted.")

###########################################################################
###################### Start the program ##################################
###########################################################################

while True:
    first_message = str(input(" Please specify a command [list, add, mark, archive] :")).lower()
    print('\n')
    valid_commands = ['list', 'add', 'mark', 'archive']

    to_do = []

    load()


    if first_message not in valid_commands:
        exit()
    elif first_message == "add":
        add()
        print('\n')
    elif first_message == "list":
        lista()
        print('\n')
    elif first_message == "mark":
        mark()
        print('\n')
        lista()
        print('\n')
    elif first_message == "archive":
        archive()
        print('\n')



    clear()

    save()

    to_do = []
