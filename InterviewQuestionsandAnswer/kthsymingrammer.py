"""
n -> row
k -> col
0    ---- k=1 n=1
01
0110
01101001

what is the n and k for the givebn value
"""
import math

def cal(n,k):
    if n ==1 and k ==1:
        return 0
    mid = math.pow(2,n-1)/2
    if k<=mid:
        return cal(n-1,k)
    else:
        return  1 if cal(n-1,k-mid) == 0 else 0

print(cal(3,4))