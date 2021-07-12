# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 15:29:01 2021

@author: Kaushal
"""
T = int(input())
for i in range(T):
    N = int(input())
    S = list(map(int,input().strip().split()[:N])) 
    S.sort()
    Ans = max(S)
    for i in range(N-1):
        if (S[i+1] - S[i] < Ans):
            Ans = S[i+1] - S[i]
    print(Ans)
        