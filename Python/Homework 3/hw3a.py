##################################################################################
# File: <Homework 3 Part A>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <It takes a list of numbers and removes the duplicates>
# Due date: <2018/10/27>
#
# Author: < Melissa Buist >
# Input: < user input of numbers>
# Output: < a list of distinct numbers >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################
#defines the function with a list parameter
def eliminateDuplicates( lst ):
    #splits the list at the spaces
    lst = list1.split()

    #converts the list to ints 
    lst = list(map(int, lst))

    #sorts the list numerically
    lst.sort()
    
    #starts a counter to go through list
    counter = 0
    #runs through the list checking each element
    while counter < len(lst):
        #makes a count of numbers in the list
        count = lst.count(lst[counter])
        #removes the instance of the repeated number
        if count > 1 :
            lst.remove(lst[counter])
            counter = 0
        counter = counter + 1
    return lst


#asks the user to enter an input of numbers
list1 = (input("Enter numbers: "))



#calls for function
results = eliminateDuplicates( list1 )
print ("The distinct numbers are " + str(results))



