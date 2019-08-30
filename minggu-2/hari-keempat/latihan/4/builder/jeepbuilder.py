from builder import Builder
from parts import Wheel, Engine, Body
class JeepBuilder(Builder) :
     
    def getWheel(self) :
         wheel = Wheel()
         wheel.size = 22
         return wheel

    def getEngine(self) :
        engine = Engine()
        engine.horsepower = 4000
        return engine
    
    def getBody(self) :
        body = Body()
        body.shape = "SUV"
        return body