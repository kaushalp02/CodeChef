# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 19:05:27 2021

@author: Kaushal
"""

X ,Y = input(" ").split()
X ,Y = float(X),float(Y)
if(X % 5 == 0) and (X + 0.5 <= Y):
    Y = Y - (X + 0.5)
print('%.2f'%Y)



