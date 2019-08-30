class Car :
    def __init__(self) :
        self.__wheels = list()
        self.__engine = None
        self.__body = None
    
    def setBody(self, body) :
        self.__body = body
    
    def attachWheel(self, wheel) :
        self.__wheels.append(wheel)

    def setEngine(self, engine) :
        self.__engine = engine
    
    def specification(self) :
        print("Body :", self.__body.shape)
        print("Engine horsepower :", self.__engine.horsepower)
        print("tire size ", self.__wheels[0].size)