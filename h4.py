# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:27:27 2022

@author: User
"""

# =============================================================================
# 請輸入兩個整數，判斷哪一個比較大，之後將該數倒著印出來，並求與原來數目的和，及該數有幾個偶數，
# 幾個奇數，數字總和各為多少？
# 例：請輸入兩個整數：123 653
# 輸出：653 較大，共有 1 個偶數，2 個奇數，數字和 14。653 + 356 = 1009
# =============================================================================

data = list(map(int,input().split()))
n = max(data)
oddNum ,evenNum = 0 ,0#奇數個，個偶數7878777777
numSum = 0 #數字和

n_str = str(n)

for i in n_str:
    a = int(i)
    numSum += a
    if( a%2 == 1):
        oddNum += 1
    else:
        evenNum += 1

n_rev = int(n_str[::-1]) #反轉數字

print("%d較大，共有 %d 個偶數，%d 個奇數，數字和%d。%d+%d=%d"
      %(n, evenNum, oddNum, numSum, n, n_rev, n + n_rev))