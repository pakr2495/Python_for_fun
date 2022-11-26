
# longest common subsequence
x = "abdcgwqeqweqw"
y = "abcqwzxzczxc"
m = len(x)
n = len(y)
temp = []
op = ''
res = ['']

def lcs(x,y,m,n,op):
    if m == 0 or n == 0:
        if len(res[0])<= len(op):
            res[0] = op
        return
    if x[m-1] == y[n-1]:
        op = op + x[m-1]
        lcs(x,y,m-1,n-1,op)
    else:
        lcs(x,y,m,n-1,op)
        lcs(x,y,m-1,n,op)
lcs(x,y,m,n,op)
print(res[0][::-1])       