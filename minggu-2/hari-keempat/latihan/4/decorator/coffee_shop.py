from concrete_coffee import ConcreteCoffee
from milk import Milk
from sugar import Sugar
from vanilla import Vanilla


myCoffee = ConcreteCoffee()

print("Ingredients : {}, Cost : {}, Sales Tax : {}".format(myCoffee.get_ingredients(), myCoffee.get_cost(), myCoffee.get_tax()))
        
myMilk = Milk(myCoffee)
print("Ingradients : {}, Cost : {}, Sales Tax : {}".format(myMilk.get_ingredients(), myMilk.get_cost(), myMilk.get_tax()))

mySugar = Sugar(myCoffee)
print("Ingradients : {}, Cost : {}, Sales Tax : {}".format(mySugar.get_ingredients(), mySugar.get_cost(), mySugar.get_tax()))

myVanilla = Vanilla(myCoffee)
print("Ingredients : {}, Cost {}, Sales Tax : {}".format(myVanilla.get_ingradients(), myVanilla.get_cost(), myVanilla.get_tax()))

