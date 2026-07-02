# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:52:31 2026

@author: jarud
"""


blacklist = [102, 205, 310, 415, 520, 630]

target = int(input("Enter sender ID to search: "))

found = False

for i in range(len(blacklist)):
    if blacklist[i] == target:
        print("Spam Sender Found at index", i)
        found = True
        break

if not found:
    print("Spam Sender Not Found")