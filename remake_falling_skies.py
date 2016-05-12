import curses
import time
import math
import random


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)


#stdscr.nodelay(1)

############################################################################
############################### VARIABLES ##################################
############################################################################


################### setting the max y and the max x coordinates #############
max_y,max_x = stdscr.getmaxyx()

####################### setting the string list #############################
string_list = "abcdefghijklmnopqrstuvwxyz"

############## get a random letter from the string list #######################
chosen_one = string_list[random.randint(0,25)]

### get a random x and a fixed y coordinate where the letter will fall from ####
x_fall = random.randint(12,max_x-10)
y_fall = 2

### setting life,scrore and difficulty(difficulty the smaller the harder) ######
life = 3
score = 0
difficulty = 0.4
new_level = 10
level = 1

####################### animation ##############################################
rain = "☢ "*(max_x-1)
earth = "⏏_"*(max_x-2)



###############################################################################
############################## FUNCTIONS ######################################
###############################################################################



############################ falling letter function ##########################
def fall():
    global y_fall
    stdscr.addstr(y_fall,x_fall,str("☣ " + chosen_one.upper()) + "☣")
    y_fall += 1
    stdscr.refresh()


############################# INTRO screen #################################
def intro():
    intro_line1 = "POLLUTION AND WARS HAVE DESTROYED OUR PLANET."
    intro_line2 = "THE LAST REMAINING MEMBERS OF HUMANITY"
    intro_line3 = "HAVE TO FACE DEADLY ACID RAINS"
    intro_line4 = "FALLING FROM THE POISONOUS SKY."
    intro_line5 = "HELP PEOPLE ESCAPE FROM THE RAIN BY"
    intro_line6 = "PRESSING THE SAME LETTER THAT YOU SEE IN THE RAINDROPS!"
    intro_line7 = "Press ANY key to start"
    stdscr.addstr(int(6), int(max_x/7), intro_line1)
    stdscr.addstr(int(7), int(max_x/7), intro_line2)
    stdscr.addstr(int(8), int(max_x/7), intro_line3)
    stdscr.addstr(int(9), int(max_x/7), intro_line4)
    stdscr.addstr(int(10), int(max_x/7), intro_line5)
    stdscr.addstr(int(11), int(max_x/7), intro_line6)
    stdscr.addstr(int(14), int(max_x/7), intro_line7, curses.A_STANDOUT)
    stdscr.getch()
    stdscr.nodelay(1)



############# environment and stage drawing function ##########################
def environment():
    stdscr.addstr(1,1,rain)
    stdscr.addstr(max_y-2,1,earth)
    stdscr.addstr(4,1,'SCORE: ✎ %s' %(score))
    stdscr.addstr(6,1,'LIFE: ♥ %s' %(life))
    stdscr.addstr(8,1,'LEVEL: ⚔ %s' %(level))
    stdscr.border(0)


################ screen update + timeout function which lets the other functions
#running while listening to keystrokes ########################################
def clear():
    stdscr.timeout(1)
    stdscr.refresh()
#comment out stdscr.erase() to to let the letter draw a line for better visibility
    stdscr.erase()


############### broadcast a new starting position of the falling letter #######
def broadcast():
    global y_fall
    y_fall= 2
    global x_fall
    x_fall = random.randint(12,max_x-10)
    global chosen_one
    chosen_one = string_list[random.randint(0,25)]

##############################################################################
##################### MAIN function ##########################################
###############################################################################
def main():
    running = True
    while running:
        global score
        global life
        global difficulty
        global chosen_one
        global rain
        global earth
        global y_fall
        global x_fall
        global new_level
        global level
        environment()
        fall()
        time.sleep(difficulty)
        key = stdscr.getch()
        clear()
### if keystroke is correct resets the falling letter and updates the score ###
        if key == ord(chosen_one):
             broadcast()
             stdscr.erase()
             score += 1
#### level up and difficulity beahviour #######################################
        if score == new_level:
            new_level += 10
            difficulty -= 0.025
            level += 1
        if score == new_level and score > 90:
            new_level += 15
            difficulty -= 0.005
            level += 1
###### if a drop hits the ground life decreases and resets the falling letter ##
        if y_fall == max_y -1 :
            broadcast()
            stdscr.erase()
            life -= 1
###### if you die you can choose to quit or restart ###########################
        if life == 0:
            running = False
    while True:
        environment()
        stdscr.addstr(int(max_y/2)-5,int(max_x/2-13), "YOUR FINAL SCORE IS : %s" %(score))
        stdscr.addstr(int(max_y/2),int(max_x/2-10),"PRESS 'Q' TO QUIT")
        stdscr.addstr(int(max_y/2)+5,int(max_x/2-12),"PRESS 'R' TO RESTART")
        key = stdscr.getch()
        stdscr.timeout(-1)
        if key == ord("q"):
            break
        if key == ord("r"):
            y_fall= 2
            x_fall = random.randint(12,max_x-10)
            chosen_one = string_list[random.randint(0,25)]
            stdscr.erase()
            life = 3
            score = 0
            difficulty = 0.4
            main()
    curses.endwin()

intro()
main()



# name = ""
# x = int(max_x/7)
# y = 18
# stdscr.move(y, x)
# run = True
# while run:
#     key = stdscr.getch()
#     name = name[::] + chr(key)
#     stdscr.addstr(chr(key).upper())
#     stdscr.move(y, x+1)
#     x = x+1
#     if len(name) == 3:
#         run = False
#         stdscr.nodelay(1)
