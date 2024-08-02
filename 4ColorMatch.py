# Generate A -> 4 Color Random Code 
# Make the User Guess the Code
# Compare the Guess
# Tie the Game together

# So it is a Game in which Computer generate a Random 4 Character code and user have to create that code from the 
# given options in the 10 chances . it also tells if there is any correct or correct but placed at wrong position

import random

COLORS= ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LEN=4

# Generating a New Random CODE from the Given COLORS
def generate_code():
    code = []

    # We use '_' coz if we know that we are not gonna require <counter_variable> ahead so it is just for iteration
    for _ in range(CODE_LEN): 
        color = random.choice(COLORS)
        code.append(color)

    return code

# Taking Input from the User 
def guess_code():
    while True:
        guess = input("Guess :").upper().split()
        if len(guess)!=CODE_LEN:
            print(f"You Must Guess {CODE_LEN} Colors!!!")
            continue
        for color in guess:
            if color not in COLORS:
                print(f"Invalid Color :{color}. Try Again!")
                break # break out of the for loop 
        else:
            break
                
    return guess


# Here Checking and Matching Both the Codes and Provinding the Direction to the user to improve if needed
def check_code(guess,real_code):
    color_cont= {}
    correctPos=0
    incorrectPos=0

    for color in real_code:
        if color not in color_cont:
            color_cont[color]=0
        color_cont[color]+=1
    
    # zip() -> takes argument and combine them into tuples
    for gus_col ,rel_col in zip(guess,real_code):
        if gus_col==rel_col:
            correctPos+=1
            color_cont[gus_col]-=1

    for gus_col ,rel_col in zip(guess,real_code):
        if gus_col in color_cont and color_cont[gus_col]>0:
            incorrectPos+=1
            color_cont[gus_col]-=1
    
    return correctPos , incorrectPos


#Main
def game():
    print(f"Welcome to 'THE COLOR MATCH'!!!, you have {TRIES} to guess the code....")
    print("The Valid Color Options are :",*COLORS)
    code = generate_code()
    for attempts in range(1,TRIES+1):
        guess=guess_code()
        correctpos,incorrectpos = check_code(guess,code)
        if correctpos==CODE_LEN:
            print(f"You Won :{attempts} ")
            print(*code)
            break
        
        print(f"Correct Positions :{correctpos} | Incorrect Positions :{incorrectpos}")

    else:
        print("You Ran Out of Tries ,the code was :",*code)



if __name__=="__main__":
    game()