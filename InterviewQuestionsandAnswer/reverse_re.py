li = [1,5,3,4,2,7,6,8]

def ins(li,temp):
    if len(li) == 0 or temp<= li[len(li)-1]:
        li.append(temp)
        return
    temp1 = li.pop()
    ins(li,temp)
    li.append(temp1)


def rev(li):
    if len(li) == 1:
        return
    temp = li.pop()
    rev(li)
    ins(li,temp)

rev(li)
print(li)

