#**********************************************************************
# Lab 4: <Files>
#
# Description:
# <This program open a file and outputs data based on the file> 
#  
#
# Author: <Melissa Buist, melissa.buist@mytwu.ca>
# Date: <October 26, 2018>
#
# Input: <a data file>
# Output: <average opening, average closing, max and min of opening>
#
# I pledge that I have completed the programming assignment independently
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Melissa Buist>
#*********************************************************************/
import sys
def lab4 ():
    #asks the user for the output file name
    outfileName = input("What file should the info go into? ")
    
    #declares infile as name of file
    infile = "AAPL.csv"
    
    #opens infile and outfile for reading and writing
    infile = open(infile, 'r')
    outfile = open(outfileName, 'w')

    #reads the first line 
    line = infile.readline()

    #declares variables for the while loop
    maxopening = 0
    minopening = sys.maxsize
    count = 0
    openaverage = 0
    closingaverage = 0

    #runs through all lines of data
    for lines in infile:

        #reads the first
        if count == 0 :
            #reads the first line 
            infile.readline()
            
        #reads the line of data
        lines = infile.readline()
        #splits line into a list
        lines = lines.split (",")
        
        #accesses opening
        opening = lines[1]

        #declares minopening
        #minopening = lines[1]
        
        #adds up average opening
        openaverage = openaverage + float(opening)
        #determines what opening is the smallest
        if float(opening) < float(minopening) :
            minopening = float(opening)
        #determines what opening is the biggest     
        if float(opening) > maxopening :
            maxopening = float(opening)
        #accesses the closing number    
        closing = lines[4]
        #adds up average closing
        closingaverage = closingaverage + float(closing)
        #increments count
        count = count + 1
        
    #calculates the opening average
    openaverage = openaverage/count
    #calculates the closing average
    closingaverage = closingaverage/count
    #prints data to the output file
    print ("The average opening price is " + str(openaverage), file=outfile)
    print ("The average closing price is " + str(closingaverage), file=outfile)
    print ("The maximun opening price is " + str(maxopening), file=outfile)
    print ("The minimum opening price is " + str(minopening), file=outfile)

    #closes both files
    infile.close()
    outfile.close()
    #tells user where the data has been put
    print("The data has been written to ", outfileName)
    
        
    


lab4 ()

