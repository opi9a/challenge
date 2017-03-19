#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:28:41 2017

@author: gav
"""
import requests
import re

# Regexes
outerRgx = re.compile(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]') # 1 lower - CORE - 1 lower
req = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")
mo = outerRgx.findall(req.text)  

print("\n Regex results:\n", mo)
print("\nThe answer is", "".join([x[4] for x in mo]))


## Regex to look for 4-way cross
#testRegex = re.compile(r'''
##                       [a-z].{81}
#                       [A-Z].{81}
#                       [A-Z].{81}
#                       [A-Z].{77}
#                       [a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]
#                       .{77}[A-Z]
#                       .{81}[A-Z]
##                       .{81}[A-Z]
##                       .{81}[a-z]
#                       ''', re.VERBOSE)
