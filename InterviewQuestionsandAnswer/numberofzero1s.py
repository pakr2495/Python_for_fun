n =3 
op =""
zero = 0
one = 0

def cal(n,zero,one,op):
    if n == 0:
        print(op)
        return
    if one - zero >=1:
        op1 = op + '0'
        op2 = op + '1'
        cal(n-1,zero+1,one,op1)
        cal(n-1,zero,one+1,op2)
    else:
        op = op + '1'
        cal(n-1,zero,one+1,op)

cal(n,zero,one,op)