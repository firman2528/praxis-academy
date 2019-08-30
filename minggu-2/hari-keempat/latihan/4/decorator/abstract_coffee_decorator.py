import six
from abc import ABCMeta
from abstract_coffee import AbstractCoffee

@six.add_metaclass(ABCMeta)
class AbstractCoffeeDecorator(AbstractCoffee) :
    
    def __init__(self, decorated_coffee) :
        self.decorated_coffee = decorated_coffee

    def get_cost(self) :
        return self.decorated_coffee.get_cost()

    def get_ingredients(self) :
        return self.decorated_coffee.get_ingredients()