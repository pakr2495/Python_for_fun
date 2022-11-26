li = "aabacebebebe"
i = 0
j = 0
l = len(li)
temp = {}
count = 0
k = 3
res = 0
while(j<l):
    if temp.get(li[j]):
        temp[li[j]] = temp[li[j]] + 1
    else:
        temp[li[j]] = 1
        count = count + 1
    if count<k:
        j = j + 1
    elif count == k:
        res = max(res,(j-i)+ 1)
        j = j +1
    elif count>k:
        while(count>k):
            if li[i] in temp:
                temp[li[i]] = temp[li[i]] - 1
                if temp[li[i]] == 0:
                    count = count -1
            i = i +1
        j = j + 1
print(res)



