class Singleton:
    instance = None
    @staticmethod
    def get_instance():
        if Singleton.instance is None:
            Singleton()
        return Singleton.instance
    
    def __init__(self) -> None:
        if Singleton.instance is None:
            Singleton.instance = self
        else:
            raise "Already Present"


s1 = Singleton.get_instance()
s2 = Singleton.get_instance()
print(s2)
print(s1)
s1.x =4
print(s2.x)

#----------------------
class Singleton1:
    instance = None

    def __new__(cls):
        if Singleton1.instance is None:
            cls.instance = super(Singleton1,cls).__new__(cls)
        return cls.instance
s1 = Singleton1()
s2 = Singleton1()
print(s1)
print(s2)


