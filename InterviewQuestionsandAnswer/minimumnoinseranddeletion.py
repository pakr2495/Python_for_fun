####
# minimum number of insertion or deletion to convert the string a to string b
####

s1 = "ABCDEFG"
s2 = "BCDFQA"
m = len(s1)
n = len(s2)

def lcf(s1,s2,m,n):
    if m  == 0 or n == 0:
        return 0
    if s1[m-1] == s2[n-1]:
        return 1 + lcf(s1,s2,m-1,n-1)
    else:
        return max(lcf(s1,s2,m-1,n),lcf(s1,s2,m,n-1))

res = lcf(s1,s2,m,n)

print("number of insertion:",len(s2)-res)
print("number of deletion:",len(s1)-res)