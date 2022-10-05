ip ='aabbcd'
op =''
s = set()

def cal(ip,op):
    if len(ip) == 0:
        s.add(op)
        return
    op1 = op + ip[0]
    op2 = op 
    ip = ip[1:]
    cal(ip,op1)
    cal(ip,op2)
cal(ip,op)
print(s)