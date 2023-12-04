#! python3

import sys
import re
import math

symbolsRegex = re.compile('[:=\/$*+;0-9]{1,1}')

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")

def countPoint(point):
    if point < 1:
        return 0
    elif point == 1:
        return 1
    else:
        return int(math.pow(2, point-1))

def processGame(line, gameNumber):
    print("Game : ", end="")
    print(gameNumber)
    print(line)
    gameData = line.split('|')
    winnerRes = gameData[0].split(' ')
    myRes = gameData[1].split(' ')
    # print("winner game ")
    # print(winnerRes)
    # print(" my res : ")
    # print(myRes)

    try:
        hasEmpty = True
        while hasEmpty:
            winnerRes.remove('')

    except:
        pass

    pts = 0

    for i in myRes:
        try:
            winnerRes.index(i)
            pts += 1
        except:
            pass

    finalPoint = countPoint(pts)
    print("A la partie : {0} Nous avons eu de numbre {1} point {2}".format(gameNumber, pts, finalPoint))
    return finalPoint

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

    totals = 0
    for i in lst:
        print(i)
        totals += processGame(i.split(':')[1], gNb)
        gNb += 1

    print("Le nombre de point total : {0}".format(totals))
    fd.close()
    

def main(av):
    print("Hello - day 3")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
