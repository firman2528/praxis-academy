from balanceinquiry import Balanceinquiry
from withdraw import WithDraw
from deposit import Deposit

class Atm() :

    def checkbalance(self) :
        print("Your current balance is {}".format(Balanceinquiry.getbalance()))

    @staticmethod
    def withdrawmoney(nominal) :
        if (Balanceinquiry.balance == 0) :
            print("\Your current balance is zero")
        elif (Balanceinquiry.balance <= 500) :
            print("You dont have suficient money to draw")
        elif (Balanceinquiry.balance < nominal) :
            print("Saldo anda tidak mencukupi")
        else :
            self.sisa = Balanceinquiry.balance - nominal
            Balanceinquiry.setbalance(self.sisa)
            return Balanceinquiry.setbalance
    
    @staticmethod
    def depositmoney(nominal) :
        Deposit.count(nominal)
        print("\nYou deposited the ammount of {}".format(Deposit.getdeposit()))
        
