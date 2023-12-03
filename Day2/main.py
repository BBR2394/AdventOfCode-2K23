#! python3

import sys
import re

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")

def workEachLine(line):
    return line

def readFile(av):
    fd = open(av[1], 'r')
    #else:
    #    fd = open ("./input.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    #displayData(lst)
    #workOnList(lst)
    lstTab = []
    for i in lst:
        lstTab.append(workEachLine(i))
    # print("ici")
    dayOneRes = 0
    for j in lstTab:
        #print (j)
        dayOneRes += int(j)

    #print("res")
    #print(lstTab)
    print('le resultat final : ', end='' )
    print(dayOneRes)
    fd.close()
    

def main(av):
    print("Hello - day 1")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
