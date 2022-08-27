Pn = [1,5,4,7]
wn = [1,4,2,3]
W = 7
n = len(Pn)
temp = []
for i in range(0,n+1):
    temp.append([])
    for j in range(0,W+1):
        temp[i].append(-1)

def knapsack(pn,wn,w,n):
    if n == 0 or w == 0:
        return 0
    if temp[n][w] != -1:
        return temp[n][w]
    if wn[n-1]<= w:
        temp[n][w] = max(pn[n-1] + knapsack(pn,wn,w-wn[n-1],n-1),knapsack(pn,wn,w,n-1))
        return temp[n][w]
    else:
        temp[n][w] = knapsack(pn,wn,w,n-1)
        return temp[n][w]

print(knapsack(Pn,wn,W,n))

Pn = [1,5,4,7]
wn = [1,4,2,3]
W = 7
n = len(Pn)

temp1 = []
for i in range(0,n+1):
    temp1.append([])
    for j in range(0,W+1):
        if i == 0 or j == 0:
            temp1[i].append(0)

for i in range(1,n+1):
    for j in range(1,W+1):
        if wn[i-1]<=j:
            temp1[i].append(max(Pn[i-1]+temp1[i-1][j-wn[i-1]],temp1[i-1][j]))
        else:
            temp1[i].append(temp1[i-1][j])

print(temp1)
