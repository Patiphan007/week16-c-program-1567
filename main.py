from Python1601 import testCon01
from Python1602 import testCon02
from Python1603 import fun
from Python1604 import result
from Python1605 import eventOdd

def star():
    values = range(30)
    for i in values:
        print("=", end="")

def main():
    print("Main program")
    #Call function in python
    #=======================
    star() 
    print("")
    fun("Mu Haaa",100,leader="forg")
    star()
    print("")
    #testCon02()
    #testCon01()
    #=======================

main()
