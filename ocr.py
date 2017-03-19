#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 10:21:00 2017

@author: gav
"""

with open("ocr_dump.txt") as f:
    # creat an empty list of characters
    
    chars = {}
    count = 0
    maxcount = 100000
    
    for i in range(37):
        f.readline()
#    print(f.readline())
        
    # read in a character from the file
    while True:
        c = f.read(1)
        if (not c) or (count == maxcount):
            print("End of file or count")
            break
        else:
            chars.setdefault(c, 0)
            chars[c]+=1
            count+=1

#    print(chars)
    # if it is in the list of characters, add 1 to the count for that entry
    
    # otherwise add a new entry and increment count to 1
    
    # finally report counts for each character
    
    for char, freq in chars.items():
        print("{:>3}".format(char), "+" * int(freq/100))