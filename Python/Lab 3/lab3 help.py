def main ():
    #here is some copialbe code for tomorrows lab
    infileName = input ("What file is the info in? ")
    outfileName = input("What file should the info go into? ")

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')


    infile.close()
    outfile.close()

main ()    
