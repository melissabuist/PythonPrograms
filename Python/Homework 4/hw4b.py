##################################################################################
# File: <hw4b>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <this program draws the letter of the user's initials>
# Due date: < 2018/11/09>
#
# Author: < Melissa Buist >
# Input: < User's name>
# Output: < the user's drawn out initials >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################


import turtle
#this functions evaluates the name the user entered and outputs the letters
def findLetters(name):
    #the while loops allows for more names then just two
    i = 0
    while i < len(name) :

        turtle.up()
        turtle.home()
        turtle.goto((i*100), 0)
        turtle.down()
        
        if name[i][0]=='a':
            #A
            turtle.left(70)
            turtle.forward(110)
            turtle.right(140)
            turtle.forward(55)
            turtle.right(110)
            turtle.forward(35)
            turtle.right (180)
            turtle.forward(35)
            turtle.right(70)
            turtle.forward(55)



        elif name[i][0]=='b':
            #B
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(50)
            turtle.forward(10)
            turtle.right(40)
            turtle.forward(30)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.right(180)
            turtle.forward(40)
            turtle.right(50)
            turtle.forward(10)
            turtle.right(40)
            turtle.forward(40)
            turtle.right(50)
            turtle.forward(10)
            turtle.right(40)
            turtle.forward(40)


        elif name[i][0]=='c':
            #C
            turtle.left(140)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward (85)
            turtle.right(50)
            turtle.forward(10)
            turtle.right(40)
            turtle.forward(40)
            turtle.right(50)
            turtle.forward(10)
            turtle.right(40)
            turtle.forward(10)
            turtle.up()
            turtle.goto((i*100),0)
            turtle.down()
            turtle.left(90)
            turtle.forward(40)
            turtle.left(50)
            turtle.forward(10)
            turtle.left(40)
            turtle.forward(10)


        elif name[i][0]=='d':
            #D
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(12)
            turtle.right(50)
            turtle.forward(81)
            turtle.right(40)
            turtle.forward(12)
            turtle.right(50)
            turtle.forward(40)

        elif name[i][0]=='e':
            #E
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(45)
            turtle.up()
            turtle.goto((i*100), 0)
            turtle.down()
            turtle.forward(45)
            turtle.up()
            turtle.goto((i*100), 50)
            turtle.down()
            turtle.forward(30)

        elif name[i][0]=='f':
            #F
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(45)
            turtle.up()
            turtle.goto((i*100), 50)
            turtle.down()
            turtle.forward(35)

        elif name[i][0]=='g':
            #G
            turtle.forward(40)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(25)
            turtle.up()
            turtle.goto((i*100), 0)
            turtle.down()
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(87)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(20)

        elif name[i][0]=='h':
            #H
            turtle.left(90)
            turtle.forward(100)
            turtle.goto(i*50, 0)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(90)
            turtle.forward(50)
            turtle.left(180)
            turtle.forward(100)


        elif name[i][0]=='i':
            #I
            turtle.forward(50)
            turtle.goto(((i*100)+25), 0)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(25)
            turtle.left(180)
            turtle.forward(50)


        elif name[i][0]=='j':
            #J
            turtle.left(140)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(20)
            turtle.up()
            turtle.goto((i*100), 0)
            turtle.down()
            turtle.right(90)
            turtle.forward(30)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(90)
            
        elif name[i][0]=='k':
            #K
            turtle.left(90)
            turtle.forward(100)
            turtle.goto((i*100), 50)
            turtle.right(45)
            turtle.forward(70)
            turtle.up()
            turtle.goto((i*100), 50)
            turtle.down()
            turtle.right(90)
            turtle.forward(70)         

        elif name[i][0]=='l':
            #L
            turtle.forward(50)
            turtle.goto((i*100), 0)
            turtle.left(90)
            turtle.forward(100)

        elif name[i][0]=='m':
            #M
            turtle.left(90)
            turtle.forward(100)
            turtle.right(135)
            turtle.forward(40)
            turtle.left(90)
            turtle.forward(40)
            turtle.right(135)
            turtle.forward(100)
            
        elif name[i][0]=='n':
            #N
            turtle.left(90)
            turtle.forward(100)
            turtle.right(150)
            turtle.forward(110)
            turtle.left(150)
            turtle.forward(100)

        elif name[i][0]=='o':
          #O
          turtle.forward(40)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(90)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(40)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(90)
          turtle.left(40)
          turtle.forward(10)
            
        elif name[i][0]=='p':
            #P
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            



        elif name[i][0]=='q':
          #Q  
          turtle.forward(40)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(90)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(40)
          turtle.left(40)
          turtle.forward(10)
          turtle.left(50)
          turtle.forward(90)
          turtle.left(40)
          turtle.forward(10)
          turtle.up()
          turtle.goto((i*100)+30, 15)
          turtle.down()
          turtle.left(10)
          turtle.forward(30)

        elif name[i][0]=='r':
            #R
            turtle.left(90)
            turtle.forward(100)
            turtle.right(90)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.left(135)
            turtle.forward(65)


        elif name[i][0]=='s':
            #S
            turtle.forward (40)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(40)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(37)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)
            turtle.right(40)
            turtle.forward(10)
            turtle.right(50)
            turtle.forward(40)

            print ()

        elif name[i][0]=='t':
            #T
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(25)
            turtle.left(180)
            turtle.forward(50)
            
        elif name[i][0]=='u':
            #U
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.right(90)
            turtle.forward(90)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(40)
            turtle.left(40)
            turtle.forward(10)
            turtle.left(50)
            turtle.forward(90)
            
        elif name[i][0]=='v':
            #V
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.right(60)
            turtle.forward(100)
            turtle.left(130)
            turtle.forward(100)
            
        elif name[i][0]=='w':
            #W
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.right(90)
            turtle.forward(100)
            turtle.left(135)
            turtle.forward(40)
            turtle.right(90)
            turtle.forward(40)
            turtle.left(135)
            turtle.forward(100)
            
        elif name[i][0]=='x':
            #X
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.right(60)
            turtle.forward(100)
            turtle.up()
            turtle.goto((i*100)+50, 100)
            turtle.down()
            turtle.right(60)
            turtle.forward(100)
            
            
        elif name[i][0]=='y':
            #Y
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.right(60)
            turtle.forward(50)
            turtle.left(130)
            turtle.forward(50)
            turtle.left(180)
            turtle.forward(50)
            turtle.left(25)
            turtle.forward(50)
            
        elif name[i][0]=='z':
            #Z
            turtle.up()
            turtle.goto((i*100), 100)
            turtle.down()
            turtle.forward(60)
            turtle.right(130)
            turtle.forward(100)
            turtle.left(130)
            turtle.forward(60)
            


        #draws a dot after the letter
        turtle.up()
        turtle.goto((i*100)+60, 0)
        turtle.down()
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)
        turtle.left(90)
        turtle.forward(2)

        #increments the counter
        i = i+1


#asks the user for their name
name = (input("Enter your name : "))
#converts the letters all the lower case
name = name.lower()
#splits the name into a list
name = name.split()
#calls the function
findLetters(name)

















