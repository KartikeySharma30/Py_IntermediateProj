# This Program helps us to find Shortest Path by dynamically checking the shortest distance between start position
# and the end position by using BFS Algo

# Breadth first Search - BFS Algo

# Curses Help to Display the things onto the screen 
import curses
from curses import wrapper
import queue
import time


maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


# Displaying the Activities that are happening 
def printmaze(maze,stdscr,path=[]):
    BLUE = curses.color_pair(1) 
    RED = curses.color_pair(2)

    for i ,row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)


# Finding the Start of the Maze if multiple chooses the one occuring first
def findstrt(maze,start):
    for i , row in enumerate(maze):
        for j , value in enumerate(row):
            if value == start:
                return i,j
    return None
            

# Here we are finding the Shortest path while keeping in mind the Path which we have already travelled 
def findpath(maze,stdscr):
    start = "O"
    end = "X"
    startpos = findstrt(maze,start)

    q = queue.Queue()
    q.put((startpos,[startpos]))  # Placing the Queue at -> Start Position 
    # The Reason why we are adding 2 element in here is as we want to keep track of the 
    # 1 CURRENT POSITION of the Node 
    # 2 PATH TO GET TO THAT NODE - as we pass through the neighbours we are going to grow that 
    visited = set()
    while not q.empty():
        current_pos,path=q.get()
        row,col = current_pos
        
        stdscr.clear()
        printmaze(maze,stdscr,path)
        time.sleep(0.1)
        stdscr.refresh()
        
        if maze[row][col]==end:
            return path
        
        neighbour = findneighbours(maze,row,col)
        for neigh in neighbour:
            if neigh in visited: 
                continue
            r,c = neigh
            if maze[r][c]=="#":
                continue
            new_path = path + [neigh]
            q.put((neigh,new_path))
            visited.add(neigh)

# Here we are Finding the Neighbours to which we can propagate further 
def findneighbours(maze,row,col): # So we need to keep that in mind that the neighbour is not an obstacle 
    neighbour = []
    if row >0: # checking UP
        neighbour.append((row-1,col))
    if row + 1<len(maze): # DOWN
        neighbour.append((row+1,col))
    if col > 0 : # LEFT
        neighbour.append((row,col-1))
    if col+1<len(maze[0]): # Right
        neighbour.append((row,col+1))
    return neighbour



# Main
def main(stdscr):
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    findpath(maze,stdscr)
    stdscr.getch()

wrapper(main)



# BFS - Goal is to find the shortest path from some starting node(0) to some endding node(X)
'''
   0 1 2 3 4
  |---------|
0 |_ _ X _ _|
1 |_ # # # _|
2 |_ # _ _ _|
3 |_ _ _ _ _|
4 |0 _ _ # _|
  |---------|
'''
# So We are Going to continuly finding/covering/expanding the path untill we reach the target node/ending node
# We then start checking All the Neighbours one iteration at a time 
#  _
#  ^
#  |
#  0 -- > _
# So for this we are Going to use Data Structure -> Queue - FIFO first in first Out
#                           _________________________
#    pop from front <------          1 2 3 4          <-----insert from back  
#                           _________________________
#     Front                                                   Back

# So first check the Neighbours if they are the End Node or Not
# if yes -> stop
# if no  -> add those nodes to the queue and pop the first node of and add to a visited list[] or set{}
# and start doing the same with each neighbours untill the target is found

# So if the neighbours neghbour in visited then -> skip 
# or if it is a blocked path -> then also skip

