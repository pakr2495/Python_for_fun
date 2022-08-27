"""
form subest sum array first
next calculate using formula minimum(sum - 2*s1) for the last row
"""

array = [1,2,5,7,9]
s = sum(array)
n = len(array)

t = []
for i in range(0,n+1):
    t.append([])
    for j in range(0,s+1):
        if j == 0:
            t[i].append(True)
        elif i == 0:
            t[i].append(False)

for i in range(1,n+1):
    for j in range(1,s+1):
        if array[i-1]<=j:
            t[i].append(t[i-1][j-array[i-1]] or t[i-1][j])
        else:
            t[i].append(t[i-1][j])

temp = []
for j in range(0,len(t[n])):
    if t[n][j]:
        temp.append(j)
minimum = s
for i in temp:
    minimum = min(minimum,abs(s-(2*i)))
print(minimum)