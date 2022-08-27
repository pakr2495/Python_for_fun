"""
count number of subset with given difference

if (sum(arr) + diff)%2 ==1
    return 0
else:

sum(s1) - sum(s2) = diff(given)
sum(s1) + sum(s2) = totalsum

2*(sum(s1)) = totalsum + diff
sum(s1) = (totalsum + diff)/2
sum(s2) = diff - sum(s1)
calculate either count of sum(s1) or count of sum(s2) 
"""

arr = [1,2,4,5]
n = len(arr)
diff = 2
t = sum(arr)

def cal(arr,s,n):
    if s == 0:
        return 1
    if n == 0: 
        return 0
    if arr[n-1]<=s:
        return cal(arr,s-arr[n-1],n-1) + cal(arr,s,n-1)
    else:
        return cal(arr,s,n-1)

if ((t+diff)%2==1):
    print(0)
else:
    s1 = int((t+diff)/2)
    print(cal(arr,s1,n))

        






