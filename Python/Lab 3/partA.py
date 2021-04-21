#**********************************************************************
# Lab 3: <Seperate Strings>
#
# Description:
# <This program takes a sentence without spaces and addds spaces> 
#  
#
# Author: <Melissa Buist, melissa.buist@mytwu.ca>
# Date: <October 12, 2018>
#
# Input: <a sentence without spaces with each word starting with capital letter>
# Output: <the sentence with spaces between words>
#
# I pledge that I have completed the programming assignment independently
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Melissa Buist>
#*********************************************************************/
def partA ():

    sentence = input("Enter a sentence without spaces in it: ")
    count = 0
    letter = sentence[1]
    for letter in sentence :
        answer = sentence[count].isupper()
        if answer == True :
           word = sentence.lower 
           print (" " + sentence[count], end="")
        else:
            print (sentence[count], end="")
        count = count + 1    
        

    
partA ()    
