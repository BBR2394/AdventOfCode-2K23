#! python3

import sys

def displayData(lst):
    print("------#Data#------")
    for i in lst:
        print(i)
    print("------END--------")

def readFile(av):
    fd = open(av[1], 'r')
    #else:
    #    fd = open ("./input.txt", 'r')
    input = fd.read()
    lst = input.split('\n')

    displayData(lst)
    #workOnList(lst)

    fd.close()
    

def main(av):
    print("Hello - day 1")
    print(av)
    if len(av) >= 2:
        readFile(av)
    
if __name__ == '__main__':
    main(sys.argv)
