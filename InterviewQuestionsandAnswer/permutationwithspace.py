"""
ip = abc
op = {a-bc,ab-c,a-b-c,abc}
"""

ip = "abc"
op = ""
op = op+ ip[0]
ip = ip[1:]

def cal(ip,op):
    if len(ip) == 0:
        print(op)
        return
    op1 = op + '-'+ip[0]
    op2 = op + ip[0]
    ip = ip[1:]
    cal(ip,op1)
    cal(ip,op2)

cal(ip,op)