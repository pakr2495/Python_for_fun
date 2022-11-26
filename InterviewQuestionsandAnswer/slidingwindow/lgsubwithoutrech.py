li = "aabacebebebe"
i = 0
j = 0
l = len(li)
temp = {}
res = 0
while(j<l):
    if temp.get(li[j]):
        temp[li[j]] = temp[li[j]] + 1
    else:
        temp[li[j]] = 1
    if len(temp.keys()) == (j-i)+1:
        res = max(res,(j-i)+ 1)
        j = j +1
    elif len(temp.keys())<(j-i)+1:
        while(len(temp.keys())<(j-i)+1):
            if li[i] in temp:
                temp[li[i]] = temp[li[i]] - 1
                if temp[li[i]] == 0:
                    del temp[li[i]]
            i = i +1
        j = j + 1
print(res)



