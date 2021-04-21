def main ():
    A, B, C, D = 0, 0, 0, 0
    for A in  [4, 5, 7, 4, 9, 2, 1]:
        if A > 3:
            if A//2*2 == A:
                B += 1
            else:
                C+= 1
            if A%3 == 0:
                break
                D += 1

    print("A is " + str(A))
    print("B is " + str(B))
    print("C is " + str(C))
    print("D is " + str(D))





    tweet1 = '#twu_cs teaching award winner Peter the Apostle'
    tweet2 = 'Want cheap food? Visit Engineering Night #twucompsci'

    print('each' in tweet1)
    print(tweet2[5] + tweet1[-1])
    print('Nobel' in tweet1 or 'ant' in tweet2)
    print(not 'awards' in tweet1)


    str1 = "Code"
    str2 = ""
    for i in range(len(str1)) :
        str2 = str2 + str1[:i+1]
    print (str2)

main ()
