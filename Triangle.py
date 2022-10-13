# -*- coding: utf-8 -*-
"""
Updated Sep 21, 2022
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: amrutha

"""
_author_="Amrutha Malavalli Srinivas"

import unittest

def classifyTriangle(a,b,c):
    
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    if (a + b <= c) or (a + c <= b) or (b + c <= a) : 
        return 'InvalidInput'

    if a > 200 or b > 200 or c > 200:
    	return 'InvalidInput'

    if not(isinstance(a,int) or not isinstance(b,int) or not isinstance(c,int)):
        return 'InvalidInput'
              
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotAtriangle'
                
    if a == b == c:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2) or ((a * 2) + (c * 2)) == (b * 2) or ((b * 2) + (c * 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isosceles'