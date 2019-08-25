# from balanceinquiry import Balanceinquiry
class Deposit() :

    totaldeposit = 0

    @classmethod
    def count(cls, nominal) :
        # menambahkan deposit yang masuk ke balance inquiry
        cls.totaldeposit = nominal
        return cls.totaldeposit 
        
    @classmethod
    def getdeposit(cls) :
        return cls.totaldeposit