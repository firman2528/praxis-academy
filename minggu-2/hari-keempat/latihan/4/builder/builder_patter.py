class Director :
    __builder = None

    def setBuilder(self, builder) :
        self.__builder = builder

    def getCar(self) :
        car = Car()

        #first goes to body 
        body = self.__builder.getBody()
        car.setBody(body)

        #then engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # and four wheels
        i = 0
        while i < 4 :
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i +=1
        return car

    

#The whole product
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
        
    def specification (self) :
        print("Body {}", self.__body.shape)
        print("Engine horsepower {}", self.__engine.horsepower)
        print("tire size {}", self.__wheels[0].size)

class Builder() :
    def getWheel(self) : pass
    def getEngine(self) : pass
    def getBody(self) : pass


class JetBuilder(Builder) :
    def getWheel(self) :
        wheel = Wheel()
        wheel.size=22
        return wheel
        
    def getEngine(self) :
        engine = Engine()
        # engine.horsepower = 400
        engine.horsepower = 400
        return engine
        
    def getBody(self) :
        body = Body()
        body.shape = "SUV"
        return body

class Wheel :
    size = None

class Engine: 
    horsepower = None

class Body :
    shape = None

def main () :
    jip = JetBuilder()
    direktur = Director()

    print("Building Jeep")
    direktur.setBuilder(jip)
    jeep = direktur.getCar()
    jeep.specification()
    print("")

if __name__ == "__main__" :
    main()

        