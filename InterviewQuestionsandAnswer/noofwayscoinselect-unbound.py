# maximum number of ways coin can be selected
c = [1,2,5,6,3]
w = 5
n = len(c)

temp = []

for i in range(0,n+1):
    temp.append([])
    for j in range(0,w+1):
        if j  == 0:
            temp[i].append(1)
        elif i  == 0:
            temp[i].append(0)
        else:
            temp[i].append(-1)


def cal(c,w,n):
    # if w  == 0:
    #     return 1
    # if n == 0:
    #     return 0
    if temp[n][w]!= -1:
        return temp[n][w]
    if c[n-1]<=w:
        temp[n][w] = cal(c,w-c[n-1],n) + cal(c,w,n-1)
    else:
        temp[n][w] =  cal(c,w,n-1)
    return temp[n][w]

print(cal(c,w,n))