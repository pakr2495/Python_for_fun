"""
sum(s1) and sum(s2) should be equal and total sum

scenaraio
[2,4,5,8] - odd sum not possible
[1,4,5,8] - even sum possible
[1,3,8]  - even not possible
"""

arr = [1,3,8]
n = len(arr)
s = sum(arr)
def subset(arr,s,n):
    if s == 0:
        return True
    if n == 0:
        return False
    
    if (arr[n-1]<=s):
        return subset(arr,s-arr[n-1],n-1) or subset(arr,s,n-1)
    else:
        return subset(arr,s,n-1)

if (s%2==0):
    print(subset(arr,s/2,n))
else:
    print(False)
