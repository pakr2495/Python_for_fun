
arr = [1,2,20,3,12,45,67,23,4,6,29]
k = 3
l = len(arr)

i = 0
j = 0
s = 0
res = sum(arr)

while(j<l):
    s = s + arr[j]
    if((j-i)+1 < k):
        j = j + 1
    elif (j-i)+ 1 == k:
        res = min(res,s)
        s = s - arr[i]
        i= i+1
        j= j + 1
print(res)

###############
# first negative

li = [1,-2,3,-4,-5,1,2]
k = 3
i = 0
j = 0
l = len(li)
temp = []
res = []
while(j<l):
    if li[j]<0:
        temp.append(li[j])
    if (j-i) + 1 < k:
        j = j + 1
    elif (j-i) + 1 == k:
        if len(temp) == 0:
            res.append[0]
        else:
            res.append(temp[0])
            if temp[0] == li[i]:
                temp = temp[1:]
        j = j + 1       
        i= i+1

print(res)
