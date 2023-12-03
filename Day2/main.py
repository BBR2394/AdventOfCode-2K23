#! python3

import sys
import re

totalGreen = 13
totalRed = 12
totalBlue = 14

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")

def workEachLine(line, gameNumber):
    game = line.split(':')
    txt = "Game is {0} the res is {1}".format(gameNumber, game[1])
    print(txt)
    resTab = game[1].split(';')
    
    for i in resTab:
        print(i)
    
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
    gNb = 1
    for i in lst:
        workEachLine(i, gNb)
        gNb += 1

    fd.close()
    

def main(av):
    print("Hello - day 1")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
