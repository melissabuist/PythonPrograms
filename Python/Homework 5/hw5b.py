##################################################################################
# File: <HW5b>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program takes two ints and multiplies them with recursion>
# Due date: < 2018/11/24 >
#
# Author: < Melissa Buist >
# Input: < two ints >
# Output: < the two ints multiplied together >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################


def mult( n, m ):
    #this is the base case for the recursive algorithm
    if m == 0:
        return 0
    #this is the recursive part
    else:
        return n + mult(n, m-1)




x = (int(input("Enter an integer: ")))
y = (int(input("Enter an integer: ")))
#the call to the function
answer = mult(x, y)
#prints the result of the muliplication
print(answer)
