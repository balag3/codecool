import curses
import time
import math
import random


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)


max_y,max_x = stdscr.getmaxyx()

y=2

string_list = "abcdefghijklmnopqrstuvwxyz"
choosen_one = string_list[random.randint(0,25)]

x = random.randint(12,max_x-2)


score = 0
difficulity = 0.4
rain = "~"*(max_x-1)



def fall():
    global y
    stdscr.addstr(y,x,str(choosen_one.upper()))
    stdscr.move(y-1,0)
    #stdscr.clrtoeol()
    y += 1
    stdscr.refresh()



running = True
while running:
    stdscr.addstr(1,1,rain)
    stdscr.addstr(2,1,'Score: %s' %(score))
    time.sleep(difficulity)
    stdscr.border(0)
    fall()
    key = stdscr.getch()
    stdscr.timeout(3)
    if key == ord(choosen_one):
         y = 2
         x = random.randint(12,max_x-2)
         choosen_one = string_list[random.randint(0,25)]
         stdscr.erase()
         score += 1
    if score > 5:
        difficulity = 0.3
    if score > 10:
        difficulity = 0.25
    if score > 15:
        difficulity = 0.2
    if score > 20:
        difficulity = 0.15
    if score > 25:
        difficulity = 0.10
    if score > 30:
        difficulity = 0.075

    if y == max_y -1 :
        stdscr.refresh()
        stdscr.addstr(int(max_y/2),int(max_x/2),'You LOST!')
        running = False
stdscr.getch()
curses.endwin()
