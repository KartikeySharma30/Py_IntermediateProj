# So this Program let's you to Test your Speed of typing over some random sentences 



import curses #it helps us print stuff out onto the terminal window -> with more power then just the print() statment 
from curses import wrapper # Wrapper wraps all that stuff together so they can be seen as one onto the screen while running 
import time
import random



def strt_scr(stdscr):
    stdscr.clear()
    #addstr(pos-y,pos-x,str,colorpair)
    stdscr.addstr("Welcome to the WPM Test!")  # curses.color_pair(2)) # Here we are referenceing to choose from which color to pick
    stdscr.addstr("\nPress Any Key to Begin!")
    stdscr.refresh()
    stdscr.getkey() # Help to wait for the user to typein then closes the program


# Helps us to display all the text and typing onto the screen 
def display_txt(stdscr, target,current,wpm=0):
    stdscr.addstr(target)  
    stdscr.addstr(1,0,f"WPM:{wpm}")  
    for i,char in enumerate(current):
        correctchar=target[i]
        color = curses.color_pair(1)
        if char!=correctchar:
            color = curses.color_pair(2)
        stdscr.addstr(0,i,char,color)

#Taking Out Text from a text file -> which can also be created depending upon one's need
def load_text():
    with open("/Users/kartikeysharma/Desktop/Hanuman/Projects/Pojects/text.txt","r") as f:
        lines=f.readlines()
        return random.choice(lines).strip()


# Calculating the Speed of the User and Letting it know wheather user following the sentence correctly or not
# by showing the typings of user in GREEN color - if correct and RED color - if WRONG
# and Allow user to delete that upon clicking backspace 
def wpm_test(stdscr):
    target_txt = load_text()
    current_txt = []
    wpm=0
    strt=time.time()
    stdscr.nodelay(True)
    while True:
        timeel=max(time.time()-strt,1)
        wpm = round((len(current_txt)/(timeel/60))/5)
        stdscr.clear()
        display_txt(stdscr,target_txt,current_txt,wpm)
        stdscr.refresh()

        if "".join(current_txt)==target_txt:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key)==27:
            break
        
        if key in ("KEY_BACKSPACE",'\b',"\x7f"):
            if len(current_txt)>0:
                current_txt.pop()

        elif len(current_txt) < len(target_txt):
            current_txt.append(key)
    



#Main
def main(stdscr): # stdscr -> standard screen -> ie is terminal screen
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE,curses.COLOR_BLACK)
    
    strt_scr(stdscr)
    while True:
        wpm_test(stdscr)
        stdscr.addstr(2,0,"You Have Completed the Test Press any Key to Continue ")
        key = stdscr.getkey() 
        if ord(key)==27:
            break
wrapper(main) # wrapper is a function which helps in calling the other function while initialzing the curses Module
 
