#**********************************************************************
# Lab 1: <Compute the Volume of a Cylinder>
#
# Description:
# <This program calculates the volume of a cylinder
# with the needed information given by the usesr>
#
# Author: <Melissa Buist, melissa.buist@mytwu.ca>
# Date: <September 14, 2018>
#
# Input: <radius and height>
# Output: <volume of a cylinder>
#
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: <Melissa Buist>
#*********************************************************************/

def lab1():
    #Constant
    pi = 3.14

    #user input of name
    name = input("What is your name? ")

    #user input of radius
    radius = int(input("What is the radius? "))

    #user input of height
    height = int(input("What is the height? "))

    #Calculates the volume of the cylinder
    volume = pi*(radius**2)*height            
             
    #prints the final output
    print ('Hi '+ name + ', the volume of the cylinder is equal to ' + str(volume)) 
                        
lab1();
