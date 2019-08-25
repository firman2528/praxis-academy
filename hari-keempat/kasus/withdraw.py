class WithDraw() :
    
    totaltarikan = 0
  
    @classmethod
    def setwithdraw(cls, nominal) :
        cls.totaltarikan = nominal
        return cls.totaltarikan 
    
    @classmethod
    def getwithdraw(cls) :
        return cls.totaltarikan