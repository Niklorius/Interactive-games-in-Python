# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
# Needs codeskulptor to run.

import simplegui
import math
import random

num_range = 100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(0, num_range)
    
    global num_guess
    num_guess = int(math.ceil(math.log(num_range + 1, 2)))
    
    print 'New game! Guess the secret number between 0 - ' + str(num_range) + "." 
    print "You have " + str(num_guess) + " guesses."
    print secret_number
    print ""
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()
    # remove this when you add your code    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    print "You guessed", guess
    global secret_number
    global num_guess
    num_guess -= 1
    
    if int(guess) == secret_number:
        print "Yup, you got it! The secret number is indeed " + str(secret_number) + "."
        print ""
        new_game()
    
    elif int(guess) > secret_number and num_guess > 0:
        
        print "Gotta go lower bruh..."
        print "You have", num_guess, "guesses remaining."
        print ""
    
    elif int(guess) < secret_number and num_guess > 0:
        
        print "You gotta go hiiigher! Hiiiiigher! Hiigher than the sky~~:D"
        print "You have", num_guess, "guesses remaining."
        print ""

    else:
        
        print "With", num_guess, "guesses remaining, you've lost all chances. Better luck next game."
        print ""
        new_game()
    
    
    
# create frame
tframe = simplegui.create_frame('Guess the number game!!', 200, 200)

# register event handlers for control elements and start frame
range100_button = tframe.add_button('<0 to 100>', range100, 100)
range1000_button = tframe.add_button('<0 to 1000>', range1000, 100)
poison_label = tframe.add_label('CHOOSE YOUR POISON')
input_region = tframe.add_input('PICK YOUR GUESS:', input_guess, 100)

# call new_game 
new_game()


