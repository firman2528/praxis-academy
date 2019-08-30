from abstract_coffee_decorator import AbstractCoffeeDecorator

class Vanilla(AbstractCoffeeDecorator) :
    
    def __init__(self, decorated_coffee) :
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self) :
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingradients(self) :
        return self.decorated_coffee.get_ingredients() + ', vanilla'