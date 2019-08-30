import copy
from prototype import Prototype


class Prototype2(Prototype) :
    def __init__(self, number) :
        self._type ="Type2"
        self._value=number

    def clone(self) :
        return copy.copy(self)

    