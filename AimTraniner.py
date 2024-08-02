# Here we have created a AIM Trainer using Pygames -> which helps us to create games using python
# AIM Trainer is a Game helps you calculate the no. of aims you have clicked in a given time 
# So as to increase your cursor accuracy overtime

import math
import random
import time
import pygame
import pygame.draw

# Here we are Initializing Pygame Screen and Its Title 
pygame.init()

WIDTH,HEIGHT = 500,500

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Aim Trainer") # Title for the window 

# CONSTANT Values 
TARGET_INC = 400
TARGET_Event = pygame.USEREVENT

TARGET_Padding = 30

BG_COLOR = (0,25,40)
LIVES=3
TOP_BARH=50
LABEL_FONT = pygame.font.SysFont("helvetica neue",18)





class Target:
    MAX_SIZE=30
    GROWTH_RATE = 0.2
    COLOR = "red"
    SECOL= "White"
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.size=0
        self.grow=True

    # Updating the Target Sizes 
    def update(self):
        if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
            self.grow=False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size-= self.GROWTH_RATE

    # Drawing the Target 
    def draw(self,win):
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.size) # Layer by layer overlapping
        pygame.draw.circle(win,self.SECOL,(self.x,self.y),self.size * 0.8)
        pygame.draw.circle(win,self.COLOR,(self.x,self.y),self.size * 0.6)
        pygame.draw.circle(win,self.SECOL,(self.x,self.y),self.size * 0.4)

    # Checking is the USER Clicked the Target or Not
    def collide(self,x,y):
        dist = math.sqrt((x - self.x)**2 + (y-self.y)**2)

        return dist <=self.size

# Calculating the Time Elapsed for Displaying 
def fmtime(secs):
    milli=math.floor(int(secs* 1000 % 1000)/100)
    sec = int(round(secs % 60,1))
    min= int(secs // 60)

    return f"{min:02d}:{sec:02d}:{milli}"

# Drawing the TopBar which will let us know the current stats of the USER 
def draw_topbar(win,elapsed_time,target_pressed,misses):
    pygame.draw.rect(win,"grey",(0,0,WIDTH,TOP_BARH))
    time_label = LABEL_FONT.render(f"Time : {fmtime(elapsed_time)}",1,"black")

    speed = round(target_pressed/elapsed_time,1)
    speedl=LABEL_FONT.render(f"Speed : {speed}t/s",1,"black")

    hitsl=LABEL_FONT.render(f"Hits : {target_pressed}",1,"black")
    
    livel=LABEL_FONT.render(f"Lives : {LIVES-misses}",1,"black")
    win.blit(time_label,(10,12))
    win.blit(speedl,(150,12))
    win.blit(hitsl,(300,12))
    win.blit(livel,(400,12))

 

# Drawing Targets 
def draw(win,targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)

    pygame.display.update()


# End Screen Shows after USERs all the lives are finished and shows the total score and accuracy 
def end_screen(win,elapsed_time,targpress,clicks):
    win.fill(BG_COLOR)
    time_label = LABEL_FONT.render(f"Time : {fmtime(elapsed_time)}",1,"white")

    speed = round(targpress/elapsed_time,1)
    speedl=LABEL_FONT.render(f"Speed : {speed}t/s",1,"white")

    hitsl=LABEL_FONT.render(f"Hits : {targpress}",1,"white")
    
    accuracy = round(targpress/clicks *100,1)
    accl=LABEL_FONT.render(f"Accuracy : {accuracy}%",1,"white")
    win.blit(time_label,(180,100))
    win.blit(speedl,(180,200))
    win.blit(hitsl,(180,300))
    win.blit(accl,(180,400))
    
    pygame.display.update()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                quit()
    





# Main 
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    target_pressed = 0
    clicks = 0
    misses=0
    start_time = time.time()




    pygame.time.set_timer(TARGET_Event,TARGET_INC)

    while run :
        clock.tick(60)
        click=False
        mousepos=pygame.mouse.get_pos()
        elapsed_time =time.time()-start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
            if event.type==TARGET_Event:
                x=random.randint(TARGET_Padding,WIDTH-TARGET_Padding) # To Ensure the Target wont appear off the Screen 
                y=random.randint(TARGET_Padding+TOP_BARH,HEIGHT-TARGET_Padding)
                target = Target(x,y)
                targets.append(target)
            if event.type == pygame.MOUSEBUTTONDOWN:
                click=True
                clicks+=1
        for target in targets:
            target.update()

            if target.size <=0:
                targets.remove(target)
                misses+=1
            if click and target.collide(*mousepos): # '*' -> known as splat operator
                targets.remove(target)
                target_pressed+=1
            if misses >= LIVES:
                end_screen(WIN,elapsed_time,target_pressed,misses)
                
                pass # End the Game
        draw(WIN,targets)
        draw_topbar(WIN,elapsed_time,target_pressed,misses)
        pygame.display.update()
    pygame.quit()




if __name__=="__main__":
    main()
