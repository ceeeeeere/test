# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 10:43:14 2022

@author: User
"""

data = [[5, 6], [1, 2], [4,8], [7, 9], ]  #(恆a <= b)
data.sort()
opTbl = []
opTbl.append(data[0])
print(data)
print(opTbl)
for i in range(1, len(data), 1):
    j = len(opTbl) - 1
    if(data[i][0] <= opTbl[j][0]):#a1 < a0
        if data[i][1] > opTbl[j][1]:#b1 > b0
            opTbl[j][0], opTbl[j][1]= data[i][0], data[i][1]
        else:
            opTbl[j][0]= data[i][0]
    if(data[i][1] >= opTbl[j][1]):#b1 > b0
        if(data[i][0] < opTbl[j][0]):#a1 < a0
            opTbl[j][0], opTbl[j][1]= data[i][0], data[i][1]
        else:
            opTbl[j][1]= data[i][1]
    else: 
        print("append",end="")    
        opTbl.append([data[i][0],data[i][1]])
    opTbl.sort()
    print(opTbl)

print(opTbl)