##################################################################################
# File: <hw4a>
#
# Course: CMPT 140 Introduction to Computing Science and Programming I
# Instructor: Dr. Herbert H. Tsang
# Description: <this program writes the letter of the user's initials>
# Due date: < 2018/11/09>
#
# Author: < Melissa Buist >
# Input: < User's name>
# Output: < the user's initials >
# I pledge that I have completed the programming assignment independently.
# I have not copied the code from a student or any source.
# I have not given my code to any student.
#
# Sign here: ___<Melissa Buist>_______
##################################################################################

#this functions evaluates the name the user entered and outputs the letters
def findLetters(name):
    #the while loops allows for more names then just two
    i = 0
    while i < len(name) :
        
        if name[i][0]=='a':
            print (" AAA ")
            print ("A   A")
            print ("AAAAA")
            print ("A   A")
            print ("A   A  *")

            print()

        elif name[i][0]=='b':
            print("BBBB")
            print("B   B")
            print("BBBB")
            print("B   B")
            print("BBBB  *")


            print()

        elif name[i][0]=='c':
            print("CCCCC")
            print("C")
            print("C")
            print("C")
            print("CCCCC  *")

            print()

        elif name[i][0]=='d':
            print("DDDD")
            print("D   D")
            print("D   D")
            print("D   D")
            print("DDDD  *")

            print()

        elif name[i][0]=='e':
            print("EEEEE")
            print("E")
            print("EEE")
            print("E")
            print("EEEEE  *")

            print()

        elif name[i][0]=='f':
            print("FFFFF")
            print("F")
            print("FFF")
            print("F")
            print("F  *")

            print()

        elif name[i][0]=='g':
            print("GGGGG")
            print("G")
            print("G  GG")
            print("G   G")
            print("GGGGG  *")

            print ()

        elif name[i][0]=='h':
            print("H   H")
            print("H   H")
            print("HHHHH")
            print("H   H")
            print("H   H  *")

            print ()
      
        elif name[i][0]=='i':
            print("IIIII")
            print("  I  ")
            print("  I  ")
            print("  I  ")
            print("IIIII  *")

            print ()

        elif name[i][0]=='j':
            print("  JJJ")
            print("   J")
            print("   J")
            print("J  J")
            print(" JJ   *")

            print ()
            
        elif name[i][0]=='k':
            print("K   K")
            print("K KK")
            print("KK")
            print("K  KK")
            print("K    K  *")

            print ()
            
        elif name[i][0]=='l':
            print("L")
            print("L")
            print("L")
            print("L")
            print("LLLLL  *")

            print()

        elif name[i][0]=='m':
            print("M   M")
            print("MM MM")
            print("M M M")
            print("M   M")
            print("M   M  *")

            print ()
            
        elif name[i][0]=='n':
            print("N   N")
            print("NN  N")
            print("N N N")
            print("N  NN")
            print("N   N  *")

            print()

        elif name[i][0]=='o':
            print(" OOO ")
            print("O   O")
            print("O   O")
            print("O   O")
            print(" OOO   *")

            print ()
            
        elif name[i][0]=='p':
            print("PPPP")
            print("P   P")
            print("PPPP")
            print("P")
            print("P  *")

            print()

        elif name[i][0]=='q':
            print(" QQQ ")
            print("Q   Q")
            print("Q   Q")
            print("Q Q Q")
            print(" QQQQ  *")

            print ()

        elif name[i][0]=='r':
            print("RRRR")
            print("R   R")
            print("RRRR")
            print("R  R")
            print("R   R  *")

            print ()

        elif name[i][0]=='s':
            print(" SSS")
            print("S")
            print(" SSS")
            print("    S")
            print(" SSS  *")

            print ()

        elif name[i][0]=='t':
            print("TTTTT")
            print("  T  ")
            print("  T  ")
            print("  T  ")
            print("  T    *")

            print ()
            
        elif name[i][0]=='u':
            print("U   U")
            print("U   U")
            print("U   U")
            print("U   U")
            print(" UUU   *")

            print ()
            
        elif name[i][0]=='v':
            print("V   V")
            print("V   V")
            print("V   V")
            print(" V V")
            print("  V    *")

            print()

        elif name[i][0]=='w':
            print("W   W")
            print("W   W")
            print("W W W")
            print("WW WW")
            print("W   W  *")

            print()
            
        elif name[i][0]=='x':
            print("X   X")
            print(" X X ")
            print("  X  ")
            print(" X X ")
            print("X   X  *")

            print ()
            
        elif name[i][0]=='y':
            print("Y   Y")
            print(" Y Y ")
            print("  Y  ")
            print("  Y  ")
            print("  Y    *")

            print()
            
        elif name[i][0]=='z':
            print("ZZZZZ")
            print("   Z ")
            print("  Z  ")
            print(" Z   ")
            print("ZZZZZ  *")

            print()

        #increments the counter
        i = i + 1


#asks the user for their name
name = (input("Enter your name : "))
#makes the name lower case
name = name.lower()
#makes the names into a list
name = name.split()
#calls the function
findLetters(name)


    



