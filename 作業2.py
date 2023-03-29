# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:57:15 2023

@author: User
"""

num_list = []
for i in range(6):
    num = int(input("請輸入數字:"))
    num_list.append(num)
    
num_list.sort(reverse = True)
print("由小至大排列:",num_list)


