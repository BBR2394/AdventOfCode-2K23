#! python3

import sys
import re

symbolsRegex = re.compile('[:=\/$*+;0-9]{1,1}')

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")


def readFile(av):
    fd = ''
    if len(av) >= 2:
        fd = open(av[1], 'r')
    else:
        fd = open ("./input.txt", 'r')

    input = fd.read()
    
    lst = input.split('\n')

    #displayData(lst)
    #workOnList(lst)
    lstTab = []
    gNb = 1

    for i in lst:
        print(i)
        for j in i:
            print("le charactere est : " + j)
            print("res de la regex : ")
            print(symbolsRegex.match(j))

        gNb += 1

    fd.close()
    

def main(av):
    print("Hello - day 3")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
