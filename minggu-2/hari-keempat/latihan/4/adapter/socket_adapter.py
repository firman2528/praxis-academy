from eropasocket import EuropeanSocketInterface

class Socket(EuropeanSocketInterface) :
    def voltage(self) :
        return 230

    def live(self) :
        return 1

    def neutral(self) :
        return -1

    def earth(self) :
        return 0

