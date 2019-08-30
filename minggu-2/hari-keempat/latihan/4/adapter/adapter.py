from usasocketinterface import USASocketInterface

class Adapter(USASocketInterface) :
    __socket = None

    def __init__(self, socket) :
        // menginisiasikan __socket ke object adapter 
        self.__socket = socket
    
    def voltage(self) :
        return 110

    def live(self) :
        return self.__socket.live()

    def neutral(self) :
        return self.__socket.neutral()

    def earth(self) :
        return self.__socket.earth()