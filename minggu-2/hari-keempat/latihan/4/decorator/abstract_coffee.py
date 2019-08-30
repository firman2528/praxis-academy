import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta) 
class AbstractCoffee(object) :

    def get_cost(self) :
        pass
    
    def get_ingredients(self) :
        pass
    
    def get_tax(self) :
        return 0.1 * self.get_cost()