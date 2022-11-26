

# 0,1,1,2,3,5

def fib():
    a=0
    b =1
    while(True):
        yield a
        a,b = b,a+b

res = fib()

for i in range(0,10):
    print(next(res))