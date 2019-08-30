from abstract_coffee_decorator import AbstractCoffeeDecorator

class Sugar(AbstractCoffeeDecorator) :
    def __init__(self, decorated_coffee) :
        AbstractCoffeeDecorator.__init__(self, decorated_coffee)

    def get_cost(self) :
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) :
        return self.decorated_coffee.get_ingredients() + ', sugar'