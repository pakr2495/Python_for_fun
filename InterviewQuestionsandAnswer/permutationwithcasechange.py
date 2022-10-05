ip = "a1"
op = ""

def cal(ip,op):
    if len(ip) == 0:
        print(op)
        return
    if ip[0].isdigit():
        op = op + ip[0]
        ip = ip[1:]
        cal(ip,op)
    else:
        op1 = op + ip[0].upper()
        op2 = op + ip[0].lower()
        ip = ip[1:]
        cal (ip,op1)
        cal (ip,op2)

cal(ip,op)