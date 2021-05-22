def i(l,ic):
    ii = 0
    while ii <len(l):
        l[ii] = l[ii] + ic
        ii = ii+1

values = [1,2,3]
print(i(values,2))
print(values)