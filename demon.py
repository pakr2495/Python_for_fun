from threading import Thread

def add (num1,num2):
    print(num1+num2) 

def mul(num2,num3):
    print(num2*num3) 

def ex_demon():
    for i in range(100):
        print("Background Process")

t1 = Thread(target=add, args=(2,3))
t2 = Thread(target=mul, args=(2,3))
t3 = Thread(target=ex_demon)
t1.setName = 'first thread'
t3.setDaemon(True)
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
print('main therad completed')