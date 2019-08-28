class MyBaseClass() :
    def __init__(self, x,y) :
        self.x = x
        self.y = y
        
class MyDerivedClass(MyBaseClass) :
    def __init__(self, x,y,z) :
        super().__init__(x,y)
        self.z = z

# d = MyDerivedClass(1,2,3)
# print(d.z)