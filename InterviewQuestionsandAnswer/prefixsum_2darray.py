"""
if x = 0 and y = 0
p[x][y] = a[x][y]

if x=0 and y>0

p[x][y] = p[x][y-1] + a[x][y]

if x>0 and y=0

p[x][y] = p[x-1][y] + a[x][y]

if x>0 and y>0

p[x][y] = p[x-1][y] + p[y][x-1] - p[x-1][y-1] + a[x][y]

"""


arr = [[1,2,3],[4,5,6],[8,9,10]]

row = len(arr)
col = len(arr[0])

for y in range(1,col):
    arr[0][y] = arr[0][y] + arr[0][y-1]

for x in range(1,row):
    arr[x][0] = arr[x][0] + arr[x-1][0]

for x in range(1,row):
    for y in range(1,col):
        arr[x][y] = arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1] + arr[x][y]

print(arr)
