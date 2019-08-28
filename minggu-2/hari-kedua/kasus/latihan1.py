class A :
    def truth(self) :
        return 'All numbers are even'
    
class B(A) :
    def truth(self) :
        return 'Bilangan ganjil'

class C(A) :
    def truth(self) :
        return 'Some number are even'
    
class D(B,C) :
    
    def truth(num) :
        if num%2 == 0 :
            return A.truth(self)
        else :
            return super().truth()
            
# d = D()
# d.truth(5)