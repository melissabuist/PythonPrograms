#**********************************************************************
# Lab 2: <Control Structures>
#
# Description:
# <This program takes a variable, head or tails
# and competes against the computer >
#
# Author: <Melissa Buist, melissa.buist@mytwu.ca>
# Date: <September 28, 2018>
#
# Input: <heads, tails, or stop>
# Output: <who wins>
#
# I pledge that I have completed the programming assignment independently
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Melissa Buist>
#*********************************************************************/
import random
def lab2():
    #declares a variable to make the while loop run
    userGuess = ' '
    
    #creates a loop to run as long as userGuess doesn't equal s
    while userGuess != 's' :
        
        #gets the random number from the computer
        computerGuess = random.randint(0,1)
        
        #asks the user for their guess
        userGuess = input("Enter your guess: head (h) tail (t), and (s) to stop ")

        #determies whether the computer entered heads or tails
        if computerGuess  == 0:
            computerAnswer = 'head'
        elif computerGuess == 1:
            computerAnswer = 'tail'

        #determines the name of the user's guess
        if userGuess == 'h':
            userAnswer = 'head'
        elif userGuess == 't':
            userAnswer = 'tail'
        elif userGuess == 's':
            break
        else :
            break

        #compares the user's guess to the computer's guess
        if userAnswer == computerAnswer :
            rightOrWrong = 'correct'
        elif userAnswer != computerAnswer :
            rightOrWrong = 'wrong'

        #prints the output
        print ('The computer\'s guess is ' + computerAnswer + '. Your guess is ' +userAnswer + '. You are ' + rightOrWrong + '.')

lab2 ();         
            
        
