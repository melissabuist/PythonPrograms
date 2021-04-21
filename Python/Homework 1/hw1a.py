##################################################################################
# HW 1
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program tests if three numbers are the same of increasing>
# Due date: < Sept. 29, 2018>
#
# Author: < Melissa Buist >
# Input: < three number: x, y, z >
# Output: < same, different, other, increasing, decreasing, or neither >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################

def hw1a():
	#user input of the three numbers number
        x,y,z = input("Please enter 3 numbers: (x, y, z): ")

	#test if the numbers are the same
        if x == y and x==z and z==y:
                print('same')
        #test if the numbers are all different        
        elif x != y and x != z and z != y:
                print ('all different')
        #the else deducts that the two other don't apply making it other       
        else :
                print ('others')

        #test if the numbers are increasing
        if x < y and y < z :
                print ('increasing')
        #test if the numbers are decreasing        
        elif x > y and y > z :
                 print ('decreasing')
        #shows that the upper to don't apply therefore it is neither        
        else :
                 print ('neither')

                 
         

hw1a ();
