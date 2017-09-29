#!/usr/bin/python3.6 -tt

import sys

def main():
# To get the arg from command line
        arglist  = sys.argv
        print(len(sys.argv))

	mylist = []
        for i in range(1, len(sys.argv)):
                print(str(arglist[i]))
                mylist.append(arglist[i])
        print(mylist) 


