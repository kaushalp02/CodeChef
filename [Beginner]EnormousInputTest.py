# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 09:12:37 2021

@author: Kaushal
"""
n ,k = input(" ").split()
n ,k = int(n),int(k)
count = 0
for i in range(n):
    t = int(input(""))
    if(t % k == 0):
        count += 1
print(count)
    
    