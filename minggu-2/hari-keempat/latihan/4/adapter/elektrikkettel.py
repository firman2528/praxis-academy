class ElectricKettle :
    __power = None

    def __init__(self, power) :
        self.__power = power

    def boil(self) :
        if self.__power.voltage() > 110 :
            print("Kettel on fire")
        else :
            if self.__power.live() == 1 and self.__power.neutral() == -1 :
                print("Coffee time")
            else : 
                print("No power")