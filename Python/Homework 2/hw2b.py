##################################################################################
# HW 2
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program takes numbers and gives characteristics of the set>
# Due date: < 2018/10/10 >
#
# Author: < Melissa Buist >
# Input: < a set of numbers >
# Output: < smallest number, largest number, average, and cummulative sum >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################
def hw2b ():

    #define count to get a divisor for the average
    count = 0
    #defines number so the while loop works
    number = 0
    #defines smallestNumber and biggestNumber for the if loop
    smallestNumber = 100000
    biggestNumber = 0
    #define these for the average and cumulative sum
    addingNumbers = 0
    cumulativeSum = 0

    #this allows for the user to enter multiple numbers
    while number != -1 :

        #asks the user for a number
        number = float(input("Enter a number or enter -1 to stop: "))

        #decides which number is the smallest
        if (number <= smallestNumber and number != -1):
            smallestNumber = number
        #decides which number is the biggest    
        if (number >= biggestNumber):
            biggestNumber = number
        #by including this if statement it makes sure to not add -1 to totals
        if (number!= -1):
            #adds the numbers together for the average later on
            addingNumbers = addingNumbers + number
            #makes a running count of how many numbers are entered
            count = count + 1
            #adds up the total for the cumulative sum
            cumulativeSum = cumulativeSum + number
    #calculates the average from the entered numbers
    finalAverage = addingNumbers/count
    #prints the results of the tests
    print ('The smallest number is ' + (str(smallestNumber)))
    print ('The largest number was ' + (str(biggestNumber)))
    print ('The average of these numbers is ' + (str(finalAverage)))
    print ('The cummulative sum of thses numbers ' + (str(cumulativeSum)))


    

            














hw2b ()    
