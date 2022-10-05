n = 5
k = 2
k = k-1
index = 0
li = [i for i in range(1,n+1)]

def cal(k,index):
    if len(li) == 1:
        res = li[0]
        return res
    index = (index+k)%len(li)
    del li[index]
    return cal(k,index)


print(cal(k,index))

