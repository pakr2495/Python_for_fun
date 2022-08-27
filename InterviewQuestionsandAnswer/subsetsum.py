arr = [1,5,4,3,8]
s = 11
n = len(arr)
temp =[]
for i in  range(0,n+1):
    temp.append([])
    for j in range(0,s+1):
        temp[i].append(-1)
def cal(arr,s,n):
    if s == 0:
        return True
    if n == 0 :
        return False
    if (temp[n][s]!=-1):
        return temp[n][s]
    if arr[n-1]<=s:
        temp[n][s] = cal(arr,s-arr[n-1],n-1) or cal(arr,s,n-1)
        return temp[n][s]
    else:
        temp[n][s] = cal(arr,s,n-1)
        return temp[n][s]

print(cal(arr,s,n))
arr = [1,5,6,3,8]
s = 11
n = len(arr)
temp1= []
for i in range(0,n+1):
    temp1.append([])
    for j in range(0,s+1):
        if j ==0:
            temp1[i].append(True)
        elif i == 0:
            temp1[i].append(False)
for i in range(1,n+1):
    for j in range(1,s+1):
        if arr[i-1]<=j:
            temp1[i].append(temp1[i-1][j-arr[i-1]] or temp1[i-1][j])
        else:
            temp1[i].append(temp1[i-1][j])

print(temp1[n][s])

arr = [1,5,6,3,8,11]
s = 11
n = len(arr)

temp2 = []
for i in range(0,n+1):
    temp2.append([])
    for j in range(0,s+1):
        temp2[i].append(-1)


        
#count of subset
def cal1(arr,s,n):
    if s == 0:
        return 1
    if n == 0:
        return 0
    if temp2[n][s]!= -1:
        return temp2[n][s]

    if arr[n-1]<=s:
        temp2[n][s] = cal1(arr,s-arr[n-1],n-1) + cal1(arr,s,n-1)
        return temp2[n][s]
    else:
        temp2[n][s] = cal1(arr,s,n-1)
        return temp2[n][s]

print(cal1(arr,s,n))

