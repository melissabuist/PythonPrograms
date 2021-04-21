def main ():


    count = 0
    sums = 0
    n = 7
    
    while count < n-1 :
        print ((2*count+1), end= " + ")
        sums = sums + (2*count +1)
        count = count +1
    finalSum = sums + (2*(n-1)+1)
    print (str(2*(n-1)+1) + " = " + str(finalSum))








main ()    
