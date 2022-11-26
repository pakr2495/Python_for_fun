w = 8
pn = [10,2,5,7,3,10,4,9]
ln = [1,2,3,4,5,6,7,8]
n = len(ln)

temp = []

for i in range(0,n+1):
    temp.append([])
    for j in range(0,w+1):
        if i == 0 or j == 0:
            temp[i].append(0)
        else:
            temp[i].append(-1)

def unks(ln,pn,n,w):
    # if n == 0 or w == 0:
    #     return 0
    if temp[n][w]!= -1:
        return temp[n][w]
    if (ln[n-1]<=w):
        temp[n][w] = max(pn[n-1]+unks(ln,pn,n,w-ln[n-1]),unks(ln,pn,n-1,w))
    else:
        temp[n][w] = unks(ln,pn,n-1,w)
        
    return temp[n][w]

print(unks(ln,pn,n,w))