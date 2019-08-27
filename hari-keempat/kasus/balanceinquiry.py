from withdraw import WithDraw

class Balanceinquiry :
    balance = 0

    def __init__(self) :
        pass

    @classmethod
    def setbalance(cls, nominal) :
        cls.balance = nominal
        return cls.balance 

    @staticmethod
    def getbalance() :
        return Balanceinquiry.balance


    
