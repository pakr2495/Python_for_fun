def fib(n):
    a,b = 0,1
    while True:
        yield a
        a, b = b,b+a

a = fib(5)

for i in range(2):
    print(next(a))



li = [1,2,3,4,5]
li.append(li)

li[5][0] = 2


print(li)


n = [1,2,3,4]
res = iter(n)

print(next(res))



class A:
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        self.n = self.n + 1
        if self.n>10:
            raise StopIteration
        return self.n

a = A()
res = iter(a)
print(next(res))
for i in res:
    print(i)



import contextlib

@contextlib.contextmanager
def my_context(a):
    a = a * 10
    print("before")
    yield a
    print("After completed task")

with my_context(10) as res:
    print(res)
    print("doing operation")

print('done')