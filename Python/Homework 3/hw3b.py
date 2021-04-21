##################################################################################
# File: <Homework 3 Part B>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <It takes a two words and decides if they contain the same letters>
# Due date: <2018/10/27>
#
# Author: < Melissa Buist >
# Input: < user input of two words >
# Output: < if the two words are anagrams >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################

def isAnagram (s1, s2):
    #converts the strings to lists
    s1 = list(s1)
    s2 = list(s2)
    #sorts the two lists alphabetically
    s1 = sorted(s1)
    s2 = sorted (s2)
    #declare variables for the loop
    count = 0
    counter = 0
    #runs through each string checking each value
    while counter < len(s1) :
        #checks if the strings are the same length
        if len(s1) != len(s2):
            return ("These words are not angrams")
            #they aren't the same length so they can't be anagrams
            break
        #evaluates if each value is the same 
        if s1[counter] is s2[counter] :
            #counts up the number of letters that are the same
            count = count + 1
        #increments the counter for the while loop    
        counter = counter + 1
    #sees if all of the letters match up    
    if count == len(s1) :
        return ("These words are anagrams")
    else :
        return ("These words are not anagrams")


    








#asks the user to enter two words
s1 = input("Enter a word ")
s2 = input("Enter another word ")
#calls the function
result = isAnagram (s1, s2)
#print the results
print(result)

