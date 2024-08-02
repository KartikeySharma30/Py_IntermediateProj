# It is a GUI based Turtle racing program in which the user choose the no. of turtle and align them equally spaced and race to
# the top of the screen and randomly assigning colors to them 
# Each turtle get assigned with a random value -> on which it moves forward 

# An GUI bases Turtle Race
import turtle           # Helps to do 2D basic Graphic activities
import time
import random
# constant val -> to denote these we generally tend to use capital letter so to tell we are not going to change this
WIDTH , HEIGHT = 500,500 
COLOR =['red','green','blue','orange','yellow','black','purple','brown','pink','cyan']


# Getting the Number of Racers from the User 
def get_number_of_racers():
    racers = 0 
    while True :
        racers = input("Enter the No. of Racers (2 - 10):")
        if racers.isdigit():
            racers = int(racers)
            if 2<=racers<=10:
                return racers
            else:
                print("Pls Enter the No. within the range")
        else:
            print("Valid Digit Pls!")
            continue

# Racing them by asigning random value to them
def race(colors):
    turtles = createturtle(colors)
    while True :
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y >= HEIGHT//2-10:
                return colors[turtles.index(racer)]

# Creating Turtle and Aligining each to the bottom of the screen
def createturtle(colors):
    turtles=[]
    spacingx=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 +(i+1)*spacingx,-HEIGHT//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles



# It help to Create/Initialize a 2D Screen to work upon 
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing")
    #screen.mainloop()


#Main

racers = get_number_of_racers()
print(racers)
init_turtle()
random.shuffle(COLOR)
colors = COLOR[:racers]

c=race(colors)
print(c)
time.sleep(2)



#racer = turtle.Turtle()
#racer.forward(100)
#time.sleep(5)

# .speed() , .penup, .shape(), .color(), .left/right(<degree>) , forward/backward(<no.of pixels to move>)