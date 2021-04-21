def hw2bPractice ():
    smallestNumber = 100
    biggestNumber = 0
    setOfNums = input("Enter some numbers seperated by a comma ")

    setOfNums = setOfNums.split(',')

    print(setOfNums)

    #while setOfNums != ' ' :
    for i in range (0, len(setOfNums)) :
        if ((setOfNums[i]) <= smallestNumber):
            smallestNumber = (setOfNums)
            
        if ((setOfNums[i]) >= biggestNumber):
            biggestNumber = (setOfNums)




hw2bPractice ()    
