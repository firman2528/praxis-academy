from abstract_coffee import AbstractCoffee

class ConcreteCoffee(AbstractCoffee) :
    def get_cost(self) :
        return 1.00

    def get_ingredients(self) :
        return "Coffee"