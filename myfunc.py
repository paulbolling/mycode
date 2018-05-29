#!/usr/bin/env python3

#Function that opens a file, writes an arguments and closes.

def newtfile(string1, string2, string3):
    pfo = open("file1.txt","a")
    print(string1, string2, string3, file = pfo)
    pfo.close()
choice = " "
while(choice.lower()!="q"):
    x = input("Give me a string: ")
    y = input("Give me a string: ")
    z = input("Give me a string: ")
    choice = input("q to quit")
newtfile(x, y, z)