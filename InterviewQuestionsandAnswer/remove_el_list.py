li = [1,2,4,5,6,8,7]
k =10

def remove(li,k):
    if len(li)==0:
        return
    if k==1:
        li.pop()
        return
    temp = li.pop()
    remove(li,k-1)
    li.append(temp)

remove(li,k)
print(li)