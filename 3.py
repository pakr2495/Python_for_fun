class Rectangle(object):
    def __init__(self,w,h):
        self.width = w
        self.height = h

    def perimeter(self):
        return 2*(self.width+self.height)
    
    def __str__(self):
        return '(R:%s %s)' %(self.width,self.height)

r1 = Rectangle(12,24)
print(r1.perimeter())