from car import Car
class Director : 
    __builder = None

    def setBuilder(self, builder) :
        self.__builder = builder
    
    def getCar(self) :
        car = Car()

        #first goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        #Then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        i = 0
        while i<4 :
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1
        return car
