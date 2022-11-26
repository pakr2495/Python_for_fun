
# longest common subsequence
x = "abdcefg"
y = "aceghd"
m = len(x)
n = len(y)
temp = []
for i in range(0,m+1):
    temp.append([])
    for j in range(0,n+1):
        temp[i].append(-1)

def lcs(x,y,m,n):
    if m == 0 or n == 0:
        return 0
    if temp[m][n] != -1:
        return temp[m][n]
    if x[m-1] == y[n-1]:
        temp[m][n] = 1 + lcs(x,y,m-1,n-1)
        return temp[m][n]
    else:
        temp[m][n] =  max(lcs(x,y,m,n-1),lcs(x,y,m-1,n))
        return temp[m][n]

print(lcs(x,y,m,n))

###### top down
x = "abdcefg"
y = "aceghd"
m = len(x)
n = len(y)
temp1 = []

for i in range(0,m+1):
    temp1.append([])
    for j in range(0,n+1):
        if i == 0 or j == 0:
            temp1[i].append(0)
        elif x[i-1] == y[j-1]:
            temp1[i].append(1 + temp1[i-1][j-1])
        else:
            temp1[i].append(max(temp1[i][j-1],temp1[i-1][j]))
print(temp1[m][n])

i  = m
j = n
res = ""
while(i>0 and j>0):
    if x[i-1] == y[j-1]:
        res = res + x[i-1]
        i = i - 1
        j = j - 1
    else:
        if temp1[i][j-1]> temp1[i-1][j]:
            j = j - 1
        else:
            i = i - 1

print(res[::-1])