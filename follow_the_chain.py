#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:06:38 2017

@author: gav
"""

import requests
from matplotlib import pyplot as plt

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

# Original starts at "12345" - and completes at "66831" with "peak.html"
# But in the original thread, the 86th url = "16044" - says
# "Yes. Divide by two and keep going."  "8044" leads to "25357"
# which is not in original list
next_nothing = "12345"
nothings = []

for i in range(400):
    next_nothing = requests.get(base_url + next_nothing).text.split()[-1]
    print("{:>4}".format(i) + "{:>8}".format(next_nothing))
    nothings.append(next_nothing)

next_nothing = "25357"

nothings1 = []

for i in range(200):
    next_nothing = requests.get(base_url + next_nothing).text.split()[-1]
    print("{:>4}".format(i) + "{:>8}".format(next_nothing))
    nothings1.append(next_nothing)

x=list(range(400))

nothings_ints = [str(x) if x.isdigit() else -10000 for x in nothings]
nothings1_ints = [str(x) if x.isdigit() else -10000 for x in nothings1]

plt.plot(x, nothings_ints)
plt.plot(x, nothings1_ints)

#with open("nothings1.txt", "w") as f:
#    for i, val in enumerate(nothings):
#        strout = str(i) + " " + val + "\n"
#        f.write(strout)
#        
## answer is at ...nothing=66831