
n = 5
import math

def cal(n):
    if n == 0:
        return 0
    if n<=2:
        return 1
    
    if n%2 == 1:
        return cal(n-1) + cal(1)
    else:
        if math.log(n,2).is_integer():
            return cal(2)
        else:
            return 
