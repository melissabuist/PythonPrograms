##################################################################################
# File: <HW5a>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program takes a text file and displays the most common words>
# Due date: < 2018/11/21 >
#
# Author: < Melissa Buist >
# Input: < file name  and number of words the user wants to know>
# Output: < a few of the most common words >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################
def findWords (fname, num):
    #opens the file to a read only mode
    infile = open(fname,'r')
    #assigns an empty dictionary
    d = dict()
    #a histogram for loop to count the words
    for line in infile :
            for words in line.split() :
                if words not in d:
                    d[words] = 1
                else:
                    d[words] += 1
    count = 0            
    #this for loop determines which words are the most common
    for w in sorted(d, key=d.get, reverse=True):
        if count < num :
            print (w + " is displayed", d[w], "times")
            count = count + 1
        else :
            break
        

    return d
                




#gets the file name
fname = input("Enter filename: ")
#asks the user for how many words they want
num = int(input("How many most common words do you want displayed? "))
#calls the function
dictionary = findWords(fname, num)
#closes the file
#infile.close()

