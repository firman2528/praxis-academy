from facade_car import Car

def main() :
    car = Car()
    car.start()
    car.drive()
    car.switch_fog_lights("ON")
    car.switch_fog_lights("OFF")
    car.park()
    car.drive()
    car.start()
    car.drive()

if __name__ == "__main__" :
    main()