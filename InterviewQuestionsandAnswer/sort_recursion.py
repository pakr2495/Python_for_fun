li = [2,5,1,7,3,8,9]

def insert(li:list,temp):
    if len(li) == 0 or temp>=li[len(li)-1]:
        li.append(temp)
        return
    temp1 = li.pop()
    insert(li,temp)
    li.append(temp1)

def c_sort(li:list):
    if len(li) == 1:
        return
    temp = li.pop()
    c_sort(li)
    insert(li,temp)

c_sort(li)
print(li)