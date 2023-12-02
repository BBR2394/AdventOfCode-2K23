#! python3

import sys
import re

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")

def workEachLine(line):
    strLine = line
    reverseStr = line [::-1]
    fisrt = re.findall('[0-9]+',strLine)

    print(fisrt)
    firstDigit = fisrt[0][0]
    secondNumber = fisrt[len(fisrt)-1]
    print("second number : ", end="")
    print(secondNumber)
    lastDigit = secondNumber[len(secondNumber)-1]
    print("lastDigit number : ", end="")
    print(lastDigit)

    trois = firstDigit + lastDigit
    trois = int(trois)
    # if len(fisrt) == 1:
    #     trois = int(fisrt[0][0])
    # else: 
    #     trois = fisrt[0][0] + fisrt[len(fisrt)-1]
    print(trois)
    # second = re.findall('[0-9]+',reverseStr)
    
    # needSecond = True
    # hasOtherThanDigitTab = re.findall('\D+', line) 
    # if len(hasOtherThanDigitTab) == 0:
    #     needSecond = False

    # # if len(fisrt) == 1:
    # #     needSecond = False

    # print(fisrt[0] )

    # print(second[0])
    # second = second[0]
    # second = second[::-1]
    # print(second)
    # if int(fisrt[0] ) == int(second):
    #     needSecond = False
    # print("need second : ", end="")
    # print(needSecond)
    # if needSecond:
    #     trois = fisrt[0] + second
    # else:
    #     trois = fisrt[0] 
    # print("trois ", end="")
    # print (trois)
    return trois

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
