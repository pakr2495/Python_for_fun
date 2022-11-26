li = [2,5,3,6,7,-7,2]
s = 8
temp = {}
count = 0
for i in li:
    if temp.get(s-i):
        count = count + 1
    else:
        temp[i] = i

print(count)

