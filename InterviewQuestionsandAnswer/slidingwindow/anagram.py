sub = "abc"
s = "abcacxbcaxxacbxxx"
k = len(sub)
l = len(s)
temp = {}

for i in sub:
    if temp.get(i):
        temp[i] = temp[i] + 1
    else:
        temp[i] = 1
count  = len(temp.keys())
res = 0

i = 0
j = 0

while (j<l):
    if s[j] in temp:
        temp[s[j]] = temp[s[j]] - 1
        if temp[s[j]] == 0:
            count = count - 1
    if (j-i) + 1 < k:
        j = j + 1
    elif(j-i) + 1 == k:
        if count == 0:
            res = res + 1
        j = j + 1
        if s[i] in temp:
            temp[s[i]] = temp[s[i]] + 1
            if temp[s[i]] == 1:
                count = count + 1
        i = i + 1
print(res)
