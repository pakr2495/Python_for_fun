res = 0
x = "abcd"
y = "abce"
count = 0
m = len(x)
n = len(y)
def cal(x,y,m,n,count):
    if m == 0 or n == 0:
        return 
    if x[m-1] == y[n-1]:
        return cal(x,y,m-1,n-1) + 1
    else:

        res = max(res,count)
        count = 0
        cal(x,y,m-1,n)
        cal(x,y,m,n-1)

cal(x,y,m,n)
print(res)