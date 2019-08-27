from balanceinquiry import Balanceinquiry
from withdraw import WithDraw
from deposit import Deposit

class Atm() :

    sisa = 0
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
            Atm.sisa = Balanceinquiry.balance - nominal
            Balanceinquiry.setbalance(Atm.sisa)
            print("Anda menarik uang sejumlah :",nominal)
            print("Saldo anda adalah : ", Balanceinquiry.balance)
    
    @staticmethod
    def depositmoney(nominal) :
        Deposit.count(nominal)
        Balanceinquiry.balance += Deposit.totaldeposit
        print("\nYou deposited the ammount of {}".format(Deposit.getdeposit()))

Atm.depositmoney(2000)
print('\n')
Atm.withdrawmoney(1000)