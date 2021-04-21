##################################################################################
# HW 2
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program takes a number and outputs a series of triangles>
# Due date: < 2018/10/10 >
#
# Author: < Melissa Buist >
# Input: < a number >
# Output: < a series of triangles the height of the input >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################
def hw2a ():
    #asks the user for a number that will determine the size of triangle
    h = int(input("Enter a number "))

    #for loop for pattern A
    for i in range(1, h+1) :
        for j in range(1, i+1) :
            print (str (j), end="")
        print ()
    #line to add a space between patterns
    print ()


    #for loop for pattern B
    for x in range(h, 0, -1) :
        count = 1
        for y in range(x, 0, -1) :
            print (str (count), end="")
            count = count + 1
        print ()
    #line to add a space between patterns
    print ()

    #for loop for pattern C
    for a in range(1, h+1) :
        count2 = h 
        print ((" ")*(count2 - a), end="")
        for b in range(1, a+1) :
            print (str (b), end="")
            count2 = count2 - 1
        print ()
        
    #line to add a space between patterns
    print ()        

        
        













hw2a()    
