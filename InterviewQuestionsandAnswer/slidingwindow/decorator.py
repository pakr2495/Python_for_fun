def parentclass(f):
    def subcl(a):
        print('before')
        res = f(a)
        print('after')
        return res
    return subcl


@parentclass
def cal(a):
    print(a)
    print("hi")
    return 2

print(cal(2))