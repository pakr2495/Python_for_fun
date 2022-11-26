li = [6,5,12,10,9,1]

i = 0
j = len(li)

def merge(li,i,j,m):
    l = li[i:m+1]
    n = li[m+1:j+1]
    x = 0
    y = 0
    k = i
    l1 = len(l)
    n1 = len(n)
    while(x<l1 and y<n1):
        if l[x]<n[y]:
            li[k] = l[x]
            x = x + 1
        else:
            li[k] = n[y]
            y = y + 1
        k = k + 1
    while(x<l1):
        li[k] = l[x]
        x = x + 1
        k = k + 1

    while(y<n1):
        li[k] = n[y]
        y = y + 1
        k = k +1

def mergesort(li,i,j):
    if i>=j:
        return
    m = ((i+j)//2)
    mergesort(li,i,m)
    mergesort(li,m+1,j)
    merge(li,i,j,m)

mergesort(li,i,j)
print(li)