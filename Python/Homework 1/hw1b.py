##################################################################################
# HW 1
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <This program reads a date and figures out what day of the week>
# Due date: < Sept. 29, 2018>
#
# Author: < Melissa Buist >
# Input: < month, day, and year >
# Output: < day of the week >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################

def hw1b ():
    #asks the user for a month
    month = input("Enter a month: ")
    
    #asks the user for the day
    day = input ("Enter the day: ")
    
    #asks the user for the year
    year = input("Enter the year: ")

    #converts the months into numbers
    if month == 'January' :
        month = 1
    elif month == 'February' :
        month = 2
    elif month == 'March' :
        month = 3
    elif month == 'April' :
        month = 4
    elif month == 'May' :
        month = 5
    elif month == 'June' :
        month = 6
    elif month == 'July' :
        month = 7
    elif month == 'August' :
        month = 8
    elif month == 'September' :
        month = 9
    elif month == 'October' :
        month = 10
    elif month == 'November' :
        month = 11
    elif month == 'December' :
        month = 12


    #run the formula to figure out the day
    y = int(year) - int((14 - month)/12)
    x = y + y /4 - y / 100 + y / 400
    m = int(month) +12 *int((14 - month)/12) - 2
    d = int((2+2426 + (31*6) / 12) % 7)

    #converts d to a day
    dayOfTheWeek = 'b'
    if d == 0 :
        dayOfTheWeek = 'Sunday'
    elif d == 1 :
        dayOfTheWeek = 'Monday'
    elif d == 2 :
        dayOfTheWeek = 'Tuesday'
    elif d == 3 :
        dayOfTheWeek = 'Wednesday'
    elif d == 4 :
        dayOfTheWeek = 'Thursday'
    elif d == 5 :
        dayOfTheWeek = 'Friday'
    elif d == 6 :
        dayOfTheWeek = 'Saturday'

    #tells what day of the week the day is on
    print ('It is ' + dayOfTheWeek)

hw1b ();     
