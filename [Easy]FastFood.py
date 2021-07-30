# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 18:14:19 2021

@author: Kaushal
"""
for __ in range(int(input())):
    N = int(input())
    A = list(map(int,input().strip().split()[:N]))
    B = list(map(int,input().strip().split()[:N]))
    Sum = []
    for i in range(N+1):
            Sum.append(sum(A[:i]) + sum(B[i:]))
    print(max(Sum))        
        
    
