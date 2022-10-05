s = ['h','e','l','l','o']
def cal(s):
    print(s)
    if len(s) <= 1:
        return 
    temp = s[0]
    s[0] = s[-1]
    s[-1] = temp
    cal(s[1:-1])

cal(s)
print(s)