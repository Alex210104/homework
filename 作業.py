# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:24:44 2023

@author: USER
"""

scores = [100,60,70,80,99,100,66]
#1.由使用者輸入分數後找到就移除 限用pop 找不到時顯示找不到

score_to_remove = int(input("請輸入要移除的分數："))

if score_to_remove in scores:
    scores.pop(scores.index(score_to_remove))

    print("分數", score_to_remove, "已移除")
    print("剩餘分數：", scores)
else:
    print("找不到分數", score_to_remove)
    print("剩餘分數：", scores)
    




