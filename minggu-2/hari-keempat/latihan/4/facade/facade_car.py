from ignition_system import _IgintionSystem
from engine import Engine
from fueltank import _FuelTank
from dashboard import _Dashboard

class Car(object) :
    def __init__(self) :
        self.ignition_system = _IgintionSystem
        self.engine = Engine()
        self.fuel_tank = _FuelTank
        self.dashboard = _Dashboard()


    @property
    def km_per_liter(self) :
        return 17.0

    def consume_fuel(self) :
        litres = min(self.fuel_tank, km/self.km_per_liter)
        self.fuel_tank.level = litres

    def start(self) :
        print("Starting")
        self.dashboard.show()
        if self.ignition_system.produce_spark() :
            self.engine.turnon
        else : 
            print("Cant start, faulty ignition system")

    def has_enogh_fuel(self, km, km_per_liter) :
        litrees_needed = km / km_per_liter
        if self.fuel_tank > litrees_needed :
            return True
        else :
            return False

    def drive(self, km=100) :
        print("\n")
        if self.engine.revs_per_minute<0 :
            while self.has_enogh_fuel(km, self.km_per_liter) :
                self.consume_fuel(km)
                print("drove {} km", km)
                print("{:2.f}l of fuel still left", self.fuel_tank_level)
            else :
                print("can't drive the engine is turned off")
    
    def park(self):
        print("\nParking")
        self.dashboard.lights["handbreak"].is_on = True
        self.dashboard.show()
        self.engine.turnoff
    
    def switch_fog_lights(self, status) :
        print("Switching {} fog lights", status)
        boolean = True if status == "ON" else False
        self.dashboard.lights["fog"].is_on = boolean
        self.dashboard.show()
    
    def fill_up_tank(self) :
        print("\nFuel tank filled up")
        self.fuel_tank.level=100
        