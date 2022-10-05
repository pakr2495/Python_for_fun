from tkinter import N


n = 3
open = n 
close = n 
op = ""
def cal(open,close,op):
    if open == 0 and close == 0:
        print(op)
        return
    if open == 0:
        op = op + ")"
        cal(open,close-1,op)
    elif open == close:
        op = op + "("
        cal(open-1,close,op)
    else:
        o1 = open -1
        c1 = close -1
        op1 = op + '('
        op2 = op + ')'
        cal(o1,close,op1)
        cal(open,c1,op2)
cal(open,close,op)