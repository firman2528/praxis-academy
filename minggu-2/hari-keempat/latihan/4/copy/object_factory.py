from prototype1 import Prototype1
from prototype2 import Prototype2

class ObjectFactory() :
    """ Manages prototypes.
    Static factory, that encapsulates prototype
    initialization and then allows instatiation
    of the classes from these prototypes.
    """
    __type1value2 = None
    __type1value1 = None
    __type2value1 = None
    __type2value2 = None

    @staticmethod 
    def initialize() :
       ObjectFactory.__type1value1 = Prototype1(1)
       ObjectFactory.__type1value2 = Prototype1(2)
       ObjectFactory.__type2value1 = Prototype2(1)
       ObjectFactory.__type2value2 = Prototype2(2)

    @staticmethod
    def getType1value1 () :
        return ObjectFactory.__type1value1

    @staticmethod
    def getType1value2 () :
        return ObjectFactory.__type1value2

    @staticmethod
    def getType2value1() :
        return ObjectFactory.__type2value1

    @staticmethod 
    def getType2value2() :
        return ObjectFactory.__type2value2

    