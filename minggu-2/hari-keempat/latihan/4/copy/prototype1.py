from prototype import Prototype
import copy

class Prototype1(Prototype) :
    def __init__(self,number) :
        self._type = "Type1"
        self._value = number

    def clone(self) :
        return copy.copy(self)

        