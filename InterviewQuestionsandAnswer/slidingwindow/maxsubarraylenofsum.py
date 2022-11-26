li  = [4,1,1,1,2,3,5]

i = 0
j = 0

k = 5
l = len(li)
res = 0
s = 0
ans =0

while(j<l):
    s = s + li[j]
    if s<k:
        j = j +1
    elif s == k:
        ans = max(ans,(j-i)+1)
        j = j + 1
    elif s>k:
        while (s>k):
            s = s - li[i]
            i = i+1
        j = j + 1
print(ans)