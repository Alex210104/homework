# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 17:39:54 2023

@author: User
"""

#4-1 and 4-2

a = int(input("輸入數值1:"))
b = int(input("輸入數值2:"))
c = int(input("輸入數值3:"))

if a**2 + b**2 > c**2 and b**2 + c**2 > a**2 and c**2 + a**2 >b**2:
   print("可構成三角形")
   if a == b == c:
        print("此為正三角形")    
   elif a == b or b == c or a == c:
        print("此為等腰三角形")
else:
    print("不可構成三角形")