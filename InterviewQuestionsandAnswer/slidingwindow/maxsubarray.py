li = [1,3,-1,-3,2,3,6,7]
k = 3
l = len(li)
i = 0
j = 0
temp = []
res = []

while(j<l):
    while(len(temp)!=0 and temp[-1]<li[j]):
        temp = temp[:-1]
    temp.append(li[j])
    if (j-i) +1 <k:
        j = j + 1
    elif (j-i) + 1 == k:
        print(temp)
        res.append(temp[0])
        if temp[0] == li[i]:
            temp = temp[1:]
        j = j + 1
        i = i + 1

print(res)

